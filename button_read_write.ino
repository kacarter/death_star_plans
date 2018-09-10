// Adapted from https://www.instructables.com/id/Big-dome-push-button-LinkIt-basics-PART-1/

int button = 2;

void setup() {
  Serial.begin(9600);
  pinMode(button, INPUT);
}


void loop() {
  int buttonState = digitalRead(button);
  Serial.println(buttonState); // 1 is on (pushed), 0 is off
  delay(10);
}
