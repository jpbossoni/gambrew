from datetime import datetime
from threading import Thread
# https://pypi.org/project/w1thermsensor/
import time
from w1thermsensor import W1ThermSensor, Sensor 


class SensorDeTemperatura(Thread):
	"""
	https://github.com/timofurrer/w1thermsensor
	"""
	def __init__(self,  sensor_id, sensor_type="DS18B20",sensor_resolution=9):
		Thread.__init__(self)
		self.__temperatura = 0
		
		if sensor_type ==  "DS18S20":
			sensor_type = Sensor.DS18S20
		elif sensor_type == "DS1822":
			sensor_type = Sensor.DS1822
		elif sensor_type == "DS18B20":
			sensor_type = Sensor.DS18B20
		elif sensor_type == "DS28EA00":
			sensor_type = Sensor.DS28EA00
		elif sensor_type == "DS1825":
			sensor_type = Sensor.DS1825
		elif sensor_type == "MAX31850K":
			sensor_type = Sensor.MAX31850K

		self.__sensor = W1ThermSensor(sensor_type, sensor_id)
		self.__sensor.set_resolution(sensor_resolution)

	def run(self):
		while True:
			try:
				time.sleep(1)
				self.__temperatura = self.__sensor.get_temperature()
			except:
				print("ERRO AO LER O SENSOR DE TEMPERATURA: " + self.__sensor.id)

 
 
	def temperatura(self) -> float:
		return self.__temperatura
	