import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # sleep function
GPIO.setwarnings(False)    
GPIO.setmode(GPIO.BOARD)   
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   

while True: # Run forever
    GPIO.output(17, GPIO.HIGH) # On
    sleep(1)                  # Sleep
    GPIO.output(17, GPIO.LOW)  # Off
    sleep(1)                  
