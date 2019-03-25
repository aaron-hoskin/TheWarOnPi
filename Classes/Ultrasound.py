#Libraries
import RPi.GPIO as GPIO
import time
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

def trigger(GPIO_TRIGGER):
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
def getU(GPIO_ECHO):
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
def distance(GPIO_TRIGGER,GPIO_ECHO):
    trigger(GPIO_TRIGGER)
    return getU(GPIO_ECHO)
if __name__ == '__main__':
 GPIO_TRIGGER = int(input('Trigger: '))
 GPIO_ECHO = int(input('Echo: '))
 try:
     while True:
         dist = distance(GPIO_TRIGGER,GPIO_ECHO)
         print ("Measured Distance = %.1f cm" % dist)

 except KeyboardInterrupt:
     print("Measurement stopped by User")
     GPIO.cleanup()
