# CarbonHub IoT – MQ135 CO₂ Sensor Integration

Membaca data estimasi emisi karbon (CO₂) dari sensor MQ135 yang terhubung ke ESP32 dan mengirimkannya ke server melalui HTTP POST setiap detik.

---

## IoT Wiring Structure (ESP32 ⇄ MQ135)

| MQ135 Pin | ESP32 Pin |
|-----------|-----------|
| VCC       | 5V        |
| GND       | GND       |
| AOUT      | GPIO15    |

> Pastikan menggunakan pin ADC ESP32 (seperti GPIO15) untuk input analog dari AOUT MQ135.

---

## 🚀 How to Run

1. **Jangan membuka aplikasi lain (contoh : Arduino IDE) yang sedang menggunakan port USB/serial.**
2. Jalankan skrip:
   ```bash
   python3 mq135.py
