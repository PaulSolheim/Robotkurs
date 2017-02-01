##### Biblioteker ######
from sense_hat import SenseHat
from datetime import datetime
from datalogger import DataLogger
from random import randint, randrange
import animasjoner
import tekster

def baseline_humidity():

    return baseline_time

def find_astronaut():

    return astro_status

def do_experiment():



##### Hovedprogrammet ######
sense = SenseHat()

# Sett riktig rotasjon paa Text og Animasjoner
sense.set_rotation(270)

# Initier Tekster
tekster.init_tekst()

# Initier datalogger
logger = DataLogger()

# les luftfuktighet sensor til vi faar max 0.5% variasjon
last_baseline = baseline_humidity()

while True:
    # Finn Astronaut
    astronaut_found = find_astronaut()

    # Eget Eksperiment
    do_experiment()

    # Vis Animasjon
    animasjoner.vis_animasjon()

    # Vis Lure sporsmaal, Fakta og Morro
    tekster.vis_tekst()
    
    # Bruk datalogger til aa skrive logg
    logger.log_data()

    # Sjekk om vi maa gjore ny baseline for luftfuktighet
    if datetime.now() > (last_baseline + 10 minutes):
        last_baseline = baseline_humidity()
