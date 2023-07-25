from threading import Thread
from Rampa import Rampa
from ControladorTemperatura import ControladorTemperatura

class Panela(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.__rampa
        self.__controlador_temperatura = ControladorTemperatura(resistencia=1, sensor_de_temperatura=sensor)
    
    def definir_rampa(self, temperatura: float, tempo: int):
        self._rampa = Rampa(temperatura, tempo)
        self.__controlador_temperatura.