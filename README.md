# CarbonHub AIoT – Smart CO₂ Monitoring System

A sophisticated IoT system that combines ESP32, MQ135 sensor, and machine learning to monitor and detect anomalies in CO₂ emissions.

## 🌟 Features

- **Real-time CO₂ Monitoring**: Continuous measurement of CO₂ levels using MQ135 sensor
- **AI-Powered Anomaly Detection**: Machine learning model to identify unusual CO₂ patterns
- **Dual-Endpoint Reporting**: 
  - Normal readings → `/emission/collect`
  - Anomalies → `/emission/report`
- **Moving Average Filtering**: Smooths sensor readings for more reliable data
- **Statistical Analysis**: Z-score based anomaly detection

## 🤖 AI Implementation

The system uses a two-layer approach for anomaly detection:

1. **Statistical Thresholds**:
   - Normal range: 10-80 ppm
   - Anomaly detection using min/max thresholds
   - Moving average for noise reduction

2. **Machine Learning Model**:
   - Isolation Forest algorithm
   - Trained on synthetic data
   - Detects complex anomaly patterns

## 🔧 Hardware Setup

### IoT Wiring Structure (ESP32 ⇄ MQ135)

| MQ135 Pin | ESP32 Pin | Description |
|-----------|-----------|-------------|
| VCC       | 5V        | Power supply |
| GND       | GND       | Ground |
| AOUT      | GPIO15    | Analog output |

> **Note**: Use ESP32's ADC pin (GPIO15) for analog input from MQ135.

## 📊 Data Flow

1. **Sensor Reading**:
   - MQ135 measures CO₂ levels
   - ESP32 converts analog to digital
   - Moving average applied

2. **Anomaly Detection**:
   - Statistical check (10-80 ppm range)
   - ML model evaluation
   - Anomaly flag generation

3. **Data Transmission**:
   - Normal data → `/emission/collect`
   - Anomalies → `/emission/report`

## 🚀 Getting Started

1. **Hardware Setup**:
   ```bash
   # Connect MQ135 to ESP32 as per wiring table
   ```

2. **Software Installation**:
   ```bash
   # Install Python dependencies
   pip install -r requirements.txt
   
   # Train the model
   python train_model.py
   ```

3. **Upload to ESP32**:
   - Open `mq135-anomaly.ino` in Arduino IDE
   - Select correct board and port
   - Upload the sketch

4. **Run Monitoring**:
   ```bash
   python mq135.py
   ```

## 📈 Performance Metrics

- **Sampling Rate**: 1 reading/second
- **Normal Range**: 10-80 ppm
- **Moving Average Window**: 10 samples
- **Anomaly Detection**: Real-time

## 🔍 Monitoring Output

```
Nilai ADC: 2048 | Tegangan: 1.65 V | Estimasi CO2: 50.0 ppm | Rata-rata: 48.5 ppm | Anomali: Tidak
```
