# import libraries
from sense_hat import SenseHat
from datetime import datetime, timedelta
from astrologger import AstroLogger
from random import randint, randrange
from time import sleep
import animation
import text

baseline = 0
astronaut_status = False

def baseline_humidity():
    baseline_missing = True

    while baseline_missing:
        # until baseline range is less than 1 percent
        base_values = get_baseline_values()
        base_range = find_range(base_values)
        baseline_mean = find_mean(base_values)
        if (base_range < 1) and (baseline_mean > 10):
            baseline_missing = False

    logger.log_data("baseline", baseline_mean, baseline, astronaut_status)
    
    return baseline_mean

def get_baseline_values():
    baseline_values = []
    for x in range(0, 5):
        humidity = sense.get_humidity()
        if humidity > 100:
            humidity = 100
        baseline_values.append(humidity)
        sleep(1)
    return baseline_values

def find_range(baseline_values):
    min_humidity = min(baseline_values)
    max_humidity = max(baseline_values)
    baseline_range = max_humidity - min_humidity
    return baseline_range

def find_mean(baseline_values):
    total = 0
    for x in baseline_values:
        total = total + x
    baseline_mean = total / len(baseline_values)
    return baseline_mean
    
def find_astronaut(baseline):
    astro_status = False
    humidity = sense.get_humidity()
    if humidity > 100:
        humidity = 100
    if (humidity - baseline) > 4:
        # Humidity increase by more than 4 percent
        astro_status = True
    if (baseline - humidity) > 4:
        # Humidity decrease by more than 4 percent
        astro_status = True
    
    logger.log_data("find_astronaut", astro_status, baseline, astronaut_status)

    return astro_status

# main program
sense = SenseHat()

# set correct rotation for astropi
sense.set_rotation(270)

# initialize text
text.init_text()

# initialize datalogger
logger = AstroLogger()

# read baseline humidity until less than 1% variation
baseline = baseline_humidity()
last_baseline = datetime.now()

# set timedelta between each new baseline
time_between = timedelta(minutes=10)

while True:
    # find astronaut
    astronaut_status = find_astronaut(baseline)
    
    # show an animation
    animation.show_animation()

    # show a trick question, facts or fun
    text.show_text()

    # do new baseline if more than 10 minutes since last
    if datetime.now() > (last_baseline + time_between):
        baseline = baseline_humidity()
        last_baseline = datetime.now()
