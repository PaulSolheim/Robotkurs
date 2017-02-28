from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.set_rotation(270)

def show_baseline():
    b = (0, 0, 200)
    r = (255, 0, 0)
    g = (0, 255, 0)

    image = [
        b, b, b, b, b, b, b, b,
        r, b, b, b, b, b, b, b,
        b, r, b, r, b, b, b, b,
        b, b, r, b, r, b, r, r,
        b, b, b, b, b, r, b, b,
        b, b, b, b, b, b, b, b,
        g, g, g, g, g, g, g, g,
        b, b, b, b, b, b, b, b
        ]

    sense.set_pixels(image)
    
def show_astronaut(astro_status):
    b = (0, 0, 200)
    r = (255, 0, 0)
    g = (0, 255, 0)

    if astro_status:
        image = [
            b, b, b, b, b, b, g, g,
            b, b, b, b, b, g, g, b,
            b, b, b, b, g, g, b, b,
            g, b, b, b, g, g, b, b,
            g, g, b, b, g, g, b, b,
            b, g, b, g, g, b, b, b,
            b, b, g, g, b, b, b, b,
            b, b, g, g, b, b, b, b
            ]
    else:
        image = [
            r, r, b, b, b, b, b, r,
            b, r, r, b, b, b, r, r,
            b, b, r, r, r, r, r, b,
            b, b, b, r, r, b, b, b,
            b, b, r, r, r, r, b, b,
            b, r, r, b, b, r, r, b,
            r, r, b, b, b, b, r, r,
            r, b, b, b, b, b, b, r
            ]

    sense.set_pixels(image)
    sleep(3)

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
    b = [75,75,75]

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
        w,w,w,w,w,w,w,w,
        w,w,w,g,w,w,w,w,
        w,w,g,g,g,w,w,w,
        w,g,g,g,g,g,w,w,
        g,g,g,g,g,g,g,w,
        w,w,w,b,b,w,w,w,
        w,w,w,b,b,w,w,w
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
        g, g, g, r, r, r, r, r
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
        b, b, b, r, r, b, b, b
        ]

    image2 = [
        b, b, b, b, b, b, b, b,
        b, r, r, b, b, r, r, b,
        b, r, r, b, b, r, r, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, b, b, r, r, b, b, b,
        b, b, r, b, b, r, b, b,
        b, r, r, r, r, r, r, b
        ]

    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)    

def coders_selection_4():
    b = (0, 0, 255) # Blue
    s = (0, 200, 0,) # Grenn
    g = (255, 255, 0) #Yellow
    h = (0, 0, 100) # LightBlue

    image1 =  [
        g, g, h, h, h, h, h, h,
        g, g, h, h, h, h, h, h,
        h, h, h, s, h, h, h, h,
        h, h, s, s, s, h, h, s,
        h, s, s, s, s, s, s, s,
        s, s, s, s, s, s, s, s,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b
        ]

    image2 =  [
        g, g, s, s, h, h, h, h,
        g, g, s, s, h, h, h, h,
        h, s, s, s, h, h, h, h,
        s, s, s, s, s, h, h, h,
        h, s, h, s, h, s, h, h,
        h, s, h, s, h, g, s, h,
        h, g, g, g, g, h, h, h,
        h, h, h, h, h, h, h, h
        ]
    
    sense.set_pixels(image1)
    sleep(1)
    sense.set_pixels(image2)
    sleep(1)

    g = (0, 255, 0) # Green
    b = (0, 0, 255) # Black
    o = (255, 127, 0) #orange
    v = (159, 0, 255) # purple
    w = (255, 255, 255) # white
    r = (255, 0, 0) # red
    y = (255, 255, 0) # yellow

    image = [
        o, o, o, o, o, o, o, o,
        o, g, g, g, g, g, g, o,
        g, g, b, b, g, b, b, g, 
        y, g, b, r, g, b, r, g,
        y, g, g, w, w, g, g, g,
        g, v, g, g, g, g, v, g,
        g, g, v, v, v, v, g, g,
        g, g, g, g, g, g, g, g,
        ]

    sense.set_pixels(image)
    sleep(1)

    r = (255, 0, 0)
    e = (0, 0, 0)
    c = (0, 255, 255)
    y = (255, 255, 0)
    p = (102, 0, 204)
    g = (0, 255, 0)
    o = (255, 128, 0)
    f = (255, 0, 255)
    b = (0, 0, 255)
    w = (255, 255, 255)

    frame1 = [e,e,e,r,r,e,e,e,e,e,r,o,o,r,e,e,e,r,o,r,r,o,r,e,r,o,r,o,o,r,o,r,r,o,r,o,o,r,o,r,e,r,o,r,r,o,r,e,e,e,r,o,o,r,e,e,e,e,e,r,r,e,e,e]

    sense.set_pixels(frame1)
    sleep(1)

    g = (0, 255, 0)
    y = (255, 255, 0)
    o = (255, 128, 0)
    c = (0, 255, 255)
    f = (255, 0, 255)
    w = (255, 255, 255)
    e = (0, 0, 0)
    b = (0, 0, 255)
    p = (102, 0, 204)
    farge1 = randint(0, 255)
    farge2 = randint(0, 255)
    farge3 = randint(0, 255)
    farge = (farge1, farge2, farge3)

    r = farge

    frame1 = [e,e,e,e,e,e,e,e,e,e,r,e,e,r,e,e,e,e,e,e,e,e,e,e,e,r,e,e,e,e,r,e,e,e,r,r,r,r,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

    sense.set_pixels(frame1)
    sleep(1)
    
    g = (0, 255, 0)
    r = (255, 0, 0)
    p = (102, 0, 204)
    y = (255, 255, 0)
    b = (0, 0, 255)
    o = (255, 128, 0)
    e = (0, 0, 0)
    c = (0, 255, 255)
    w = (255, 255, 255)
    f = (255, 0, 255)

    frame1 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,w,w,w,b,b,b,b,e,w,w,w,r,r,r,r,e,b,b,b,b,b,b,b,e,r,r,r,r,r,r,r,e,b,b,b,b,b,b,b,e,r,r,r,r,r,r,r,e]

    sense.set_pixels(frame1)
    sleep(1)
    
def show_pizza_animation():
    r = (255, 0, 0)
    b = (0, 0, 255)
    c = (0, 255, 255)
    p = (102, 0, 204)
    o = (255, 128, 0)
    y = (255, 255, 0)
    f = (255, 0, 255)
    w = (255, 255, 255)
    g = (0, 255, 0)
    e = (0, 0, 0)

    frame1 = [w,w,w,w,w,w,w,w,w,w,o,o,o,o,w,w,w,o,y,r,y,r,o,w,w,o,r,y,y,y,o,w,w,o,y,y,r,y,o,w,w,o,r,y,y,r,o,w,w,w,o,o,o,o,w,w,w,w,w,w,w,w,w,w]
    frame2 = [w,w,w,w,w,w,w,w,w,w,o,o,o,o,w,w,w,o,r,y,y,r,o,w,w,o,y,r,y,y,o,w,w,o,r,y,r,y,o,w,w,o,y,r,y,r,o,w,w,w,o,o,o,o,w,w,w,w,w,w,w,w,w,w]
    frame3 = [w,w,w,w,w,w,w,w,w,w,o,o,o,o,w,w,w,o,y,r,y,r,o,w,w,o,r,y,r,r,o,w,w,o,y,y,r,y,o,w,w,o,y,r,y,r,o,w,w,w,o,o,o,o,w,w,w,w,w,w,w,w,w,w]
    frame4 = [w,w,w,w,w,w,w,w,w,w,o,o,o,o,w,w,w,o,r,y,r,y,o,w,w,o,y,r,y,y,o,w,w,o,r,r,y,r,o,w,w,o,r,y,r,y,o,w,w,w,o,o,o,o,w,w,w,w,w,w,w,w,w,w]

    sense.set_pixels(frame1)
    sleep(1)
    sense.set_pixels(frame2)
    sleep(1)
    sense.set_pixels(frame3)
    sleep(1)
    sense.set_pixels(frame4)
    sleep(1)
    
def show_random_with_frame():
    sense.clear()
    inorder = 0
    i = 0
    XRed = 255
    RGorB = 0

    X = [XRed, 0, 0]  # Red
    O = [255, 255, 255]  # White

    outline = [
    X, X, X, X, X, X, X, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, X, X, X, X, X, X, X
    ]

    sense.set_pixels(outline)

    ## Show animation 30 times
    for t in range(30):
        x = randint(1, 6)
        y = randint(1, 6)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        sense.set_pixel(x, y, r, g, b)
        sleep(0.001)

        i += 1

        if i >= 200:
            i = 0

            if inorder == 0:
                XRed = randint(0, 255)
            else:
                XRed = 255

            RGorB = randint(0, 2)
            if inorder == 0:
                if RGorB == 0:
                    X = [XRed, 0, 0]

                    outline = [
                    X, X, X, X, X, X, X, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, X, X, X, X, X, X, X
                    ]

                    sense.set_pixels(outline)
                elif RGorB == 1:
                    X = [0, XRed, 0]

                    outline = [
                    X, X, X, X, X, X, X, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, X, X, X, X, X, X, X
                    ]

                    sense.set_pixels(outline)
                if RGorB == 2:
                    X = [0, 0, XRed]

                    outline = [
                    X, X, X, X, X, X, X, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, X, X, X, X, X, X, X
                    ]

                    sense.set_pixels(outline)
            else:
                if RGorB == 0:
                    X = [XRed, 0, 0]

                    outline = [
                        X, X, X, X, X, X, X, X,
                        X, O, O, O, O, O, O, X,
                        X, O, O, O, O, O, O, X,
                        X, O, O, O, O, O, O, X,
                        X, O, O, O, O, O, O, X,
                        X, O, O, O, O, O, O, X,
                        X, O, O, O, O, O, O, X,
                        X, X, X, X, X, X, X, X
                        ]
                    sense.set_pixels(outline)
                elif RGorB == 1:
                    X = [0, XRed, 0]

                    outline = [
                    X, X, X, X, X, X, X, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, X, X, X, X, X, X, X
                    ]

                    sense.set_pixels(outline)
                if RGorB == 2:
                    X = [0, 0, XRed]

                    outline = [
                    X, X, X, X, X, X, X, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, O, O, O, O, O, O, X,
                    X, X, X, X, X, X, X, X
                    ]

                    sense.set_pixels(outline)
                    
def show_flower_animation():
    e = (0, 0, 0)
    w = (255, 255, 255)
    f = (255, 0, 255)
    c = (0, 255, 255)
    p = (102, 0, 204)
    y = (255, 255, 0)
    b = (0, 0, 255)
    o = (255, 128, 0)
    g = (0, 255, 0)
    r = (255, 0, 0)

    frame1 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,o,o,e,e,e,e,e,e,o,o,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]
    frame2 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,o,e,e,o,e,e,e,e,e,o,o,e,e,e,e,e,e,o,o,e,e,e,e,e,o,e,e,o,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]
    frame3 = [e,e,e,e,e,e,e,e,e,o,e,e,e,e,o,e,e,e,o,e,e,o,e,e,e,e,e,o,o,e,e,e,e,e,e,o,o,e,e,e,e,e,o,e,e,o,e,e,e,o,e,e,e,e,o,e,e,e,e,e,e,e,e,e]
    frame4 = [e,e,e,e,e,e,e,e,e,o,e,e,e,e,o,e,e,e,o,y,y,o,e,e,e,e,y,o,o,y,e,e,e,e,y,o,o,y,e,e,e,e,o,y,y,o,e,e,e,o,e,e,e,e,o,e,e,e,e,e,e,e,e,e]
    frame5 = [o,e,e,e,e,e,e,o,e,o,e,e,e,e,o,e,e,e,o,y,y,o,e,e,e,e,y,o,o,y,e,e,e,e,y,o,o,y,e,e,e,e,o,y,y,o,e,e,e,o,e,e,e,e,o,e,o,e,e,e,e,e,e,o]
    frame6 = [o,e,e,e,e,e,e,o,e,o,e,e,e,e,o,e,e,e,o,o,o,o,e,e,e,e,o,o,o,o,e,e,e,e,o,o,o,o,e,e,e,e,o,o,o,o,e,e,e,o,e,e,e,e,o,e,o,e,e,e,e,e,e,o]
    frame7 = [o,e,e,e,e,e,e,o,e,o,e,e,e,e,o,e,e,e,o,o,o,o,e,e,e,e,o,r,r,o,e,e,e,e,o,r,r,o,e,e,e,e,o,o,o,o,e,e,e,o,e,e,e,e,o,e,o,e,e,e,e,e,e,o]
    frame8 = [o,e,e,e,e,e,e,o,e,o,y,y,y,y,o,e,e,y,o,o,o,o,y,e,e,y,o,r,r,o,y,e,e,y,o,r,r,o,y,e,e,y,o,o,o,o,y,e,e,o,y,y,y,y,o,e,o,e,e,e,e,e,e,o]
    frame9 = [o,e,e,e,e,e,e,o,e,o,y,y,y,y,o,e,e,y,r,o,o,r,y,e,e,y,o,r,r,o,y,e,e,y,o,r,r,o,y,e,e,y,r,o,o,r,y,e,e,o,y,y,y,y,o,e,o,e,e,e,e,e,e,o]
    frame10 = [o,e,e,e,e,e,e,o,e,o,y,y,y,y,o,e,e,y,r,r,r,r,y,e,e,y,r,r,r,r,y,e,e,y,r,r,r,r,y,e,e,y,r,r,r,r,y,e,e,o,y,y,y,y,o,e,o,e,e,e,e,e,e,o]
    frame11 = [o,e,e,e,e,e,e,o,e,o,y,y,y,y,o,e,e,y,r,r,r,r,y,e,e,y,r,p,p,r,y,e,e,y,r,p,p,r,y,e,e,y,r,r,r,r,y,e,e,o,y,y,y,y,o,e,o,e,e,e,e,e,e,o]
    frame12 = [o,e,e,e,e,e,e,o,e,o,o,o,o,o,o,e,e,o,r,r,r,r,o,e,e,o,r,p,p,r,o,e,e,o,r,p,p,r,o,e,e,o,r,r,r,r,o,e,e,o,o,o,o,o,o,e,o,e,e,e,e,e,e,o]
    frame13 = [o,y,y,y,y,y,y,o,y,o,o,o,o,o,o,y,y,o,r,r,r,r,o,y,y,o,r,p,p,r,o,y,y,o,r,p,p,r,o,y,y,o,r,r,r,r,o,y,y,o,o,o,o,o,o,y,o,y,y,y,y,y,y,o]
    frame14 = [o,y,y,y,y,y,y,o,y,p,o,o,o,o,p,y,y,o,p,r,r,p,o,y,y,o,r,p,p,r,o,y,y,o,r,p,p,r,o,y,y,o,p,r,r,p,o,y,y,p,o,o,o,o,p,y,o,y,y,y,y,y,y,o]
    frame15 = [o,y,y,y,y,y,y,o,y,p,o,o,o,o,p,y,y,o,p,f,f,p,o,y,y,o,f,p,p,f,o,y,y,o,f,p,p,f,o,y,y,o,p,f,f,p,o,y,y,p,o,o,o,o,p,y,o,y,y,y,y,y,y,o]
    frame16 = [o,y,y,y,y,y,y,o,y,p,f,f,f,f,p,y,y,f,p,w,w,p,f,y,y,f,w,p,p,w,f,y,y,f,w,p,p,w,f,y,y,f,p,w,w,p,f,y,y,p,o,o,o,o,p,y,o,y,y,y,y,y,y,o]
    frame17 = [o,e,e,e,e,e,e,o,e,p,f,f,f,f,p,e,e,f,p,w,w,p,f,e,e,f,w,p,p,w,f,e,e,f,w,p,p,w,f,e,e,f,p,w,w,p,f,e,e,p,f,f,f,f,p,e,o,e,e,e,e,e,e,o]
    frame18 = [o,e,e,f,f,e,e,o,e,p,f,f,f,f,p,e,e,f,p,w,w,p,f,e,f,f,w,p,p,w,f,f,f,f,w,p,p,w,f,f,e,f,p,w,w,p,f,e,e,p,f,f,f,f,p,e,o,e,e,f,f,e,e,o]
    frame19 = [o,y,y,f,f,y,y,o,y,p,f,f,f,f,p,y,y,f,p,w,w,p,f,y,f,f,w,p,p,w,f,f,f,f,w,p,p,w,f,f,y,f,p,w,w,p,f,y,y,p,f,f,f,f,p,y,o,y,y,f,f,y,y,o]
    frame20 = [o,y,y,f,f,y,y,o,y,p,f,f,f,f,p,y,y,f,p,w,w,p,f,y,f,f,w,r,r,w,f,f,f,f,w,r,r,w,f,f,y,f,p,w,w,p,f,y,y,p,f,f,f,f,p,y,o,y,y,f,f,y,y,o]
    frame21 = [o,y,y,f,f,y,y,o,y,p,f,f,f,f,p,y,y,f,p,r,r,p,f,y,f,f,r,r,r,r,f,f,f,f,r,r,r,r,f,f,y,f,p,r,r,p,f,y,y,p,f,f,f,f,p,y,o,y,y,f,f,y,y,o]
    frame22 = [o,y,y,f,f,y,y,o,y,p,f,f,f,f,p,y,y,f,p,r,r,p,f,y,f,f,r,g,g,r,f,f,f,f,r,g,g,r,f,f,y,f,p,r,r,p,f,y,y,p,f,f,f,f,p,y,o,y,y,f,f,y,y,o]
    frame23 = [g,y,y,f,f,y,y,g,y,g,f,f,f,f,g,y,y,f,g,r,r,g,f,y,f,f,r,g,g,r,f,f,f,f,r,g,g,r,f,f,y,f,g,r,r,g,f,y,y,g,f,f,f,f,g,y,g,y,y,f,f,y,y,g]
    frame24 = [g,y,y,f,f,y,y,g,y,g,f,f,f,f,g,y,y,f,g,r,r,g,f,y,f,f,r,c,c,r,f,f,f,f,r,c,c,r,f,f,y,f,g,r,r,g,f,y,y,g,f,f,f,f,g,y,g,y,y,f,f,y,y,g]
    frame25 = [c,y,y,f,f,y,y,c,y,c,f,f,f,f,c,y,y,f,c,r,r,c,f,y,f,f,r,c,c,r,f,f,f,f,r,c,c,r,f,f,y,f,c,r,r,c,f,y,y,c,f,f,f,f,c,y,c,y,y,f,f,y,y,c]
    frame26 = [c,y,y,f,f,y,y,c,y,c,f,f,f,f,c,y,y,f,c,r,r,c,f,y,f,f,r,e,e,r,f,f,f,f,r,e,e,r,f,f,y,f,c,r,r,c,f,y,y,c,f,f,f,f,c,y,c,y,y,f,f,y,y,c]
    frame27 = [c,y,y,f,f,y,y,c,y,c,f,f,f,f,c,y,y,f,e,r,r,e,f,y,f,f,r,e,e,r,f,f,f,f,r,e,e,r,f,f,y,f,e,r,r,e,f,y,y,c,f,f,f,f,c,y,c,y,y,f,f,y,y,c]
    frame28 = [c,y,y,f,f,y,y,c,y,e,f,f,f,f,e,y,y,f,e,r,r,e,f,y,f,f,r,e,e,r,f,f,f,f,r,e,e,r,f,f,y,f,e,r,r,e,f,y,y,e,f,f,f,f,e,y,c,y,y,f,f,y,y,c]
    frame29 = [e,y,y,f,f,y,y,e,y,e,f,f,f,f,e,y,y,f,e,r,r,e,f,y,f,f,r,e,e,r,f,f,f,f,r,e,e,r,f,f,y,f,e,r,r,e,f,y,y,e,f,f,f,f,e,y,e,y,y,f,f,y,y,e]
    frame30 = [e,e,e,f,f,e,e,e,e,e,f,f,f,f,e,e,e,f,e,r,r,e,f,e,f,f,r,e,e,r,f,f,f,f,r,e,e,r,f,f,e,f,e,r,r,e,f,e,e,e,f,f,f,f,e,e,e,e,e,f,f,e,e,e]
    frame31 = [e,e,e,f,f,e,e,e,e,e,f,f,f,f,e,e,e,f,e,e,e,e,f,e,f,f,e,e,e,e,f,f,f,f,e,e,e,e,f,f,e,f,e,e,e,e,f,e,e,e,f,f,f,f,e,e,e,e,e,f,f,e,e,e]
    frame32 = [e,e,e,f,f,e,e,e,e,e,f,e,e,f,e,e,e,f,e,e,e,e,f,e,f,e,e,e,e,e,e,f,f,e,e,e,e,e,e,f,e,f,e,e,e,e,f,e,e,e,f,e,e,f,e,e,e,e,e,f,f,e,e,e]
    frame33 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

    # Show each frame for 0.2 second
    sense.set_pixels(frame1)
    sleep(.2)
    sense.set_pixels(frame2)
    sleep(.2)
    sense.set_pixels(frame3)
    sleep(.2)
    sense.set_pixels(frame4)
    sleep(.2)
    sense.set_pixels(frame5)
    sleep(.2)
    sense.set_pixels(frame6)
    sleep(.2)
    sense.set_pixels(frame7)
    sleep(.2)
    sense.set_pixels(frame8)
    sleep(.2)
    sense.set_pixels(frame9)
    sleep(.2)
    sense.set_pixels(frame10)
    sleep(.2)
    sense.set_pixels(frame11)
    sleep(.2)
    sense.set_pixels(frame12)
    sleep(.2)
    sense.set_pixels(frame13)
    sleep(.2)
    sense.set_pixels(frame14)
    sleep(.2)
    sense.set_pixels(frame15)
    sleep(.2)
    sense.set_pixels(frame16)
    sleep(.2)
    sense.set_pixels(frame17)
    sleep(.2)
    sense.set_pixels(frame18)
    sleep(.2)
    sense.set_pixels(frame19)
    sleep(.2)
    sense.set_pixels(frame20)
    sleep(.2)
    sense.set_pixels(frame21)
    sleep(.2)
    sense.set_pixels(frame22)
    sleep(.2)
    sense.set_pixels(frame23)
    sleep(.2)
    sense.set_pixels(frame24)
    sleep(.2)
    sense.set_pixels(frame25)
    sleep(.2)
    sense.set_pixels(frame26)
    sleep(.2)
    sense.set_pixels(frame27)
    sleep(.2)
    sense.set_pixels(frame28)
    sleep(.2)
    sense.set_pixels(frame29)
    sleep(.2)
    sense.set_pixels(frame30)
    sleep(.2)
    sense.set_pixels(frame31)
    sleep(.2)
    sense.set_pixels(frame32)
    sleep(.2)
    sense.set_pixels(frame33)
    sleep(.2)

def show_circle_animation():
    c = (0, 255, 255)
    b = (0, 0, 255)
    y = (255, 255, 0)
    g = (0, 255, 0)
    o = (255, 128, 0)
    p = (102, 0, 204)
    r = (255, 0, 0)
    f = (255, 0, 255)
    w = (255, 255, 255)
    e = (0, 0, 0)

    frame1 = [e,e,e,o,o,e,e,e,e,e,o,e,e,o,e,e,e,o,e,e,e,e,o,e,o,e,e,e,e,e,e,o,o,e,e,e,e,e,e,o,e,o,e,e,e,e,o,e,e,e,o,e,e,o,e,e,e,e,e,o,o,e,e,e]
    frame2 = [y,e,e,o,o,e,e,y,e,y,o,e,e,o,y,e,e,o,e,e,e,e,o,e,o,e,e,e,e,e,e,o,o,e,e,e,e,e,e,o,e,o,e,e,e,e,o,e,e,y,o,e,e,o,y,e,y,e,e,o,o,e,e,y]
    frame3 = [y,r,r,o,o,r,r,y,r,y,o,e,e,o,y,r,r,o,e,e,e,e,o,r,o,e,e,e,e,e,e,o,o,e,e,e,e,e,e,o,r,o,e,e,e,e,o,r,r,y,o,e,e,o,y,r,y,r,r,o,o,r,r,y]
    frame4 = [r,r,r,o,o,r,r,r,r,r,o,e,e,o,r,r,r,o,e,e,e,e,o,r,o,e,e,e,e,e,e,o,o,e,e,e,e,e,e,o,r,o,e,e,e,e,o,r,r,r,o,e,e,o,r,r,r,r,r,o,o,r,r,r]
    frame5 = [r,r,r,o,o,r,r,r,r,r,o,b,b,o,r,r,r,o,b,e,e,b,o,r,o,b,e,e,e,e,b,o,o,b,e,e,e,e,b,o,r,o,b,e,e,b,o,r,r,r,o,b,b,o,r,r,r,r,r,o,o,r,r,r]
    frame6 = [r,r,r,o,o,r,r,r,r,r,o,b,b,o,r,r,r,o,b,p,p,b,o,r,o,b,p,e,e,p,b,o,o,b,p,e,e,p,b,o,r,o,b,p,p,b,o,r,r,r,o,b,b,o,r,r,r,r,r,o,o,r,r,r]
    frame7 = [r,r,r,o,o,r,r,r,r,r,o,b,b,o,r,r,r,o,b,p,p,b,o,r,o,b,p,f,f,p,b,o,o,b,p,f,f,p,b,o,r,o,b,p,p,b,o,r,r,r,o,b,b,o,r,r,r,r,r,o,o,r,r,r]
    frame8 = [r,r,r,e,e,r,r,r,r,r,e,b,b,e,r,r,r,e,b,p,p,b,e,r,e,b,p,f,f,p,b,e,e,b,p,f,f,p,b,e,r,e,b,p,p,b,e,r,r,r,e,b,b,e,r,r,r,r,r,e,e,r,r,r]
    frame9 = [o,o,o,e,e,o,o,o,o,o,e,b,b,e,o,o,o,e,b,p,p,b,e,o,e,b,p,f,f,p,b,e,e,b,p,f,f,p,b,e,o,e,b,p,p,b,e,o,o,o,e,b,b,e,o,o,o,o,o,e,e,o,o,o]
    frame10 = [o,o,o,b,b,o,o,o,o,o,b,b,b,b,o,o,o,b,b,p,p,b,b,o,b,b,p,f,f,p,b,b,b,b,p,f,f,p,b,b,o,b,b,p,p,b,b,o,o,o,b,b,b,b,o,o,o,o,o,b,b,o,o,o]
    frame11 = [o,o,o,b,b,o,o,o,o,o,b,b,b,b,o,o,o,b,b,e,e,b,b,o,b,b,e,f,f,e,b,b,b,b,e,f,f,e,b,b,o,b,b,e,e,b,b,o,o,o,b,b,b,b,o,o,o,o,o,b,b,o,o,o]
    frame12 = [o,o,o,b,b,o,o,o,o,o,b,p,p,b,o,o,o,b,p,e,e,p,b,o,b,p,e,f,f,e,p,b,b,p,e,f,f,e,p,b,o,b,p,e,e,p,b,o,o,o,b,p,p,b,o,o,o,o,o,b,b,o,o,o]
    frame13 = [o,o,o,b,b,o,o,o,o,o,b,p,p,b,o,o,o,b,p,f,f,p,b,o,b,p,f,y,y,f,p,b,b,p,f,y,y,f,p,b,o,b,p,f,f,p,b,o,o,o,b,p,p,b,o,o,o,o,o,b,b,o,o,o]
    frame14 = [o,o,o,e,e,o,o,o,o,o,e,p,p,e,o,o,o,e,p,f,f,p,e,o,e,p,f,y,y,f,p,e,e,p,f,y,y,f,p,e,o,e,p,f,f,p,e,o,o,o,e,p,p,e,o,o,o,o,o,e,e,o,o,o]
    frame15 = [b,b,b,e,e,b,b,b,b,b,e,p,p,e,b,b,b,e,p,f,f,p,e,b,e,p,f,y,y,f,p,e,e,p,f,y,y,f,p,e,b,e,p,f,f,p,e,b,b,b,e,p,p,e,b,b,b,b,b,e,e,b,b,b]
    frame16 = [b,b,b,p,p,b,b,b,b,b,p,p,p,p,b,b,b,p,p,f,f,p,p,b,p,p,f,y,y,f,p,p,p,p,f,y,y,f,p,p,b,p,p,f,f,p,p,b,b,b,p,p,p,p,b,b,b,b,b,p,p,b,b,b]
    frame17 = [b,b,b,p,p,b,b,b,b,b,p,f,f,p,b,b,b,p,f,f,f,f,p,b,p,f,f,y,y,f,f,p,p,f,f,y,y,f,f,p,b,p,f,f,f,f,p,b,b,b,p,f,f,p,b,b,b,b,b,p,p,b,b,b]
    frame18 = [y,y,y,p,p,y,y,y,y,y,p,f,f,p,y,y,y,p,f,f,f,f,p,y,p,f,f,w,w,f,f,p,p,f,f,w,w,f,f,p,y,p,f,f,f,f,p,y,y,y,p,f,f,p,y,y,y,y,y,p,p,y,y,y]
    frame19 = [y,y,y,p,p,y,y,y,y,y,p,f,f,p,y,y,y,p,f,f,f,f,p,y,p,f,f,r,r,f,f,p,p,f,f,r,r,f,f,p,y,p,f,f,f,f,p,y,y,y,p,f,f,p,y,y,y,y,y,p,p,y,y,y]
    frame20 = [y,y,y,r,r,y,y,y,y,y,r,f,f,r,y,y,y,r,f,f,f,f,r,y,r,f,f,r,r,f,f,r,r,f,f,r,r,f,f,r,y,r,f,f,f,f,r,y,y,y,r,f,f,r,y,y,y,y,y,r,r,y,y,y]
    frame21 = [y,y,y,r,r,y,y,y,y,y,r,f,f,r,y,y,y,r,f,f,f,f,r,y,r,f,f,e,e,f,f,r,r,f,f,e,e,f,f,r,y,r,f,f,f,f,r,y,y,y,r,f,f,r,y,y,y,y,y,r,r,y,y,y]
    frame22 = [y,y,y,r,r,y,y,y,y,y,r,f,f,r,y,y,y,r,f,e,e,f,r,y,r,f,e,e,e,e,f,r,r,f,e,e,e,e,f,r,y,r,f,e,e,f,r,y,y,y,r,f,f,r,y,y,y,y,y,r,r,y,y,y]
    frame23 = [y,y,y,r,r,y,y,y,y,y,r,e,e,r,y,y,y,r,e,e,e,e,r,y,r,e,e,e,e,e,e,r,r,e,e,e,e,e,e,r,y,r,e,e,e,e,r,y,y,y,r,e,e,r,y,y,y,y,y,r,r,y,y,y]
    frame24 = [y,y,y,e,e,y,y,y,y,y,e,e,e,e,y,y,y,e,e,e,e,e,e,y,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,y,e,e,e,e,e,e,y,y,y,e,e,e,e,y,y,y,y,y,e,e,y,y,y]
    frame25 = [y,e,e,e,e,e,e,y,e,y,e,e,e,e,y,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,y,e,e,e,e,y,e,y,e,e,e,e,e,e,y]
    frame26 = [e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e,e]

    ## Show each frame 0.2 seconds
    sense.set_pixels(frame1)
    sleep(.2)
    sense.set_pixels(frame2)
    sleep(.2)
    sense.set_pixels(frame3)
    sleep(.2)
    sense.set_pixels(frame4)
    sleep(.2)
    sense.set_pixels(frame5)
    sleep(.2)
    sense.set_pixels(frame6)
    sleep(.2)
    sense.set_pixels(frame7)
    sleep(.2)
    sense.set_pixels(frame8)
    sleep(.2)
    sense.set_pixels(frame9)
    sleep(.2)
    sense.set_pixels(frame10)
    sleep(.2)
    sense.set_pixels(frame11)
    sleep(.2)
    sense.set_pixels(frame12)
    sleep(.2)
    sense.set_pixels(frame13)
    sleep(.2)
    sense.set_pixels(frame14)
    sleep(.2)
    sense.set_pixels(frame15)
    sleep(.2)
    sense.set_pixels(frame16)
    sleep(.2)
    sense.set_pixels(frame17)
    sleep(.2)
    sense.set_pixels(frame18)
    sleep(.2)
    sense.set_pixels(frame19)
    sleep(.2)
    sense.set_pixels(frame20)
    sleep(.2)
    sense.set_pixels(frame21)
    sleep(.2)
    sense.set_pixels(frame22)
    sleep(.2)
    sense.set_pixels(frame23)
    sleep(.2)
    sense.set_pixels(frame24)
    sleep(.2)
    sense.set_pixels(frame25)
    sleep(.2)
    sense.set_pixels(frame26)
    sleep(.2)

def iceland_animation():
    FRAMES = [
    [[0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 0]],
    [[0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    ]
    for x in FRAMES:
             sense.set_pixels(x)
             time.sleep(0.25)
    time.sleep(2)

    FRAMES = [
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [0, 0, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0], [255, 128, 0]],
    ]
    for x in FRAMES:
             sense.set_pixels(x)
             time.sleep(0.25)
    time.sleep(2)

    sense.clear()

def greenland_animation():
    FRAMES = [
    [[255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [0, 0, 0]],
    [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0]],
    ]
    for x in FRAMES:
             sense.set_pixels(x)
             time.sleep(0.25)

    time.sleep(2)

    FRAMES = [
    [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 255], [0, 255, 255], [0, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 255], [0, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 255, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 255, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 255], [255, 255, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    ]
    for x in FRAMES:
             sense.set_pixels(x)
             time.sleep(0.3)

    sense.clear()

def canada_animation():
    FRAMES = [
    [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 0, 0], [255, 255, 255], [255, 255, 255], [255, 255, 255]],
    ]
    for x in FRAMES:
             sense.set_pixels(x)
             time.sleep(0.25)

    time.sleep(5)

    FRAMES = [
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 128, 0], [0, 0, 0], [0, 0, 0], [255, 255, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [0, 0, 0], [102, 0, 204], [0, 0, 0], [255, 255, 0], [0, 0, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [255, 255, 0], [0, 0, 0], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255], [0, 0, 255]],
    ]
    for x in FRAMES:
             sense.set_pixels(x)
             time.sleep(0.3)

    time.sleep(1)

    sense.clear()


def show_animation():
    x = randint(1, 14)
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
    elif x == 7:
        coders_selection_4()
    elif x == 8:
        show_flower_animation()        
    elif x == 9:
        show_circle_animation()
    elif x == 10:
        show_pizza_animation()
    elif x == 11:
        show_random_with_frame()
    elif x == 12:
        iceland_animation()
    elif x == 13:
        greenland_animation()
    elif x == 14:
        canada_animation()
