import serial
import time
ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
#ser.open() # serial is already open

# Variable dir will be set according to the 
# direction that the prototype needs to go
# based on the target action

dirR = 'r' #right -> ascii character
dirL = 'l' #left
foward = 'f' 
back = 'b'

try:
 while 1:
  dir = input("Insert the motors orientation: ")  

  ser.write(dir)
  time.sleep(1)
  response = ser.readline()	
  print response

except KeyboardInterrupt:
 ser.close()
