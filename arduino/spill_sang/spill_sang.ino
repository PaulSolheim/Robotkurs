// Definer variabler for å spille en sang
const int buzzerPin = 8;
const int songLength = 18;
char notes[] = "cdfda ag cdfdg gf "; // mellomrom betyr en pause

// Beats er en tabell av varighet for hver note og hver pause.
// En "1" representerer en kvart-note, "2" en halv-note etc.
// Ikke glem at også pausene trenger en varighet.
int beats[] = {1, 1, 1, 1, 1, 1, 4, 4, 2, 1, 1, 1, 1, 1, 1, 4, 4, 2};

// tempo bestemmer hvor fort sangen skal spilles.
// For å spille sangen fortere må du velge en mindre verdi.
int tempo = 150;

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
      delay(duration);            // vent til noten er ferdigspillt
    }
    delay(tempo / 10);            // en kort pause mellom notene
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

void setup() {
  // put your setup code here, to run once:
  pinMode(buzzerPin, OUTPUT);

  // Hvis du vil spille sangen bare en gang:
  spillSang();
}

void loop() {
  // Hvis du vil spille sangen hele tiden:
  // spillSang();
  // delay(2000);    // en pause mellom hver gang
}
