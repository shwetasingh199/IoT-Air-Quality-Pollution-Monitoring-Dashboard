#include "DHT.h"

#define DHTPIN 4
#define DHTTYPE DHT22

#define MQ135_PIN 34

DHT dht(DHTPIN, DHTTYPE);

void setup() {

  Serial.begin(115200);

  dht.begin();
}

void loop() {

  int aqi = analogRead(MQ135_PIN);

  float temp =
      dht.readTemperature();

  float hum =
      dht.readHumidity();

  Serial.print("AQI: ");
  Serial.println(aqi);

  Serial.print("Temp: ");
  Serial.println(temp);

  Serial.print("Humidity: ");
  Serial.println(hum);

  delay(2000);
}