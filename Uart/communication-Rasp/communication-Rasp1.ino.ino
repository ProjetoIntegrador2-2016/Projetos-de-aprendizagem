int number = 0;

void setup(){
  Serial.begin(9600);
}

void loop(){
  
  if (Serial.available() > 0) {
    number = Serial.read();
    Serial.print("character recieved: ");
    Serial.println(number, DEC);
    //Serial.flush();
  }
}
