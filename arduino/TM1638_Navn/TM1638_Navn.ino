#include <TM1638.h>

TM1638 modul(8, 9, 10);
String forNavn = "PAAL    ";
String etterNavn = "SOLHEIM ";

void setup() {
  // Kode for oppsett som kjøres en gang:
}

void loop() {
  // Hovedkode som kjøres gang etter gang: 
  modul.setDisplayToString(forNavn);
  delay(1000);
  modul.setDisplayToString(etterNavn);
  delay(1000);  
}
