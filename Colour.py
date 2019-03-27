from Classes.Movement import *

m = Movement()
v = Vision()
area_limit = 1000
for i in range(4):
    done_colour = False
    while not done_colour:
        blocks = v.get_color(i)
        if len(blocks) == 0:
            m.turn('r')
        for block in blocks:
            x = block['x']
            y = block['y']
            a = block['area']
        if a <= area_limit:
            if abs(x-200) <= 30:
                m.forward(20)
            elif x > 200:
                m.turn('r')
            else:
                m.turn('l')
        elif a > area_limit:
            done_colour = True