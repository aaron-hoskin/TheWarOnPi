import RPi.GPIO as IO
from .Movement import *
from .Ultrasound import *
import time as t
from threading import Thread

IO.setmode(IO.BCM)
m = Movement()
sThresh = int(input('Side Threshold (in cm): '))
fThresh = int(input('Front Threshold (in cm): '))
tPin = 17
lPin = 2
rPin = 3
fPin = 4
for i in [lPin,rPin,fPin]:
    IO.setup(i,IO.IN)
IO.setup(tPin,IO.OUT)

class lThread(Thread):
    def run(self):
        return getU(lPin)
class rThread(Thread):
    def run(self):
        return getU(rPin)
class fThread(Thread):
    def run(self):
        self.result = getU(fPin)

def smartDistance():
    L = lThread
    R = rThread
    F = fThread
    trigger(tPin)
    L.start()
    R.start()
    F.start()
    L.join()
    R.join()
    F.join()
    return L.result, R.result, F.result

