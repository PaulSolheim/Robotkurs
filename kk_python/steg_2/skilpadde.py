from turtle import *
from random import randrange, choice

def figur(sider, lengde, vinkel):
    begin_fill()
    pendown()
    for antall in range(sider):
        forward(lengde)
        right(vinkel)
    penup()
    end_fill()

farge_tabell = ["black", "blue", "brown", "chocolate", "coral", "cyan", "dark blue", "dark orange", "gold", "green", "lime green", "pink", "red", "tomato", "violet", "yellow"]
colormode(255)
#bgcolor(choice(farge_tabell))
bgcolor(randrange(0,255), randrange(0,255), randrange(0,255))
speed(9)
register_shape("gorilla.gif")
shape("gorilla.gif")
pensize(8)

sider = 3
total_lengde = 250
figurer = 20

penup()
setpos(0, 355)

for teller in range(figurer):

    pencolor(choice(farge_tabell))
    fillcolor(choice(farge_tabell))
    #pencolor(randrange(0,255), randrange(0,255), randrange(0,255))
    #fillcolor(randrange(0,255), randrange(0,255), randrange(0,255))
    
    vinkel = 360 / sider
    #vinkel = 144
    lengde = total_lengde / sider

    figur(sider, lengde, vinkel)

    setheading(0)
    right(360/figurer * teller)
    forward(total_lengde / figurer + 95)
    sider = sider + 1

home()

