from turtle import *
from random import randrange, choice

def stjerne(bredde):
    begin_fill()
    pendown()
    for antall in range(5):
        forward(bredde)
        right(144)
    penup()
    end_fill()

def velgfarge():
    farge = choice(farge_tabell)
    pencolor(farge)
    fillcolor(farge)

speed(6)
shape("turtle")
pencolor("red")
pensize(2)
penup()
setpos(0, 240)
farge_tabell = ["black", "blue", "brown", "chocolate", "coral", "cyan", "dark blue", "dark orange", "gold", "green", "lime green", "pink", "red", "tomato", "violet", "yellow"]

for teller in range(30):
    velgfarge()
    setpos(randrange(-320, 320), randrange(-280, 280))
    stjerne(randrange(20, 80))


