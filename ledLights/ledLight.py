#import libraries
import RPi.GPIO as GPIO
import time

#setup output from pi/breadboard
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)

#led flashing loop
for x in range(0,10):
    GPIO.output(7,True)
    GPIO.output(11,False)
    time.sleep(.3)
    GPIO.output(7,False)
    GPIO.output(11,True)
    time.sleep(.7)
    
#finish and clean up
GPIO.cleanup()