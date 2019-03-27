import evdev
from Classes.Movement import *
m = Movement()
speed = int(input('Speed: ')) % 101
deadzone = 10
buttonMap = {'310':[m.turn,('l',0,speed)],'311':[m.turn,('r',0,speed)],'316':[exit,()]}

for i in buttonMap.values():
    i.append(False)

def buttonPressed(button):
    a = buttonMap[button]
    print(a)
    a[2] = not a[2]
    if a[2]:
        a[0](*a[1])
    elif not a[2]:
        m.stop()

def deadZones(conInput):
    a = conInput - 127
    if abs(a) < deadzone: return 0
    else: return a

def mapper(coord,scaler,dir1):
    l,r=100,100
    if coord>0:
        r= 100 - (100/128)*abs(coord)
    elif coord<0:
        l= 100 - (100/128)*abs(coord)
    l *= scaler
    r *= scaler
    return int(abs(l)),int(abs(r)),dir1,dir1
x = 0
R2 = 0
L2 = 0
devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)
number = input('Event No: ')
device = evdev.InputDevice('/dev/input/event'+number)
print(device)
pressed = False
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
        button = str(evdev.categorize(event)).split()[4]
        if button not in ['313','312']:
            buttonPressed(button)

    elif event.type == evdev.ecodes.EV_ABS:
        print('    ', event.code) #To check what L2 is

        if event.code == evdev.ecodes.ABS_X:
            x = deadZones(event.value)
        if event.code == 5:
            R2 = event.value
            if R2 > 0:
                if R2 < 20:
                    m.stop()
                else:
                    out = mapper(x,R2/255,0)
                    m.set(*out)
        if event.code == 0:
            L2  = event.value
            if L2 >  0:
                if L2 < 20:
                    m.stop()
                else:
                    out= mapper(x,L2/255,1)
                    m.set(*out)

