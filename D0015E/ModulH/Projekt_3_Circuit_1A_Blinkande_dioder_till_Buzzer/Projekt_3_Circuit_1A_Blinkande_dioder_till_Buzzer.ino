/*
  SparkFun Inventor’s Kit
  Circuit 2A - Buzzer

  Play notes using a buzzer connected to pin 10

  This sketch was written by SparkFun Electronics, with lots of help from the Arduino community.
  This code is completely free for any use.

  View circuit diagram and instructions at: https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-experiment-guide---v41
  Download drawings and code at: https://github.com/sparkfun/SIK-Guide-Code
*/

int speakerPin = 10;               //the pin that buzzer is connected to
int LED1 = 9;
int LED2 = 8;
int potPos;
void setup()
{
  Serial.begin(9600);
  pinMode(speakerPin, OUTPUT);    //set the output pin for the speaker
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
}

void loop()
{ 
  digitalWrite(LED1, HIGH);
  play('C', 2);       //old
  digitalWrite(LED1, LOW);
  
  digitalWrite(LED2, HIGH); 
  play('C', 2);       //mc
  digitalWrite(LED2, LOW);
  
  digitalWrite(LED1, HIGH);
  play('g', 2);       //do-
  digitalWrite(LED1, LOW);
  
  digitalWrite(LED2, HIGH);
  play('g', 2);       //nald
  digitalWrite(LED2, LOW);
  
  digitalWrite(LED1, HIGH);
  play('a', 2);       //had
  digitalWrite(LED1, LOW);
  
  digitalWrite(LED2, HIGH);
  play('a', 2);       //a
  digitalWrite(LED2, LOW);
  
  digitalWrite(LED1, HIGH);
  play('g', 4);       //farm
  digitalWrite(LED1, LOW);
  
  play(' ', 1);       //pause for 1 beat
  
  digitalWrite(LED1, HIGH);
  play('E', 2);       //ee
  digitalWrite(LED1, LOW);
 
  digitalWrite(LED2, HIGH);
  play('E', 2);       //ya
  digitalWrite(LED2, LOW);
  
  digitalWrite(LED1, HIGH);
  play('D', 2);       //EE
  digitalWrite(LED1, LOW);
 
  digitalWrite(LED2, HIGH);
   play('D', 2);       //ya
  digitalWrite(LED2, LOW);
  
  digitalWrite(LED1, HIGH);
  play('C', 6);       //yoo
  digitalWrite(LED1, LOW);
  while (true){}
}


void play( char note, int beats)
{
  int numNotes = 14;  // number of notes in our note and frequency array (there are 15 values, but arrays start at 0)

  //Note: these notes are C major (there are no sharps or flats)

  //this array is used to look up the notes
  char notes[] = { 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C', 'D', 'E', 'F', 'G', 'A', 'B', ' '};
  //this array matches frequencies with each letter (e.g. the 4th note is 'f', the 4th frequency is 175)
  int frequencies[] = {131, 147, 165, 175, 196, 220, 247, 262, 294, 330, 349, 392, 440, 494, 0};

  int currentFrequency = 0;    //the frequency that we find when we look up a frequency in the arrays
  int beatLength = 150;   //the length of one beat (changing this will speed up or slow down the tempo of the song)

  //look up the frequency that corresponds to the note
  for (int i = 0; i < numNotes; i++)  // check each value in notes from 0 to 14
  {
    if (notes[i] == note)             // does the letter passed to the play function match the letter in the array?
    {
      currentFrequency = frequencies[i];   // Yes! Set the current frequency to match that note
    }
  }

  //play the frequency that matched our letter for the number of beats passed to the play function
  tone(speakerPin, currentFrequency, beats * beatLength);
  delay(beats * beatLength);  //wait for the length of the tone so that it has time to play
  delay(50);                  //a little delay between the notes makes the song sound more natural

}

/* CHART OF FREQUENCIES FOR NOTES IN C MAJOR
  Note      Frequency (Hz)
  c        131
  d        147
  e        165
  f        175
  g        196
  a        220
  b        247
  C        262
  D        294
  E        330
  F        349
  G        392
  A        440
  B        494
*/
