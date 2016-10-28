// --------------------------------------------------------------------------------
// Definer variabler for motorkort
#include <AFMotor.h>

AF_DCMotor venstreMotor(1, MOTOR12_64KHZ);   // lag venstreMotor objekt
AF_DCMotor hoyreMotor(2, MOTOR12_64KHZ);     // lag hoyreMotor objekt

// --------------------------------------------------------------------------------
// Definer variabler for å følge en linje
bool skalFolgeLinje = true;
unsigned int venstre, hoyre, senter;
const int venstreSensor = A0;
const int senterSensor = A1;
const int hoyreSensor = A2;

// Data strukturer for Tilstandsmaskinen som brukes til å følge en linje
struct State {
  unsigned int out;        // Tilstand som vi er i nå
  unsigned int next[6];
};  // Tabell som bestemmer neste tilstand utfra hva sensorene forteller oss
typedef const struct State StateType;

#define Center 0
#define CenterLeft 1
#define Left 2
#define CenterRight 3
#define Right 4

StateType fsm[5] = {
  {Center, { Center, CenterLeft, Left, CenterRight, Right, Right }},        // Center
  {CenterLeft, { Center,  CenterLeft, Left, CenterRight, Right, Left }},    // CenterLeft
  {Left, { Center,  CenterLeft, Left, CenterRight, Right, Left }},          // Left
  {CenterRight, { Center, CenterLeft, Left, CenterRight, Right, Right }},   // CenterRight
  {Right, { Center, CenterLeft, Left, CenterRight, Right, Right }}          // Right
};

unsigned int S;       // index til nåværende tilstand
unsigned int Input;
unsigned int Output;

void setup() {
  hoyreMotor.setSpeed(100);     // sett farten til 100 av max 255
  venstreMotor.setSpeed(100);   // sett farten til 100 av max 255

  // Sett sensorene som input
  pinMode(venstreSensor, INPUT);
  pinMode(senterSensor, INPUT);
  pinMode(hoyreSensor, INPUT);

  S = Center;

  // Pause i 8 sekunder så den ikke kjører mens den er koblet til PC'n
  delay(8000);
}

void loop() {
  Output = fsm[S].out;      // sett output fra Tilstandsmaskinen
  Robot_Output(Output);     // juster hastigheten på motorene utfra gjeldende Tilstand
  delay(10);                // kort pause som bestemmer hvor ofte vi gjør målinger med sensorene
  Input = Robot_Input();    // les sensorene
  S = fsm[S].next[Input];   // neste Tilstand avhenger av input fra sensorer og gjeldende Tilstand
}

unsigned int Robot_Input(void) {
  unsigned int resultat;
  LesFraSensorer();

  // Default er på Banen
  resultat = 0;

  // På Banen
  if ((venstre == 0) && (senter == 0) && (hoyre == 0)) resultat = 0; 
  if ((venstre == 1) && (senter == 0) && (hoyre == 1)) resultat = 0;
  if ((venstre == 0) && (senter == 1) && (hoyre == 0)) resultat = 0;

  // Senter Venstre
  if ((venstre == 1) && (senter == 0) && (hoyre == 0)) resultat = 1;
  
  // Til Venstre
  if ((venstre == 1) && (senter == 1) && (hoyre == 0)) resultat = 2;

  // Senter Høyre
  if ((venstre == 0) && (senter == 0) && (hoyre == 1)) resultat = 3;

  // Til Høyre
  if ((venstre == 0) && (senter == 1) && (hoyre == 1)) resultat = 4;

  // Utenfor banen
  if ((venstre == 1) && (senter == 1) && (hoyre == 1)) resultat = 5;

  return resultat;
}

void Robot_Output(unsigned int output) {
    switch (output) {
    case 0:   // På Banen
      venstreMotor.setSpeed(80);
      hoyreMotor.setSpeed(80);
      break;
    case 1:   // Senter Venstre
      venstreMotor.setSpeed(80);
      hoyreMotor.setSpeed(20);
      break;
    case 2:   // Til Venstre
      venstreMotor.setSpeed(80);
      hoyreMotor.setSpeed(20);
      break;
    case 3:   // Senter Høyre
      venstreMotor.setSpeed(20);
      hoyreMotor.setSpeed(80);
      break;
    case 4:   // Til Høyre
      venstreMotor.setSpeed(20);
      hoyreMotor.setSpeed(80);
      break;      
    }
    forover();
}

void LesFraSensorer() {
  venstre = digitalRead(venstreSensor);
  senter = digitalRead(senterSensor);
  hoyre = digitalRead(hoyreSensor);
}

void forover() {
  hoyreMotor.run(FORWARD);
  venstreMotor.run(FORWARD);
}

void stopp() {
  hoyreMotor.run(RELEASE);
  venstreMotor.run(RELEASE);
}

