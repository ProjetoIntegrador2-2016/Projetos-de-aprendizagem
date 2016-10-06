     import RPi.GPIO as GPIO
import time
import serial

# Inicia serial e a velocidade de transmissao
ser = serial.Serial("/dev/serial0", 115200)

GPIO.setmode(GPIO.BOARD)

#Botao como entrada
GPIO.setup(18, GPIO.IN)

print("Press the button")

while True:
    if GPIO.input(18) == True:
        ser.write("L")
        print("Enviado L")

        # Aguarda resposta
        answer = ser.readLine()

        # Mostra na tela a resposta enviada pelo arduino

        print answer

        # Aguarda 5 sec
        time.sleep(0.5)

