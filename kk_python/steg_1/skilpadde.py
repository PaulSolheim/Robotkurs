from turtle import *
from random import randrange, choice

def stjerne(bredde):
    pendown()
    for antall in range(5):
        forward(60)
        right(144)
    penup()    

speed(6)
shape("turtle")
pencolor("violet")
pensize(10)

for teller in range(10):
    stjerne(60)
    right(360/10)
    forward(80)
    

