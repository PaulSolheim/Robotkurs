// For å legge inn nettverk og passord, 
// Skru på roboten og koble mobilen til nettverket for din robot "ESP" og et tall
// og gå til adressen "192.168.4.1" i nettleseren på mobilen.

#include <ESP8266WiFi.h>
#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>
#include <BlynkSimpleEsp8266.h>
#include <SimpleTimer.h>

char auth[] = "";                     // Legg inn auth-koden fra Appen

void setup() {
  WiFiManager wifiManager;
  wifiManager.autoConnect("ESPx");    // Endre x til tallet på roboten
  // Konfigurer blynk til å koble seg til serveren
  Blynk.config(auth, IPAddress(192,168,43,16), 8442);
}

void loop() {
  Blynk.run();
}
