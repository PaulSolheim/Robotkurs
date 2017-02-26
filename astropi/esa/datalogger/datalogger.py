from sense_hat import SenseHat
from datetime import datetime

class DataLogger:
    def __init__(self):
        self.sense = SenseHat()
        self.filename = "./logs/Datalogg-"+str(datetime.now())+".csv"
        self.file_setup(self.filename)

    def write_line(self, line):
        with open(self.filename, "a") as f:
            f.write(line + "\n")
            
    def log_thrust(self):
        line = str(datetime.now()) + ", Thrust received!!!"
        self.write_line(line)

    def log_orientation(self, orientation):
        line = str(datetime.now()) + ", Orientation: ," + orientation
        self.write_line(line)

    def log_compass(self, compass):
        line = str(datetime.now()) + ", Compass: ," + str(compass)
        self.write_line(line)

    def file_setup(self, filename):
        header = ["datetime", "event", "value"]

        with open(filename, "w") as f:
            f.write(",".join(str(value) for value in header)+ "\n")

