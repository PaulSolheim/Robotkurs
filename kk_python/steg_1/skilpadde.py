from turtle import *

speed(1)
shape("turtle")
pencolor("red")
pensize(10)

for teller in range(10):

    pendown()
    for antall in range(5):
        forward(60)
        right(144)
    penup()

    right(360/10)
    forward(80)
    

