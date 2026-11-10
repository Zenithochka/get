#include <Wire.h>

volatile uint16_t millivolts = 0;
const float V_REF = 5.0; // ОПОРНОЕ НАПРЯЖЕНИЕ НАНО (обычно 5.0 при питании от USB)

void setup() {
  Wire.begin(0x4D);
  Wire.onRequest(onRequest); 
  Wire.onReceive(onReceive);
}

void onRequest() {
  // Отправляем старший байт, затем младший
  Wire.write((uint8_t)(millivolts >> 8));   // HI
  Wire.write((uint8_t)(millivolts & 0xFF)); // LO
}

void onReceive(int n) {
  while (n-- > 0 && Wire.available()) Wire.read();
}

void loop() {
  uint16_t raw = analogRead(A0);
  float voltage = (raw / 1024.0) * V_REF;
  millivolts = (uint16_t)(voltage * 1000); 
  delay(10); 
}