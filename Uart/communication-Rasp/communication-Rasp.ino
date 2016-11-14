// Clockwise and counter-clockwise definitions.
// Depending on how you wired your motors, you may need to swap.
#define CW  1
#define CCW 0

// Motor definitions to make life easier:
#define MOTOR_A 0
#define MOTOR_B 1

#define STOP 's'
#define FOWARD 'f'
#define BACKWARD 'b'
#define LEFT 'l'
#define RIGHT 'r'
#define TURN_LEFT 'e'
#define TURN_RIGHT 'd'

const byte PWMA = 3;  // PWM control (speed) for motor A
const byte PWMB = 11; // PWM control (speed) for motor B
const byte DIRA = 12; // Direction control for motor A
const byte DIRB = 13; // Direction control for motor B

char incoming = 'n';
int last_cw = CW;

void setup()
{
  Serial.begin(19200);
  setupArdumoto();
}

void loop()
{
  
  if (Serial.available()){
    
    incoming = Serial.read();
    switch(incoming){
      case FOWARD:
        driveArdumoto(MOTOR_A, CW, 100);
        driveArdumoto(MOTOR_B, CW, 100);
        last_cw = CW;  
      break;
      case BACKWARD:
        driveArdumoto(MOTOR_A, CCW, 100);
        driveArdumoto(MOTOR_B, CCW, 100);
        last_cw = CCW;
      break;
      case LEFT:
        if (last_cw == CW) {
            analogWrite(PWMA, 50);
            analogWrite(PWMB, 200);
          } else {
            analogWrite(PWMA, 200);
            analogWrite(PWMB, 50);
          }
      break;
      case RIGHT:
        if (last_cw == CW) {
            analogWrite(PWMA, 50);
            analogWrite(PWMB, 200);
          } else {
            analogWrite(PWMA, 200);
            analogWrite(PWMB, 50);
          }
      break;
      case TURN_RIGHT:
         stopArdumoto(MOTOR_A);
         stopArdumoto(MOTOR_B);
         driveArdumoto(MOTOR_A, CCW, 200);
      break;
      case TURN_LEFT:
         stopArdumoto(MOTOR_A);
         stopArdumoto(MOTOR_B);
         driveArdumoto(MOTOR_B, CCW, 200);
      default:
        stopArdumoto(MOTOR_A);
        stopArdumoto(MOTOR_B);
    }
    delay(1);
    
  }
}

// driveArdumoto drives 'motor' in 'dir' direction at 'spd' speed
void driveArdumoto(byte motor, byte dir, byte spd)
{
  if (motor == MOTOR_A)
  {
    digitalWrite(DIRA, dir);
    analogWrite(PWMA, spd);
  }
  else if (motor == MOTOR_B)
  {
    digitalWrite(DIRB, dir);
    analogWrite(PWMB, spd);
  }  
}

// stopArdumoto makes a motor stop
void stopArdumoto(byte motor)
{
  driveArdumoto(motor, 0, 0);
}

// setupArdumoto initialize all pins
void setupArdumoto()
{
  // All pins should be setup as outputs:
  pinMode(PWMA, OUTPUT);
  pinMode(PWMB, OUTPUT);
  pinMode(DIRA, OUTPUT);
  pinMode(DIRB, OUTPUT);

  // Initialize all pins as low:
  digitalWrite(PWMA, LOW);
  digitalWrite(PWMB, LOW);
  digitalWrite(DIRA, LOW);
  digitalWrite(DIRB, LOW);
}
