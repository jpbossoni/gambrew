import RPi.GPIO as GPIO
import time
import asyncio


class Buzzer():
	def __init__(self, gpio_pin_bcm):
		"""
		Broadcom GPIO numbers (BCM)        
		https://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs

		:param gpio_pin_bcm: recebe um inteiro que representa o pino no schema BCM
		"""
		self.__gpio_pin_bcm = gpio_pin_bcm
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.__gpio_pin_bcm, GPIO.OUT)
		GPIO.output(  self.__gpio_pin_bcm, GPIO.LOW)
	
	async def pulsar(self, repeticao, duracao, intervalo):
		"""
		:param repeticao: um inteiro com a quantidade de vezes que o sinal sonoro será emitido
		:param duracao: um inteiro com a duração em milisegundos da do sinal sonoro
		:param intervalo: um inteiro com a duração em milisegundos do intervalo (pausa) entre os sinais sonoros
		"""
		for p in range(0,repeticao):
			print (p)
			GPIO.output(self.__gpio_pin_bcm, GPIO.HIGH)
			await asyncio.sleep(duracao)
			GPIO.output(self.__gpio_pin_bcm, GPIO.LOW)
			await asyncio.sleep(intervalo)
			
		GPIO.output(self.__gpio_pin_bcm, GPIO.LOW)

 