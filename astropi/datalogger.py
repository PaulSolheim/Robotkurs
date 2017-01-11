##### Biblioteker ######
from sense_hat import SenseHat
from datetime import datetime

##### Innstillinger ######
FILNAVN = ""
BUFFER = 50

##### Funksjoner    ######
def log_data():
    output_streng = ",".join(str(value) for value in sense_data)
    batch_data.append(output_streng)

def file_setup():
    header = ["temp_h", "temp_p", "luftfuktighet", "lufttrykk", "pitch",
              "roll", "yaw", "mag_x", "mag_y", "mag_z",
              "accel_x", "accel_y", "accel_z",
              "gyro_x", "gyro_y", "gyro_z",
              "datetime"]

    with open(filnavn, "w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")

def get_sense_data():
    sense_data = []
    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())

    o = sense.get_orientation()
    yaw = o["yaw"]
    pitch = o["pitch"]
    roll = o["roll"]
    sense_data.extend([pitch, roll, yaw])

    mag = sense.get_compass_raw()
    x = mag["x"]
    y = mag["y"]
    z = mag["z"]
    sense_data.extend([x, y, z])    

    acc = sense.get_accelerometer_raw()
    x = acc["x"]
    y = acc["y"]
    z = acc["z"]
    sense_data.extend([x, y, z])  

    gyro = sense.get_gyroscope_raw()
    x = gyro["x"]
    y = gyro["y"]
    z = gyro["z"]
    sense_data.extend([x, y, z])

    sense_data.append(datetime.now())
    return sense_data
    
##### Hovedprogrammet ######
sense = SenseHat()

while True:
    sense_data = get_sense_data()
    print(sense_data)
    
