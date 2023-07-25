import SensorTemperatura
import Resistencia
import time
import asyncio
from threading import Thread

class ControladorTemperatura(Thread):
	def __init__(self, resistencia: Resistencia, sensor_de_temperatura: SensorTemperatura):
		self.__sensor_de_temperatura = sensor_de_temperatura
		self.__temperatura_alvo = 0
		self.__resistencia = resistencia

		Thread.__init__(self)

	def run(self):
		while True:
			try:
				time.sleep(1)
				self.__controle_temperatura()
				self.__log()
			except:
				pass
	
	def __controle_temperatura(self):
		pass

	def __log(self):
		pass