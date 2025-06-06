#include "co2_anomaly_detector.h"

#define MQ135_PIN 15
#define WINDOW_SIZE 10  // Number of readings to keep for moving average

float readings[WINDOW_SIZE];
int readingIndex = 0;

void setup() {
  Serial.begin(115200);
  delay(1000);
  
  // Initialize readings array
  for(int i = 0; i < WINDOW_SIZE; i++) {
    readings[i] = 0;
  }
}

bool isAnomaly(float value) {
  return value < NORMAL_MIN || value > NORMAL_MAX;
}

void loop() {
  int analogValue = analogRead(MQ135_PIN);
  float voltage = analogValue * (3.3 / 4095.0);
  float estimatedPPM = (analogValue / 4095.0) * 1000.0;
  
  // Update moving window
  readings[readingIndex] = estimatedPPM;
  readingIndex = (readingIndex + 1) % WINDOW_SIZE;
  
  // Calculate moving average
  float sum = 0;
  for(int i = 0; i < WINDOW_SIZE; i++) {
    sum += readings[i];
  }
  float movingAvg = sum / WINDOW_SIZE;
  
  // Check for anomaly
  bool is_anomaly = isAnomaly(estimatedPPM);
  
  // Print results
  Serial.print("Nilai ADC: ");
  Serial.print(analogValue);
  Serial.print(" | Tegangan: ");
  Serial.print(voltage, 2);
  Serial.print(" V | Estimasi CO2: ");
  Serial.print(estimatedPPM, 1);
  Serial.print(" ppm | Rata-rata: ");
  Serial.print(movingAvg, 1);
  Serial.print(" ppm | Anomali: ");
  Serial.println(is_anomaly ? "Ya" : "Tidak");
  
  delay(1000);
} 