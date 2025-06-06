import serial
import requests
import time
import datetime

SERIAL_PORT = '/dev/ttyUSB0' 
BAUD_RATE = 115200
API_URL = 'https://api.carbonhub.app/emission/collect'
REPORT_URL = 'https://api.carbonhub.app/emission/report'
API_KEY = ''

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2) 

print("Monitoring CO2 dari ESP32...\n")

def send_data(url, payload):
    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response

while True:
    try:
        line = ser.readline().decode('utf-8').strip()

        if "Estimas" in line and "CO2" in line:
            try:
                parts = line.split('|')
                co2_raw = parts[2].split(':')[1].strip().replace('ppm', '').strip()
                co2_value = float(co2_raw)
                
                # Check if line contains anomaly information
                is_anomaly = "Anomali: Ya" in line

                # Prepare payload
                payload = {
                    "ppm": co2_value,
                    "time": datetime.datetime.now(datetime.UTC).isoformat()
                }

                # print(payload)

                # Send to appropriate endpoint
                if is_anomaly:
                    response = send_data(REPORT_URL, payload)
                    print(f"[{datetime.datetime.now(datetime.UTC).isoformat()}] Anomaly detected! Sent to report endpoint: {payload} | Status: {response.status_code}")
                else:
                    response = send_data(API_URL, payload)
                    print(f"[{datetime.datetime.now(datetime.UTC).isoformat()}] Normal reading sent: {payload} | Status: {response.status_code}")

            except Exception as parse_err:
                print(f"Gagal parsing line: {line} → {parse_err}")

        time.sleep(1)

    except Exception as e:
        print(f"[Error] {e}")
        time.sleep(2)