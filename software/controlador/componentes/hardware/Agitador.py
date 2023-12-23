import RPi.GPIO as GPIO
import time
import asyncio


class Agitador():
	def __init__(self, gpio_pin_bcm: int, descricao: str, id: str) -> None:
		"""
		Broadcom GPIO numbers (BCM)        
		https://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs

		:param gpio_pin_bcm: recebe um inteiro que representa o pino no schema BCM
		:param descricao: recebe uma string e atribui um descricao ao agitador
		:param id: recebe uma string e atribui um id ao agitador
		

		"""
		self.__gpio_pin_bcm = gpio_pin_bcm
		self.__descricao = descricao
		self.__id = id
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.__gpio_pin_bcm, GPIO.OUT)
		GPIO.output(  self.__gpio_pin_bcm, GPIO.LOW)
	
	async def ligar(self,  pulsos:int =0) -> int:
		"""
		Liga o agitador
		return: int
		"""
		if pulsos > 0:
			for i in range(0,pulsos):
				GPIO.output(  self.__gpio_pin_bcm, GPIO.HIGH)
				await asyncio.sleep(500)
				GPIO.output(  self.__gpio_pin_bcm, GPIO.LOW)
		GPIO.output(  self.__gpio_pin_bcm, GPIO.HIGH)
		return GPIO.input(self.__gpio_pin_bcm)
	
	def desligar(self) -> int:
		"""
		Desliga  o agitador
		retorna int
		"""
		GPIO.output(  self.__gpio_pin_bcm, GPIO.LOW)
		return GPIO.input(self.__gpio_pin_bcm)
	
	def ligado(self) -> int:
		"""
		Verifica se o agitador esta ligadao
		retorna int
		"""
		return GPIO.input(self.__gpio_pin_bcm)
	
	def info(self) -> dict:
		"""
		Retorna um dicionario com as informações do agitador
			ligado
			gpio_pin_bcm
			descricao
			id
		"""
		dados =  {
			"ligado":self.ligado()
			,"gpio_pin_bcm": self.__gpio_pin_bcm
			,"descricao":self.__descricao
			,"id": self.__id
		}
		return dados


