from datalogger import DataLogger
from time import sleep
import animasjoner
import tekster

logger = DataLogger()
tekster.init_tekst()
while True:
    logger.log_data()
    sleep(1)
    animasjoner.vis_animasjon()
    tekster.vis_tekst()
