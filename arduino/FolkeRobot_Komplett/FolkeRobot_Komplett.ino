// --------------------------------------------------------------------------------
// Definer variabler for motorkort
#include <AFMotor.h>

AF_DCMotor venstreMotor(1, MOTOR12_64KHZ);   // lag venstreMotor objekt
AF_DCMotor hoyreMotor(2, MOTOR12_64KHZ);     // lag hoyreMotor objekt

// --------------------------------------------------------------------------------
// Definer variabler for avstandsmåling med Ultralyd sensorene
const int triggerForanPin = A4;
const int ekkoForanPin = A5;

int avstandForan = 0;
int varighet;

unsigned long forrigeAvstandMillis = 0;      // skal lagre forrige tid som vi målte avstander
const long avstandInterval = 600;           // interval mellom hver gang vi måler avstander (millisekunder)

// --------------------------------------------------------------------------------
// Definer variabler for å spille en sang
const int buzzerPin = A3;
const int songLength = 18;
char notes[] = "cdfda ag cdfdg gf "; // a space represents a rest

// Beats er en tabell av varighet for hver note og hver pause.
// En "1" representerer en kvart-note, "2" en halv-note etc.
// Ikke glem at også pausene trenger en varighet.
int beats[] = {1, 1, 1, 1, 1, 1, 4, 4, 2, 1, 1, 1, 1, 1, 1, 4, 4, 2};

// tempo bestemmer hvor fort sangen skal spilles.
// For å spille sangen fortere må du velge en mindre verdi.
int tempo = 150;

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
  Serial.begin(9600);

  pinMode(buzzerPin, OUTPUT);
  pinMode(triggerForanPin, OUTPUT);
  pinMode(ekkoForanPin, INPUT);

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
  //styrAvstandsMaaling();

  // kode for å følge en linje som bruker en Tilstandsmaskin
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
  if (avstandForan == 0 || avstandForan > 10) {
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
  } else {
    stopp();
  }
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
  // Stopp motorene
  hoyreMotor.run(RELEASE);
  venstreMotor.run(RELEASE);
}

void styrAvstandsMaaling() {
  // Styrer hvor ofte avstander skal leses siden det tar litt tid (ca. 15 millisek. nå)
  unsigned long gjeldendeMillis = millis();

  if (gjeldendeMillis - forrigeAvstandMillis >= avstandInterval) {
    // lagre tiden for avstandsmåling som forrige tid til bruk senere
    forrigeAvstandMillis = gjeldendeMillis;
    lesAvstander();           // avstandsvariablene har nå fått verdi og kan brukes når roboten styres
  }
}

void lesAvstander()
{
  // Mål avstand foran
  digitalWrite(triggerForanPin, HIGH);
  delayMicroseconds(10);                  // Må holde signalet høyt i minst 10us
  digitalWrite(triggerForanPin, LOW);
  varighet = pulseIn(ekkoForanPin, HIGH, 5000);
  avstandForan = (varighet / 2) / 29;
}

void spillSang()
{
  int i, duration;

  for (i = 0; i < songLength; i++) // gå gjennom sang tabellen
  {
    duration = beats[i] * tempo;  // lengden på note/pause i millisekunder

    if (notes[i] == ' ')          // er dette en pause?
    {
      delay(duration);            // da tar vi en pause
    }
    else                          // ellers, spiller vi noten
    {
      tone(buzzerPin, frequency(notes[i]), duration);
      delay(duration);            // wait for tone to finish
    }
    delay(tempo / 10);            // brief pause between notes
  }
}

int frequency(char note)
{
  // Denne funksjonen tar en note-bokstav (a-g), og returnerer
  // den riktige frekvensen i Hz som skal brukes i tone() funksjonen.

  int i;
  const int numNotes = 8;  // antall noter vi har definert

  // De følgende tabellene inneholder note bokstavene
  // og deres frekvenser.

  char names[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C' };
  int frequencies[] = {262, 294, 330, 349, 392, 440, 494, 523};

  // Vi søker nå igjennom tabellen for navm og hvis vi finner bokstaven så
  // returnerer vi den tilsvarende frekvensen

  for (i = 0; i < numNotes; i++)  // gå gjennom navnene
  {
    if (names[i] == note)         // er dette riktig bokstav?
    {
      return (frequencies[i]);    // Ja! Returner frekvensen
    }
  }
  return (0); // Vi så gjennom alt og fant ikke note-bokstaven,
  // vi må allikevel gi en returverdi så vi returnerer 0.
}


