import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


LED_PIN = 11
GPIO.setup(LED_PIN,GPIO.OUT)
INPUT_PIN = 13
GPIO.setup(INPUT_PIN,GPIO.IN)

while True:
   if GPIO.input(INPUT_PIN):
      GPIO.output(LED_PIN, True)
   else:
      GPIO.output(LED_PIN, False)

