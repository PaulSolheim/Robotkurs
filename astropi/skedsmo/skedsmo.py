# import libraries
from sense_hat import SenseHat
from datetime import datetime, timedelta
from astrologger import AstroLogger
from datalogger import DataLogger
from senselogger import SenseLogger
from random import randint, randrange
from time import sleep
import animation
import text

###  Define Functions  ###

def baseline_humidity():
    baseline_missing = True

    # show baseline animation
    animation.show_baseline()

    while baseline_missing:
        # until baseline range is less than 1 percent
        base_values = get_baseline_values()
        base_range = find_range(base_values)
        baseline_mean = find_mean(base_values)
        if (base_range < 1) and (baseline_mean > 10):
            baseline_missing = False

    astrologger.log_data("baseline_humidity", baseline_mean, baseline, astronaut_status)
    return baseline_mean

def get_baseline_values():
    baseline_values = []
    for x in range(0, 5):
        humidity = sense.get_humidity()
        if humidity > 100:
            humidity = 100
        baseline_values.append(humidity)
        sleep(1)

    astrologger.log_data("get_baseline_values", baseline_values, baseline, astronaut_status)
    return baseline_values

def find_range(baseline_values):
    min_humidity = min(baseline_values)
    max_humidity = max(baseline_values)
    baseline_range = max_humidity - min_humidity

    astrologger.log_data("find_range", baseline_range, baseline, astronaut_status)
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
    if (humidity - baseline) > 3:
        # Humidity increase by more than 3 percent
        astro_status = True
    if (baseline - humidity) > 3:
        # Humidity decrease by more than 3 percent
        astro_status = True
    
    astrologger.log_data("find_astronaut", humidity, baseline, astro_status)

    print("Astronaut = " + str(astro_status))

    return astro_status

def baseline_acceleration():
    baseline_acc = sense.get_accelerometer_raw()
    return baseline_acc

def find_thrust(baseline):
    thrust = False
    
    old_x = baseline["x"]
    old_y = baseline["y"]
    old_z = baseline["z"]
    
    acc = sense.get_accelerometer_raw()
    new_x = acc["x"]
    new_y = acc["y"]
    new_z = acc["z"]

    # based on study of existing data from ISS
    # if acceleration in either direction changes
    # by more than 0.03, we log that a thrust has occured

    if (new_x - old_x) > 0.03:
        thrust = True
    elif (new_y - old_y) > 0.03:
        thrust = True
    elif (new_z - old_z) > 0.03:
        thrust = True

    return thrust

def find_orientation_by_yaw():
    o = sense.get_orientation()
    yaw = o["yaw"]
    yaw = round(yaw, 1)
    
    if yaw < 45:
        orientation = "Yaw: North-NorthEast"
    elif yaw < 90:
        orientation = "Yaw: NorthEast-East"
    elif yaw < 135:
        orientation = "Yaw: East-SouthEast"
    elif yaw < 180:
        orientation = "Yaw: SouthEast-South"
    elif yaw < 225:
        orientation = "Yaw: South-SouthWest"
    elif yaw < 270:
        orientation = "Yaw: SouthWest-West"
    elif yaw < 315:
        orientation = "Yaw: West-NorthWest"
    elif yaw < 360:
        orientation = "Yaw: NorthWest-North"
        
    return orientation

def find_orientation_by_roll():
    o = sense.get_orientation()
    roll = o["roll"]
    roll = round(roll, 1)
    
    if roll < 45:
        orientation = "Roll: North-NorthEast"
    elif roll < 90:
        orientation = "Roll: NorthEast-East"
    elif roll < 135:
        orientation = "Roll: East-SouthEast"
    elif roll < 180:
        orientation = "Roll: SouthEast-South"
    elif roll < 225:
        orientation = "Roll: South-SouthWest"
    elif roll < 270:
        orientation = "Roll: SouthWest-West"
    elif roll < 315:
        orientation = "Roll: West-NorthWest"
    elif roll < 360:
        orientation = "Roll: NorthWest-North"
        
    return orientation

def find_compass():
    north = sense.get_compass()
    north = round(north, 1)
    
    return north


###  Main Program  ###

# initialize variables
baseline = 0
astronaut_status = False
sense = SenseHat()
sense.set_rotation(270)

# initialize text
text.init_text()

# initialize loggers
astrologger = AstroLogger()
datalogger = DataLogger()
senselogger = SenseLogger()

# get initial orientations
base_orientation_yaw = find_orientation_by_yaw()
datalogger.log_orientation(base_orientation_yaw)
base_orientation_roll = find_orientation_by_roll()
datalogger.log_orientation(base_orientation_roll)

# get baseline for acceleration
base_acc = baseline_acceleration()

# read baseline humidity until less than 1% variation
baseline = baseline_humidity()
last_baseline = datetime.now()

# set timedelta between each new baseline
time_between = timedelta(minutes=10)

while True:
    # find astronaut and log findings to astrologg
    astronaut_status = find_astronaut(baseline)

    # show astronaut animation
    animation.show_astronaut(astronaut_status)

    # show a trick question, facts or fun
    text.show_text()
    
    # Log raw sensordata to senselogg
    senselogger.log_data()

    # find thrust, orientations, compass and log to datalogg

    # find thrust
    thrust_status = find_thrust(base_acc)
    if thrust_status:
        datalogger.log_thrust()

    # find orientation using yaw
    orientation = find_orientation_by_yaw()
    if (orientation != base_orientation_yaw):
        datalogger.log_orientation(orientation)
        base_orientation_yaw = orientation

    # find orientation using roll
    orientation = find_orientation_by_roll()
    if (orientation != base_orientation_roll):
        datalogger.log_orientation(orientation)
        base_orientation_roll = orientation
        
    # find compass
    compass = find_compass()
    datalogger.log_compass(compass)

    # show a random animation
    animation.show_animation()

    # do new baseline of humidity if more than 10 minutes since last
    if datetime.now() > (last_baseline + time_between):
        baseline = baseline_humidity()
        last_baseline = datetime.now()
