#define MQ135_PIN 15 

void setup() {
  Serial.begin(115200);
  delay(1000); 
}

void loop() {
  int analogValue = analogRead(MQ135_PIN);

  float voltage = analogValue * (3.3 / 4095.0);

  float estimatedPPM = (analogValue / 4095.0) * 1000.0;

  Serial.print("Nilai ADC: ");
  Serial.print(analogValue);
  Serial.print(" | Tegangan: ");
  Serial.print(voltage, 2);
  Serial.print(" V | Estimasi CO2: ");
  Serial.print(estimatedPPM, 1);
  Serial.println(" ppm");

  delay(1000); 
}