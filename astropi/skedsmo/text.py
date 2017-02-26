from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
text = []
sense.set_rotation(270)

def init_text():
    # Trick Questions / Commands
    text.append("Thomas! Press Joystick!")
    text.append("Urgent Call to all Astronauts!")
    text.append("Help! Ship ahoy!")
    text.append("Move closer!")
    text.append("Turn around!")
    text.append("Spaceship Voyager ahead!")
    text.append("Have you ever tried to eat goat cheese?")
    text.append("Look closer ;-)")
    text.append("Greetings to you - space explorer")
    text.append("Trick Question?")
    # Facts
    text.append("We are: Elias, Kevin, Oscar, Mattis, Toan, Leander")
    text.append("We are: Alexander, Adrian, Helene, Haakon, Lukas")
    text.append("We are: Magnus, Ethan, Kiran, Linnea, Jonas")
    text.append("Our teachers: Paul, Steinar, Sten Roger and Hans Petter")
    text.append("Skedsmo Kodeklubb @ 400 000 meters above the earth!")
    text.append("We code at Kjeller Skole in Skedsmo, Norway")
    text.append("Norway looks like a spoon on a map")
    text.append("Norway has mountains, glaciers and deep coastal fjords")
    text.append("Oslo is the capital of Norway")
    text.append("King of Norway wears a Krone")
    text.append("More Facts to follow")
    # Fun
    text.append("What is the meaning of life, the universe and everything?")
    text.append("Fun, funnier, funniest")
    text.append("Fun Family Fair")
    text.append("Pigs in Space!")
    text.append("More Pigs in Space!")
    text.append("More fun to come, watch this space")
    text.append("Why are we not funny?")

def show_text():
    maximum = len(text) - 1
    chosen_text = text[randint(0, maximum)]
    sense.show_message(chosen_text)
