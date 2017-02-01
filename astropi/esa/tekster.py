from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
tekst = []

def init_tekst():
    # Lure sporsmaal
    tekst.append("Thomas! Press Joystick to send message!")
    tekst.append("Urgent Call to all Astronauts!")
    tekst.append("Help!")
    # Fakta
    tekst.append("Fakta")
    # Morro
    tekst.append("Morro")

def vis_tekst():
    sense.set_rotation(270)
    maximum = len(tekst) - 1
    en_tekst = tekst[randint(0, maximum)]
    sense.show_message(en_tekst)
