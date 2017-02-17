# import libraries
from sense_hat import SenseHat
from datetime import datetime, timedelta
from datalogger import DataLogger
from random import randint, randrange
from time import sleep
import animation
import text

sense = SenseHat()
sense.set_rotation(270)

def do_experiment():

    return status

def do_something():
    last_something = datetime.now()

    return last_something
    
# initialize text
text.init_text()

# initialize datalogger
logger = DataLogger()

# set timedelta
time_between = timedelta(minutes=10)

# do something
last_something = do_something()

while True:
    # do experiment
    experiment_status = do_experiment()

    # Log data
    logger.log_data()
    
    # show experiment animation
    animation.show_experiment(experiment_status)

    # show a trick question, facts or fun
    text.show_text()

    # show a random animation
    animation.show_animation()

    # if more than 10 minutes since last something
    if datetime.now() > (last_something + time_between):
        # do something
        last_something = do_something()
