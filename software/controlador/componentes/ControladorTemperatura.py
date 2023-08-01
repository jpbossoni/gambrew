from hardware import SensorDeTemperatura
from hardware import Resistencia
import time
import asyncio
from threading import Thread
from typing import Type

class ControladorTemperatura(Thread):
	def __init__(self, resistencia Type[Resistencia], sensor_de_temperatura Type[SensorDeTemperatura]):
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