#define buzzerPin 3
#define d 100
bool noteCompleted = false;
String note;

void setup() {
  pinMode(buzzerPin, OUTPUT);
  Serial.begin(115200);
  while(!Serial) {}
}

void loop() {
  if(noteCompleted) {
    playNote();  
    note = "";
    noteCompleted = false;
  }
}

void playNote() {
  int tmp = note.toInt();
  tone(buzzerPin, tmp);

  //int pauseBetweenNotes = d * 1.3f;
  //delay(pauseBetweenNotes);
}

void serialEvent() {
  char c = Serial.read();
  if(c == 'a') {
      noTone(buzzerPin);
      return;
  }
  if(c == '\n') {
    noteCompleted = true;
    return;
  }
  note += c;
}
