import RPi.GPIO as GPIO
import time
import asyncio

class Bomba():
    def __init__(self, gpio_pin_bcm: int, nome: str):
        """
        Broadcom GPIO numbers (BCM)        
        https://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs

        :param gpio_pin_bcm: recebe um inteiro que representa o pino no schema BCM
        :param nome: recebe uma string e atribui um nome a bomba

        """
        self.__gpio_pin_bcm = gpio_pin_bcm
        self.__nome = nome
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__gpio_pin_bcm, GPIO.OUT)
        GPIO.output(  self.__gpio_pin_bcm, GPIO.LOW)
    
    async def ligar(self,  pulsos=0):
        """
        Liga a bomba
        return: boolean
        """
        if pulsos > 0:
            for i in range(0,pulsos):
                GPIO.output(  self.__gpio_pin_bcm, GPIO.HIGH)
                await asyncio.sleep(500)
                GPIO.output(  self.__gpio_pin_bcm, GPIO.LOW)
        GPIO.output(  self.__gpio_pin_bcm, GPIO.HIGH)
                

        return GPIO.input(self.__gpio_pin_bcm)
    
    def desligar(self):
        """
        Desliga  a bomba
        retorna boolean
        """
        GPIO.output(  self.__gpio_pin_bcm, GPIO.LOW)
        return GPIO.input(self.__gpio_pin_bcm)
    
    def ligada(self):
        """
        Verifica se a bomba esta ligada 
        retorna boolean
        """
        return GPIO.input(self.__gpio_pin_bcm)
    


