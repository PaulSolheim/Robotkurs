from sense_hat import SenseHat
from datetime import datetime

class AstroLogger:
    def __init__(self):
        self.sense = SenseHat()
        self.filename = "Astrologg-"+str(datetime.now())+".csv"
        self.file_setup(self.filename)        

    def log_data(self, event, value, baseline, astronaut_status):
        sense_data = []
        sense_data.append(datetime.now())
        sense_data.append(event)
        sense_data.append(value)
        sense_data.append(baseline)
        sense_data.append(astronaut_status)
        
        line = ",".join(str(value) for value in sense_data)

        with open(self.filename, "a") as f:
            f.write(line + "\n")

    def file_setup(self, filename):
        header = ["datetime", "event", "value", "baseline", "astronaut"]

        with open(filename, "w") as f:
            f.write(",".join(str(value) for value in header)+ "\n")

