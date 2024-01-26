import RPi.GPIO as GPIO
import time
import sys
import math
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

secsPerInt = 1
numSecsRun = 15
if '-alter' in sys.argv:
   secsPerInt = float(input('Enter the number of seconds the LED will Blink: '))
   numSecsRun = int(input('Enter the number of seconds the program will run: '))
iterCnt = math.trunc(numSecsRun/secsPerInt)

DEBUG = False 
if '-debug' in sys.argv:
   DEBUG = True

LED_PIN = 11
ledIsOn = False
GPIO.setup(LED_PIN,GPIO.OUT)
INPUT_PIN = 13
GPIO.setup(INPUT_PIN,GPIO.IN)

with open('data.txt','w') as data:
   for i in range(0,iterCnt):
      if GPIO.input(INPUT_PIN):
         ledIsOn = False
      GPIO.output(LED_PIN, ledIsOn)
      data.write(f'{time.time():1.0f}\t{ledIsOn}\n')
      if DEBUG:
         print(f'{time.time():1.0f}:\tLED is on: {ledIsOn}  \tInteration: {i+1}\n')
         ledIsOn = not(ledIsOn)
         time.sleep(secsPerInt)
GPIO.cleanup()
