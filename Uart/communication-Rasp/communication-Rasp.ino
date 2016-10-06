// Programa: Comunicacao Arduino com Raspberry Pi
// Autor: FILIPEFLOP
 
const int pino_led = 13;
char buf;
int estado = 1;
 
void setup()
{
  pinMode(pino_led, OUTPUT);
  Serial.begin(115200);
}
 
void loop()
{
  while (Serial.available() > 0)
  {
    buf = Serial.read();
    // Caso seja recebido o caracter L, acende o led
    if (buf == 'L')
    {
      // Liga ou desliga o led da porta 13
      digitalWrite(pino_led, estado);
      // Envia a resposta para o Raspberry
      Serial.print("Recebido! - Estado Led: ");
      if (estado == 1)
      {
        Serial.println("Ligado");
      }
      else
        Serial.println("Desligado");
    }
    // Inverte o estado do led
    estado = !estado;
  }
}
