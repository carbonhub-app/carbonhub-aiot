import serial
import requests
import time
from datetime import datetime

SERIAL_PORT = '/dev/cu.SLAB_USBtoUART' 
BAUD_RATE = 115200
SENSOR_ID = 'sensor-001'  
API_URL = 'https://api.carbonhub.app/emmission/collect'

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
time.sleep(2) 

print("Monitoring CO2 dari ESP32...\n")

while True:
    try:
        line = ser.readline().decode('utf-8').strip()

        if "Estimas" in line and "CO2" in line:
            
            try:
                parts = line.split('|')
                co2_raw = parts[2].split(':')[1].strip().replace('ppm', '').strip()
                co2_value = float(co2_raw)

                # Payload ke server
                payload = {
                    "id": SENSOR_ID,
                    "co2": co2_value,
                    "timestamp": datetime.utcnow().isoformat() + "Z"
                }

                response = requests.post(API_URL, json=payload)
                print(f"[{datetime.now().isoformat()}] Sent: {payload} | Status: {response.status_code}")

            except Exception as parse_err:
                print(f"Gagal parsing line: {line} → {parse_err}")

        time.sleep(1)

    except Exception as e:
        print(f"[Error] {e}")
        time.sleep(2)