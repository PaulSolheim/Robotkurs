#include <TM1638.h>

TM1638 modul(8, 9, 10);
unsigned long teller;

void setup() {
  // Kode for oppsett som kjøres en gang:
  teller = 1;
}

void loop() {
  // Hovedkode som kjøres gang etter gang: 
  modul.setDisplayToDecNumber(teller, 0, false);
  delay(100);
  teller = teller + 1;
}
