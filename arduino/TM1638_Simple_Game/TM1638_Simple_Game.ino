// simple numerical memory game using TM1638 LED display and Arduino style board
// John Boxall CC by-sa-nc tronixstuff.com/projects | March 2012
#include <TM1638.h> // See http://code.google.com/p/tm1638-library/
// define a TM1638 module on data pin 8, clock pin 7 and strobe pin 6
TM1638 module(8, 9, 10);
byte buttons;
int level;
void setup()
{
 pinMode(11, OUTPUT); // for piezo buzzer
 randomSeed(analogRead(0)); // for random number generator
 preGame();
}
void preGame()
{
 // say Hello and get the level the user wants to play
 // the level is the number of milliseconds between displaying each number to remember
 module.setDisplayToString(" HELLO ", 1);
 for (int z=1; z<5; z++)
 {
 piezoBeep(z);
 }
 module.setDisplayToString(" LEVEL? ", 0);
 do // wait for user to select level
 {
 buttons=module.getButtons();
 }
 while (buttons==0);
 switch(buttons)
 {
 case 1:
 level=1000;
 break;
 case 2:
 level=900;
 break;
 case 4:
 level=800;
 break;
 case 8:
 level=700;
 break;
 case 16:
 level=600;
 break;
 case 32:
 level=500;
 break;
 case 64:
 level=400;
 break;
 case 128:
 level=300;
 break;
 }
 module.clearDisplay();
}
void piezoBeep(int type) // used to make beeps
{
 long duration=250000;
 int freq;
 switch(type)
 {
 case 1:
 freq = 600;
 break;
 case 2:
 freq = 700;
 break;
 case 3:
 freq = 800;
 break;
 case 4:
 freq = 900;
 break;
 case 5:
 freq = 1000;
 break;
 case 6:
 freq = 1100;
 break;
 case 7:
 freq = 1200;
 break;
 case 8:
 freq = 1300;
 break;
 }
 int period = (1.0 / freq) * 1000000;
 long elapsed_time = 0;
 while (elapsed_time < duration)
 {
 digitalWrite(11,HIGH);
 delayMicroseconds(period / 2);
 digitalWrite(11, LOW);
 delayMicroseconds(period / 2);
 elapsed_time += (period);
 }
}
void playGame()
{
 int gameNumbers[9]; // stores numbers to remember
 int userNumbers[9]; // stores users' presses
 int count=1; // tracks number of digits per round
 int z; // for various loops etc.
 boolean correct=true;
 delay(1000);
 
 do
 {
 for (int z=1; z<9; z++) // get random numbers for game
 {
 gameNumbers[z]=random(1,9);
 }
// display numbers to remember
 for (int i=1; i<=count; i++)
 {
 module.setDisplayDigit(gameNumbers[i],(i-1), false);
 piezoBeep(gameNumbers[i]);
 delay(level);
 module.clearDisplay();
 }
// get user attempts
for (z=1; z<=count; z++)
 {
 do // wait for user to press button
 {
 buttons=module.getButtons();
 }
 while (buttons==0);
 delay(300); // for debounce
 switch(buttons)
 {
 case 1:
 userNumbers[z]=1;
 break;
 case 2:
 userNumbers[z]=2;
 break;
 case 4:
 userNumbers[z]=3;
 break;
 case 8:
 userNumbers[z]=4;
 break;
 case 16:
 userNumbers[z]=5;
 break;
 case 32:
 userNumbers[z]=6;
 break;
 case 64:
 userNumbers[z]=7;
 break;
 case 128:
 userNumbers[z]=8;
 break;
 }
 module.setDisplayDigit(userNumbers[z],(z-1), false);
 delay(200);
 module.clearDisplay();
 }
// check for incorrect entries
 for (int z=1; z<=count; z++)
 {
 if (userNumbers[z]!=gameNumbers[z])
 {
 correct=false;
 }
 }
 count++;
 }
 while ((correct==true) && (count<9));
delay(1000);
 if (correct==true)
 {
 module.setDisplayToString("YOU WIN ", 0);
 }
 if (correct==false)
 {
 module.setDisplayToString("YOU LOSE", 0);
 }
 delay(1000);
 module.setDisplayToString("GO AGAIN", 0);
 delay(1000);
 module.clearDisplay();
}
void loop()
{
 playGame();
 delay(1000);
}
