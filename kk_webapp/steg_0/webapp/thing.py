import RPi.GPIO as GPIO

LED_PIN    = 23
SWITCH_PIN = 24

class PiThing(object):
    """Raspberry Pi Internet 'Thing'"""

    def __init__(self):
        GPIO.setwarnings(False)
        

        
