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
    
    async def pulsar(self, repeticao, tempo):
        """
        :
        """
        for p in range(0,repeticao):
            print (p)
            GPIO.output(self.__gpio_pin_bcm, GPIO.HIGH)
            await asyncio.sleep(tempo)
            GPIO.output(self.__gpio_pin_bcm, GPIO.LOW)
            await asyncio.sleep(tempo)
            
        GPIO.output(self.__gpio_pin_bcm, GPIO.LOW)

 