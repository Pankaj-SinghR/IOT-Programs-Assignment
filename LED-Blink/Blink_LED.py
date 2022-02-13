import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from time import sleep     # Import the sleep function from the time module

def startLEDBlink():
    GPIO.setwarnings(False)    # Ignore all the warning 
    GPIO.setmode(GPIO.BOARD)   # Using board pin numbers
    GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)   #Initial value of pin 8 is set to low and set as output pin\


    while True:
        GPIO.output(8, GPIO.HIGH) #Turn on
        sleep(1) #sleep for 1 sec
        GPIO.output(8, GPIO.LOW) #Turn off
        sleep(1) #sleep for 1 sec


if __name__=="__main__":
  startLEDBlink() #call the function to start blinking
