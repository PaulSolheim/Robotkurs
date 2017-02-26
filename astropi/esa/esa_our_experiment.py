# import libraries
from sense_hat import SenseHat
from datetime import datetime, timedelta
from datalogger import DataLogger
from senselogger import SenseLogger
from random import randint, randrange
from time import sleep
import animation
import text

sense = SenseHat()
sense.set_rotation(270)

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

    if (new_x - old_x) > 0.02:
        thrust = True
    elif (new_y - old_y) > 0.02:
        thrust = True
    elif (new_z - old_z) > 0.02:
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

# initialize text
text.init_text()

# initialize dataloggers
logger = DataLogger()
sense_logger = SenseLogger()

# set timedelta
time_between = timedelta(minutes=10)

# get initial orientations
base_orientation_yaw = find_orientation_by_yaw()
logger.log_orientation(base_orientation_yaw)
base_orientation_roll = find_orientation_by_roll()
logger.log_orientation(base_orientation_roll)

# get baseline for acceleration
base_acc = baseline_acceleration()
last_baseline = datetime.now()

while True:
    # Log data to Senselogg
    sense_logger.log_data()

    # show a random animation
    animation.show_animation()
    
    # find thrust
    thrust_status = find_thrust(base_acc)
    if thrust_status:
        logger.log_thrust()

    # find orientation using yaw
    orientation = find_orientation_by_yaw()
    if (orientation != base_orientation_yaw):
        logger.log_orientation(orientation)
        base_orientation_yaw = orientation

    # find orientation using roll
    orientation = find_orientation_by_roll()
    if (orientation != base_orientation_roll):
        logger.log_orientation(orientation)
        base_orientation_roll = orientation
        
    # find compass
    compass = find_compass()
    logger.log_compass(compass)

    # show a trick question, facts or fun
    text.show_text()

    # if more than 10 minutes since last acceleration baseline
    if datetime.now() > (last_baseline + time_between):
        # get baseline for acceleration
        base_acc = baseline_acceleration()
        last_baseline = datetime.now()
