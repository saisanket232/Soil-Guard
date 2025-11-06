import tensorflow as tf
import requests, numpy as np, time

# Disable oneDNN optimization message (optional)
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

BLYNK_TOKEN = "YEm2JcFpYlHIgNO_vvImjReH-GLJMN-P"

# ✅ FIXED LINE
model = tf.keras.models.load_model("moisture_lstm.h5", compile=False)

L = 5
buffer = []

while True:
    try:
        moisture = float(requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_TOKEN}&V0").text)
        temp = float(requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_TOKEN}&V1").text)
        print(f"\nLive → Moisture={moisture:.1f}%  Temp={temp:.1f}°C")

        buffer.append(moisture)
        if len(buffer) > L:
            buffer = buffer[-L:]

        if len(buffer) == L:
            X = np.array(buffer).reshape(1, L, 1)
            pred = float(model.predict(X, verbose=0))
            print(f"Predicted next moisture: {pred:.2f}%")

            if pred < 30:
                print("💧 Predicted dry → Pump ON")
                requests.get(f"https://blynk.cloud/external/api/update?token={BLYNK_TOKEN}&V2=1")
            else:
                print("🌿 Predicted sufficient → Pump OFF")
                requests.get(f"https://blynk.cloud/external/api/update?token={BLYNK_TOKEN}&V2=0")

        time.sleep(60)

    except Exception as e:
        print("Error:", e)
        time.sleep(30)
