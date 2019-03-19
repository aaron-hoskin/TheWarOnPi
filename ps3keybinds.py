import evdev
from Classes.Movement import *
m = Movement()
speed = int(input('Speed: ')) % 101

buttonMap = {'312':[m.forward,(speed,0,1)],'310':[m.turn,('l',0,speed)],'313':[m.forward,(speed,0)],'311':[m.turn,('r',0,speed)],'316':[exit,()]}

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
    return (a//10)*10
    

x = 0
y = 0

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)

device = evdev.InputDevice('/dev/input/event3')
print(device)
pressed = False
for event in device.read_loop():
    if event.type == evdev.ecodes.EV_KEY:
        print(evdev.categorize(event))
        button = str(evdev.categorize(event)).split()[4]
        buttonPressed(button)
    elif event.type == evdev.ecodes.EV_ABS:
        if event.code == evdev.ecodes.ABS_X:
            x = deadZones(event.value)
        if event.code == evdev.ecodes.ABS_Y:
            y = deadZones(event.value)
        print(x,y)
