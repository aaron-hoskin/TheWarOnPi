import RPi.GPIO as IO
from Classes.Ultrasound import *
from Classes.Movement import *
import time as t

speed = 100
sThreshold = int(input('Side Threshold: '))
fThreshold = int(input('Front Threshold: '))
m = Movement()
IO.setmode(IO.BCM)

Trigger = 17
l_Echo = 2
r_Echo = 3
f_Echo = 4

IO.setup(Trigger, IO.OUT)
IO.setup(l_Echo, IO.IN)
IO.setup(r_Echo, IO.IN)
IO.setup(f_Echo, IO.IN)

timetoturn90 = 2 # WILL NEED TO BE CHANGED ON DAY IF USED
a = 0
x=0
avef=0
aveb=0
avel=0
aver=0
n=0
while True:
  l,r,f = distance(Trigger,l_Echo),distance(Trigger,r_Echo),distance(Trigger,f_Echo)
  x+=1
  n+=1
  if n==10:
    avef=0
    aveb=0
    avel=0
    aver=0
    n=0
  if x==30:
      x=0
      print(f,l,r, a)
  if f > fThreshold :
    avef+=1
    if a!=1 and avef>8:
      m.forward(speed,0,0)
      a = 1
  elif r < sThreshold and l > sThreshold:
    avel+=1
    if a!=2 and avel>9:
      m.turn('l',0,speed)
      a=2
  elif r > sThreshold and l < sThreshold:
    aver+=1
    if a!=3 and aver>8:
      m.turn('r',0,speed)
      a=3
  elif r > l:
    aver+=1
    if a!=3 and aver>8:
      m.turn('r', 0, speed)
      a=3
  else:
    avel+=1
    if a!=2 and avel>8:
      m.turn('l',0,speed)
      a=2
