//To input local SSID and Password, connect to WiFi "ESP6",
//and point your browser to "192.168.4.1".

#include <ESP8266WiFi.h>

#include <DNSServer.h>
#include <ESP8266WebServer.h>
#include <WiFiManager.h>
#include <BlynkSimpleEsp8266.h>
#include <SimpleTimer.h>

// MQTT Client Setup
#include <PubSubClient.h>
const char* mqtt_server = "192.168.2.16";
WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
char msg[50];
int value = 0;
long lastReconnectAttempt = 0;

//either create a config.h and define auth token there
//or comment and include here like:
char auth[] = "19c0743f6ca646d3995f164e09be7357";
//#include "Config.h"

SimpleTimer timer;
int timerId;
unsigned long counter = 0;
bool bSikkSakk = false;
int retning = 0;

void venstre()
{
  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);
  analogWrite(0, 766);
  analogWrite(2, 1023);
}

void hoyre()
{
  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);
  analogWrite(0, 1023);
  analogWrite(2, 800);
}

void rettfrem()
{
  digitalWrite(4, HIGH);
  digitalWrite(5, HIGH);
  analogWrite(0, 1023);
  analogWrite(2, 1023);
}

void sikksakk()
{
  if (bSikkSakk)
  {
    switch (retning) {
      case 0:
        rettfrem();
        break;
      case 1:
        venstre();
        break;
      case 2:
        rettfrem();
        break;
      case 3:
        hoyre();
        break;
      default:
        break;
    }
    retning++;
    if (retning > 3)
    {
      retning = 0;
    }
  }
}

void stopp()
{
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
}

void settGPIO(int GPIO, int verdi)
{
  if (GPIO == 4 || GPIO == 5)
  {
    if (verdi == 0) 
    {
      digitalWrite(GPIO, LOW);
    } else {
      digitalWrite(GPIO, HIGH);
    }
  } else {
    analogWrite(GPIO, verdi);
  }
}

BLYNK_WRITE(V0)    // Button widget is writing to pin V0
{
  int pinData = param.asInt();
  if (pinData == 1) {
    bSikkSakk = true;
  }
  else
  {
    bSikkSakk = false;
    stopp();
  }
}

// MQTT Client Reconnect
boolean reconnect() {
  if (client.connect("ESP6", "pi", "raspberry")) {
    // Once connected, publish an announcement...
    client.publish("fraEsp","Hei fra Esp6");
    // ... and resubscribe
    client.subscribe("tilEsp");
  }
  return client.connected();
}

// MQTT Client Callback
void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Melding mottatt [");
  Serial.print(topic);
  Serial.print("] ");
  Serial.println();

  int i = 0;
  char input[50];

  for (i = 0; i < length; i++) {
    input[i] = (char)payload[i];
    Serial.print((char)payload[i]);
  }
  input[i] = 0;

  // Meldingene er på formatet: "GPIO:verdi&GPIO:verdi"
  // antallet kommando par kan variere.
  // Les hvert kommando par
  char* command = strtok(input, "&");
  while (command != 0)
  {
      // Splitt kommandoen i to deler
      char* separator = strchr(command, ':');
      if (separator != 0)
      {
          // Faktisk splitte i 2 deler: erstatte ':' with 0
          *separator = 0;
          int GPIO = atoi(command);
          ++separator;
          int verdi = atoi(separator);
          
          Serial.print("GPIO: ");
          Serial.print(GPIO);
          Serial.print(" Verdi: ");
          Serial.print(verdi);
          Serial.println();
          
          settGPIO(GPIO, verdi);
          
      }
      // Finn den neste kommandoen i meldingen
      command = strtok(0, "&");
  }

  // 1 eller 0 styrer innebygd led for testing
//  char kommando = (char)payload[0];
//  switch (kommando) {
//    case '1':
//      digitalWrite(BUILTIN_LED, LOW);   // Turn the LED on
//      break;
//    case '0':
//      digitalWrite(BUILTIN_LED, HIGH);  // Turn the LED off
//      break;
//    default:
//      break;
//  }
  
}

void setup() {
  pinMode(0, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  
  WiFiManager wifiManager;
  //first parameter is name of access point, second is the password (nothing is unsecured)
  wifiManager.autoConnect("ESP6", "");
  //config blynk to connect to local server (rpi6)
  Blynk.config(auth, IPAddress(192,168,2,16), 8442);

  // MQTT Client Setup
  pinMode(BUILTIN_LED, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  Serial.begin(115200);
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  lastReconnectAttempt = 0;

  // Sett opp funksjon for sikksakk kjøring
  timer.setInterval(1000L, sikksakk);  
}

void loop() {
  // put your main code here, to run repeatedly:
  Blynk.run();
  timer.run(); // Initiates SimpleTimer  

  // MQTT Client 
  if (!client.connected()) {
    long now = millis();
    if (now - lastReconnectAttempt > 5000) {
      lastReconnectAttempt = now;
      // Attempt to reconnect
      if (reconnect()) {
        lastReconnectAttempt = 0;
      }
    }
  } else {
    // Client connected
    client.loop();

    long now = millis();
    if (now - lastMsg > 2000) {
      lastMsg = now;
      ++value;
      snprintf (msg, 75, "Hei fra Esp6 #%ld", value);
      Serial.print("Publish message: ");
      Serial.println(msg);
      client.publish("fraEsp", msg);
    }
  }
  
}
