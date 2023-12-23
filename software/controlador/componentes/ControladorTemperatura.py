from hardware.SensorDeTemperatura import SensorDeTemperatura
from hardware.Resistencia import Resistencia
from Rampa import Rampa

import time
import asyncio
from threading import Thread
from typing import Type

class ControladorTemperatura(Thread):
	def __init__(self, resistencia: Type[Resistencia], sensor_de_temperatura: type[SensorDeTemperatura]):
		self.__sensor_de_temperatura = sensor_de_temperatura
		self.__resistencia = resistencia
		self.__automatico = False
		self.__rampa: Type [Rampa]
		

		Thread.__init__(self)

	def run(self):
		while True:
			try:
				time.sleep(1)
				
				if self.__automatico:
					self.__controle_temperatura_automatico()
				else:
					self.__controle_temperatura_manual()
				
				self.__log()
			except:
				pass
	
	
	def __controle_temperatura_automatico(self):
		pass

	def __controle_temperatura_manual(self):
		if self.__sensor_de_temperatura.temperatura < 

	def __log(self):
		pass

	def definir_rampa(self, rampa: Type[Rampa]) -> None:
		self.__rampa = rampa