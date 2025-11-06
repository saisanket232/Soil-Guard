import requests, csv, time, datetime

BLYNK_TOKEN = "YEm2JcFpYlHIgNO_vvImjReH-GLJMN-P"

with open("soilguard_log.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "moisture", "temperature", "pump_state"])
    print("⏱️  Logging started… press Ctrl+C to stop.\n")
    while True:
        try:
            moisture = requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_TOKEN}&V0").text
            temperature = requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_TOKEN}&V1").text
            pump_state = requests.get(f"https://blynk.cloud/external/api/get?token={BLYNK_TOKEN}&V2").text
            ts = datetime.datetime.now().isoformat(timespec='seconds')
            writer.writerow([ts, moisture, temperature, pump_state])
            f.flush()
            print(f"{ts} | Moisture={moisture} | Temp={temperature} | Pump={pump_state}")
            time.sleep(120)
        except Exception as e:
            print("Error:", e)
            time.sleep(60)
