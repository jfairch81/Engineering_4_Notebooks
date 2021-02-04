import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) # sets warning to false
leds = [38] #  pin number
GPIO.setmode(GPIO.BOARD)
GPIO.setup(leds, GPIO.OUT) # output

for i in range(0, 3): # blinks
	GPIO.output(leds, 1)
	time.sleep(0.5)
	GPIO.output(leds, 0)
	time.sleep(0.5)
	print("hi")
