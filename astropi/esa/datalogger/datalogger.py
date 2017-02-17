from sense_hat import SenseHat
from datetime import datetime

class DataLogger:
    def __init__(self):
        self.buffer = 10
        self.sense = SenseHat()
        self.batch_data = []
        self.filename = "./logs/Datalogg-"+str(datetime.now())+".csv"
        self.file_setup(self.filename)        

    def log_data(self):
        sense_data = self.get_sense_data()
        
        output_string = ",".join(str(value) for value in sense_data)
        self.batch_data.append(output_string)

        if len(self.batch_data) >= self.buffer:
            print("Writing to file..")
            with open(self.filename, "a") as f:
                for line in self.batch_data:
                    f.write(line + "\n")
                self.batch_data = []

    def file_setup(self, filename):
        header = ["datetime", "temp_h", "temp_p", "humidity", "pressure", "pitch",
                  "roll", "yaw", "mag_x", "mag_y", "mag_z",
                  "accel_x", "accel_y", "accel_z",
                  "gyro_x", "gyro_y", "gyro_z"]

        with open(filename, "w") as f:
            f.write(",".join(str(value) for value in header)+ "\n")

    def get_sense_data(self):
        sense_data = []
        sense_data.append(datetime.now())
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

        return sense_data
