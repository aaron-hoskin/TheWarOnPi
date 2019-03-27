#Libraries
import RPi.GPIO as GPIO
import time
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
def distance(GPIO_TRIGGER,GPIO_ECHO):
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
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
    s = (TimeElapsed * 34300) / 2
    return s
def trigger(GPIO_TRIGGER):
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

def getU(GPIO_ECHO):
    StartTime = time.time()
    StopTime = time.time()
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
    s = (TimeElapsed * 34300) / 2
    return s
if __name__ == '__main__':
 GPIO_TRIGGER = int(input('Trigger: '))
 GPIO_ECHO = int(input('Echo: '))
 GPIO.setup(GPIO_ECHO, GPIO.IN)
 GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
 try:
     while True:
         dist = distance(GPIO_TRIGGER,GPIO_ECHO)
         print ("Measured Distance = %.1f cm" % dist)
         time.sleep(0.1)

 except KeyboardInterrupt:
     print("Measurement stopped by User")
     GPIO.cleanup()
