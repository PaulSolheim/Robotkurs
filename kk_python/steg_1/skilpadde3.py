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
    pencolor(choice(farge_tabell))
    fillcolor(choice(farge_tabell))

speed(6)
shape("turtle")
pencolor("red")
pensize(10)
penup()
setpos(0, 240)
farge_tabell = ["black", "blue", "brown", "chocolate", "coral", "cyan", "dark blue", "dark orange", "gold", "green", "lime green", "pink", "red", "tomato", "violet", "yellow"]

for teller in range(10):
    velgfarge()
    stjerne(100)
    right(360/10)
    forward(120)

