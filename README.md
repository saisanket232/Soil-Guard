# SoilGuard

SoilGuard: An IoT and LSTM-Based Predictive Maintenance System for Smart Farming

## Overview

SoilGuard is an intelligent irrigation system that combines Internet of Things (IoT) sensors with machine learning to predict soil moisture levels and optimize water usage in agriculture. The system uses real-time sensor data from Blynk-connected devices and an LSTM (Long Short-Term Memory) neural network to forecast future moisture conditions, enabling proactive irrigation management.

## Features

- **Real-time Monitoring**: Continuously fetches soil moisture and temperature data from IoT sensors via Blynk API
- **Predictive Analytics**: Uses LSTM neural network to predict future moisture levels based on historical data
- **Automated Logging**: Records sensor data to CSV files for analysis and model training
- **Smart Irrigation**: Helps prevent over/under watering by predicting moisture trends

## Architecture

The system consists of three main components:

1. **AI Controller** (`ai_controller.py`): Main prediction engine that fetches live data and makes moisture predictions
2. **Data Logger** (`log_data.py`): Background service that logs sensor readings to CSV files
3. **LSTM Model** (`moisture_lstm.h5`): Pre-trained neural network for moisture prediction

## Requirements

- Python 3.7+
- Blynk account and device setup
- Internet connection for API access

### Dependencies

```
tensorflow
requests
numpy
```

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Blynk device and obtain your authentication token
4. Update the `BLYNK_TOKEN` in the Python files with your token

## Usage

### Data Logging

To start logging sensor data:

```bash
python log_data.py
```

This will create/append to `soilguard_log.csv` with timestamped readings every 2 minutes.

### AI Prediction

To run the predictive controller:

```bash
python ai_controller.py
```

This will:
- Fetch current moisture and temperature readings
- Display live sensor values
- Predict next moisture level using the LSTM model

### Blynk Setup

1. Create a Blynk account at [blynk.cloud](https://blynk.cloud)
2. Set up your IoT device with moisture sensor (V0), temperature sensor (V1), and pump control (V2)
3. Copy your authentication token to the Python scripts

## Files Description

- `ai_controller.py` - Main AI prediction controller
- `log_data.py` - Data logging utility
- `moisture_lstm.h5` - Trained LSTM model file
- `soilguard_log.csv` - Logged sensor data
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## Model Training

The LSTM model (`moisture_lstm.h5`) should be trained on historical moisture data. The model expects input sequences of 5 moisture readings to predict the next value.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is open source. Please check individual file headers for license information.
