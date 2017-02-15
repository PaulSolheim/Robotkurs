from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

def norway_animation():
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

    ## Show animation 3 times
    for t in range(3):
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

def sparkle():
    for t in range(1000):
        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 127)
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

def coders_selection_1():
    u = [0, 0, 255] # Blue
    y = [255, 255, 0] # Yellow
    b = [0, 0, 0] # Black

    image = [
        y, y, y, y, y, y, y, y,
        y, y, b, y, y, y, y, y, 
        y, y, b, y, y, y, y, y,
        y, y, b, y, y, y, y, y,
        y, y, b, y, y, y, y, y,
        y, y, b, y, y, y, y, y,
        y, y, b, b, b, b, y, y,
        y, y, y, y, y, y, y, y
        ]

    hat = [
        y, y, y, y, y, y, y, y,
        y, y, u, u, u, u, y, y, 
        y, y, u, u, u, u, y, y,
        y, y, u, u, u, u, y, y,
        y, y, u, u, u, u, y, y,
        y, y, u, u, u, u, y, y,
        u, u, u, u, u, u, u, u,
        y, y, y, y, y, y, y, y
        ]

    sense.set_pixels(image)
    sleep(1)
    sense.set_pixels(hat)
    sleep(1)

    o = (255,127,0)
    b = (0,0,255)
    s = (0,0,0)
    h = (255,255,255)

    image = [
        h, h, h, h, h, h, h, h,
        h, h, h, h, h, h, h, h,
        h, h, h, h, h, h, h, h,
        h, h, h, o, o, o, o, o,
        h, o, o, o, o, o, o, o,
        h, o, o, o, o, o, o, o,
        h, h, s, h, h, h, s, h,
        h, h, h, h, h, h, h, h
        ]

    bil = [
        h, h, h, h, s, s, s, s,
        h, s, s, h, s, s, s, s,
        h, s, s, h, s, s, s, s,
        h, s, s, h, s, s, s, s,
        h, h, h, h, s, s, s, s,
        s, s, s, s, s, s, s, s,
        h, h, h, h, h, h, h, h,
        s, s, s, s, s, s, s, s
        ]

    sense.set_pixels(image)
    sleep(1)
    sense.set_pixels(hat)
    sleep(1)

    w = (255, 255, 255)
    r = (255, 0, 0)

    image = [
        w, r, r, w, w, w, w, w,
        r, r, r, r, r, w, w, r,
        r, w, w, r, r, r, r, r,
        w, w, w, w, w, r, r, w,
        w, r, r, w, w, w, w, w,
        r, r, r, r, r, w, w, r,
        r, w, w, r, r, r, r, r,
        w, w, w, w, w, r, r, w
        ]

    image2 = [
        w, w, w, w, w, r, r, w,
        r, w, w, r, r, r, r, r,
        r, r, r, r, r, w, w, r,
        w, r, r, w, w, w, w, w,
        w, w, w, w, w, r, r, w,
        r, w, w, r, r, r, r, r,
        r, r, r, r, r, w, w, r,
        w, r, r, w, w, w, w, w
        ]

    sense.set_pixels(image)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)

def coders_selection_2():
    o = [255,127,0]
    w = [255,255,255]
    z = [25,25,25]
    g = [0,255,0]
    u = [0,0,255]

    fjell = [
        o,o,w,w,w,w,w,w,
        o,o,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,z,w,w,w,
        w,w,w,z,z,z,w,w,
        w,w,z,z,z,z,z,w,
        w,z,z,z,z,z,z,z
        ]

    tre = [
        w,w,w,w,w,w,w,w,
        w,w.w,g,w,w,w,w,
        w,w,g,g,g,w,w,w,
        w,g,g,g,g,g,w,w,
        g,g,g,g,g,g,g,w,
        w,w,w,z,z,w,w,w,
        w,w,w,z,z,w,w,w        
        ]

    sense.set_pixels(fjell)
    sleep(1)
    sense.set_pixels(tre)
    sleep(1)

    g = (0, 255, 0) # Green
    b = (50,50,50) # Black
    o = (255, 127, 0) # Orange
    w = (255,255,255) # White

    happy = [
        g,g,b,b,b,b,g,g,
        g,g,b,b,b,b,g,g,
        b,b,w,b,b,w,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,g,o,g,o,g,o,b,
        b,g,w,o,w,o,w,b,
        b,b,b,b,b,b,b,b
        ]

    sad = [
        g,g,b,b,b,b,g,g,
        g,g,b,b,b,b,g,g,
        b,b,w,b,b,w,b,b,
        b,b,b,b,b,b,b,b,
        b,b,b,b,b,b,b,b,
        b,g,b,b,b,b,g,b,
        b,b,g,g,g,g,b,b,
        b,b,b,b,b,b,b,b
        ]
    
    sense.set_pixels(happy)
    sleep(1)
    sense.set_pixels(sad)
    sleep(1)

    g=(0,255,0) # green
    r=(255,0,0) # red
    y=(255,255,0) # yellow

    image = [
        g, g, g, r, r, r, r, r, 
        g, g, g, r, r, r, r, r,
        g, g, g, r, r, r, r, r,
        g, g, g, y, r, r, r, r, 
        g, g, y, r, y, r, r, r, 
        g, g, g, y, r, r, r, r, 
        g, g, g, r, r, r, r, r, 
        g, g, g, r, r, r, r, r,
        ]
        
    sense.set_pixels(image)
    sleep(1)

def coders_selection_3():
    r = (255,0,0)
    y = (255,255,0)
    b = (0,0,0)
    w = (255,255,255)

    image = [
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        y, y, y, y, y, y, y, y,
        y, y, y, y, y, y, y, y,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r,
        r, r, r, r, r, r, r, r
        ]
    
    sense.set_pixels(image)
    sleep(1)

    g = (0, 255, 0) # Green
    b = (0, 0, 0) # Black
     
    image = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, b, b, g, g, b, b, g,
        g, b, b, g, g, b, b, g,
        g, g, g, b, b, g, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, g, g, b, g, g
        ]

    sense.set_pixels(image)
    sleep(1)

    l = (0, 0, 0) # Black
    g = (255, 255, 255) # White
    b = (255, 127, 0) # Orange
    e = (255, 0, 0) # Red
    o = (0, 0, 255) # BLue
     
    image = [
            e, e, e, e, e, e, e, e,
            g, g, g, g, g, g, g, g,
            g, o, o, b, b, o, o, g,
            g, o, o, b, b, o, o, g,
            g, b, b, b, b, b, b, g,
            g, b, b, b, b, b, b, g,
            g, g, g, g, g, g, g, g,
            g, g, g, g, g, g, g, g
            ]

    sense.set_pixels(image)
    sleep(1)

    r = (255, 0, 0,) # Red
    b = (0, 0, 255,) # Blue

    image1 = [
        b, b, b, b, b, b, b, b,
        b, r, r, b, b, r, r, b,
        b, r, r, b, b, r, r, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, r, r, r, r, r, r, b,
        b, b, r, b, b, r, b, b,
        b, b, b, r, r, b, b, b,
        ]

    image2 = [
        b, b, b, b, b, b, b, b,
        b, r, r, b, b, r, r, b,
        b, r, r, b, b, r, r, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, r, b, b, r, b, b,
        b, r, r, r, r, r, r, b,
        ]

    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)    

def show_animation():
    x = randint(1, 6)
    if x == 1:
        norway_animation()
    elif x == 2:
        sparkle()
    elif x == 3:
        smiley()
    elif x == 4:
        coders_selection_1()        
    elif x == 5:
        coders_selection_2()
    elif x == 6:
        coders_selection_3()
        
