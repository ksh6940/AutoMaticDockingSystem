#include <Servo.h>

Servo servo;

const int triggerPin = 9; 
const int echoPin = 8;

void setup() {
  Serial.begin(9600); 

  servo.attach(7);
  servo.write(0);

  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  float duration = pulseIn(echoPin, HIGH);
  float distance = (duration * 0.0343) / 2;

  Serial.print("도킹까지 남은 거리 : "); // Added semicolon here
  Serial.print(distance);
  Serial.println(" cm");

  delay(100);

  if (distance < 5){
    servo.write(360);
  } else {
    servo.write(0);
  }
}
