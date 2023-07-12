import SensorTemperatura
import Resistencia
import time
import asyncio
from threading import Thread
from .SensorTemperatura import SensorTemperatura

class ControladorTemperatura(Thread):
	def __init__(self, resistencia :Resistencia, sensor_de_temperatura :SensorTemperatura):
		self.__sensor_de_temperatura = sensor_de_temperatura

		Thread.__init__(self)

	def run(self):
		while True:
			try:
				time.sleep(1)
				self.__sensor_de_temperatura.temperatura()
			except:
				