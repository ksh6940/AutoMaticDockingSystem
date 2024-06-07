#include <Servo.h>

const int servoPin = 9;
const int triggerPin = 8;
const int echoPin = 7;

Servo RotateMoter;

void setup() {
  Serial.begin(9600);

  pinMode(A0, INPUT); // Light sensor pin

  pinMode(servoPin, OUTPUT);
  RotateMoter.attach(servoPin);

  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  int lightValue = analogRead(A0);
  
  Serial.print("빛의 세기 : ");
  Serial.println(lightValue);

  FindLight(lightValue);
  
  delay(1000);

  FireEcho();
}

void FindLight(int lightValue){
  while(true){
   if (lightValue > 0) {
     RotateMoter.write(10);
   } else {
     RotateMoter.write(0);
     break
  }
 }
}

void FireEcho(){
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);

  float duration = pulseIn(echoPin, HIGH);
  float distance = (duration * 0.0343) / 2; /

  Serial.print(distance);
  Serial.println(" cm");

  delay(1000);
}

void CalculateAngle(){

  
}
