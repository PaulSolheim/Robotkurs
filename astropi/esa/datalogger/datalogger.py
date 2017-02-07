##### Biblioteker ######
from sense_hat import SenseHat
from datetime import datetime

class DataLogger:
    def __init__(self):
        self.buffer = 10
        self.sense = SenseHat()
        self.batch_data = []
        self.filnavn = "Datalogg-"+str(datetime.now())+".csv"
        self.file_setup(self.filnavn)        

    def log_data(self, astronaut_status):
        sense_data = self.get_sense_data()
        
        # append astronaut_status
        sense_data.append(astronaut_status)
        
        output_streng = ",".join(str(value) for value in sense_data)
        self.batch_data.append(output_streng)

        if len(self.batch_data) >= self.buffer:
            print("Skriver til fil..")
            with open(self.filnavn, "a") as f:
                for linje in self.batch_data:
                    f.write(linje + "\n")
                self.batch_data = []

    def file_setup(self, filnavn):
        header = ["temp_h", "temp_p", "luftfuktighet", "lufttrykk", "pitch",
                  "roll", "yaw", "mag_x", "mag_y", "mag_z",
                  "accel_x", "accel_y", "accel_z",
                  "gyro_x", "gyro_y", "gyro_z",
                  "datetime", "astronaut"]

        with open(filnavn, "w") as f:
            f.write(",".join(str(value) for value in header)+ "\n")

    def get_sense_data(self):
        sense_data = []
        sense_data.append(self.sense.get_temperature_from_humidity())
        sense_data.append(self.sense.get_temperature_from_pressure())
        sense_data.append(self.sense.get_humidity())
        sense_data.append(self.sense.get_pressure())

        o = self.sense.get_orientation()
        yaw = o["yaw"]
        pitch = o["pitch"]
        roll = o["roll"]
        sense_data.extend([pitch, roll, yaw])

        mag = self.sense.get_compass_raw()
        x = mag["x"]
        y = mag["y"]
        z = mag["z"]
        sense_data.extend([x, y, z])    

        acc = self.sense.get_accelerometer_raw()
        x = acc["x"]
        y = acc["y"]
        z = acc["z"]
        sense_data.extend([x, y, z])  

        gyro = self.sense.get_gyroscope_raw()
        x = gyro["x"]
        y = gyro["y"]
        z = gyro["z"]
        sense_data.extend([x, y, z])

        sense_data.append(datetime.now())
        return sense_data
