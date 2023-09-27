int ledpin_1=13;
int blink_duration =100;
int ledpin_2 =12;
void setup() {
  // put your setup code here, to run once:

}

void loop() {
  pinMode(13, ledpin_1);
  digitalWrite(13,HIGH);
  delay(blink_duration);
  pinMode (13, ledpin_1);
  digitalWrite(13,LOW);
  delay(blink_duration);
  pinMode (12, ledpin_2);
  digitalWrite (12, ledpin_2);
  delay(blink_duration);
  pinMode (12,ledpin_2);
  digitalWrite(12,LOW);
  delay(blink_duration);

}