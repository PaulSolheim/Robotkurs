from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

def norge_animasjon():
    o = (255, 128, 0)
    e = (0, 0, 0)
    c = (0, 255, 255)
    b = (0, 0, 255)
    f = (255, 0, 255)
    y = (255, 255, 0)
    w = (255, 255, 255)
    g = (0, 255, 0)
    p = (102, 0, 204)
    r = (255, 0, 0)

    sense.set_rotation(270)
    frame1 = [r,r,w,w,w,w,r,r,r,r,r,w,w,w,r,r,r,r,r,r,w,w,r,r,r,r,r,r,r,w,r,r,r,r,w,r,r,r,r,r,r,r,w,w,r,r,r,r,r,r,w,w,w,r,r,r,r,r,w,w,w,w,r,r]
    frame2 = [w,w,b,b,b,b,w,w,w,b,b,w,w,b,b,w,b,b,w,w,w,w,b,b,b,b,w,w,w,w,b,b,b,b,w,w,w,w,b,b,b,b,w,w,w,w,b,b,w,b,b,w,w,b,b,w,w,w,b,b,b,b,w,w]
    frame3 = [r,r,r,r,r,r,r,w,r,r,w,w,w,w,r,r,r,r,w,w,w,w,r,r,r,r,w,w,w,r,r,w,r,r,r,r,r,r,w,w,r,r,w,w,w,r,r,w,r,r,w,w,w,w,r,r,r,r,w,w,w,w,r,r]
    frame4 = [w,w,b,b,b,b,w,w,w,b,b,w,w,b,b,w,b,b,w,w,w,w,b,b,b,w,w,w,w,w,w,w,b,w,w,w,w,w,w,w,b,b,w,w,w,b,b,b,w,b,b,w,w,w,b,b,w,w,b,b,b,b,w,b]
    frame5 = [r,r,r,r,r,r,r,w,r,r,r,r,r,r,r,w,r,r,w,w,w,w,w,w,r,r,r,r,r,r,w,w,r,r,r,r,r,r,w,w,r,r,w,w,w,w,w,w,r,r,r,r,r,r,r,w,r,r,r,r,r,r,r,w]
    frame6 = [r,r,w,b,w,r,r,r,r,r,w,b,w,r,r,r,r,r,w,b,w,r,r,r,w,w,w,b,w,w,w,w,b,b,b,b,b,b,b,b,w,w,w,b,w,w,w,w,r,r,w,b,w,r,r,r,r,r,w,b,w,r,r,r]

    ## Vis Norge animasjonen 5 ganger ##
    for t in range(5):
        sense.set_pixels(frame6)
        sleep(0.5)
        sense.set_pixels(frame1)
        sleep(0.5)
        sense.set_pixels(frame2)
        sleep(0.5)
        sense.set_pixels(frame3)
        sleep(0.5)
        sense.set_pixels(frame4)
        sleep(0.5)
        sense.set_pixels(frame5)
        sleep(0.5)
        sense.set_pixels(frame6)
        sleep(0.5)
    sense.clear()

def funkle():
    for t in range(2000):
        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        sense.set_pixel(x, y, r, g, b)
        sleep(0.01)

    sense.clear()

def smiley():
    o = (255, 128, 0)
    g = (0, 255, 0)
    p = (102, 0, 204)
    w = (255, 255, 255)
    y = (255, 255, 0)
    c = (0, 255, 255)
    r = (255, 0, 0)
    b = (0, 0, 255)
    f = (255, 0, 255)
    e = (0, 0, 0)

    sense.set_rotation(270)

    frame1 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,b,y,y,b,y,y,y,w,y,y,y,y,w,y,y,w,w,y,y,w,w,y,e,y,w,w,w,w,y,e,e,e,y,y,y,y,e,e]
    frame2 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,b,y,y,b,y,y,y,w,y,y,y,y,w,y,y,w,w,y,y,w,w,y,e,y,w,w,w,w,y,e,e,e,y,y,y,y,e,e]
    frame3 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,b,y,y,b,y,y,y,y,y,y,y,y,y,y,y,w,w,y,y,w,w,y,e,y,w,w,w,w,y,e,e,e,y,y,y,y,e,e]
    frame4 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,w,y,y,w,y,y,y,y,y,y,y,y,y,y,y,w,w,w,w,w,w,y,e,y,y,y,y,y,y,e,e,e,y,y,y,y,e,e]
    frame5 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,b,y,y,b,y,y,y,y,y,y,y,y,y,y,y,w,w,w,w,w,w,y,e,y,y,w,w,y,y,e,e,e,y,y,y,y,e,e]
    frame6 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,b,y,y,b,y,y,y,y,y,w,w,y,y,y,y,w,w,w,w,w,w,y,e,y,y,w,w,y,y,e,e,e,y,y,y,y,e,e]
    frame7 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,b,y,y,b,y,y,y,y,y,y,y,y,y,y,y,w,w,y,y,w,w,y,e,y,y,w,w,y,y,e,e,e,y,y,y,y,e,e]
    frame8 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,b,y,y,b,y,y,y,y,y,w,w,y,y,y,y,w,w,y,y,w,w,y,e,y,y,w,w,y,y,e,e,e,y,y,y,y,e,e]
    frame9 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,b,y,y,b,y,y,y,w,y,y,y,y,w,y,y,w,w,y,y,w,w,y,e,y,y,w,w,y,y,e,e,e,y,y,y,y,e,e]
    frame10 = [e,e,y,y,y,y,e,e,e,y,y,y,y,y,y,e,y,y,w,y,y,w,y,y,y,y,b,y,y,b,y,y,y,w,y,y,y,y,w,y,y,w,w,y,y,w,w,y,e,y,w,w,w,w,y,e,e,e,y,y,y,y,e,e]

    sense.set_pixels(frame1)
    sleep(1)
    sense.set_pixels(frame2)
    sleep(1)
    sense.set_pixels(frame3)
    sleep(1)
    sense.set_pixels(frame4)
    sleep(1)
    sense.set_pixels(frame5)
    sleep(1)
    sense.set_pixels(frame6)
    sleep(1)
    sense.set_pixels(frame7)
    sleep(1)
    sense.set_pixels(frame8)
    sleep(1)
    sense.set_pixels(frame9)
    sleep(1)
    sense.set_pixels(frame10)
    sleep(1)

    sense.clear()

def vis_animasjon():
    tilfeldig = randint(1, 3)
    if tilfeldig == 1:
        norge_animasjon()
    elif tilfeldig == 2:
        funkle()
    elif tilfeldig == 3:
        smiley()
        
