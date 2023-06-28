import RPi.GPIO as GPIO

class Resistencia():
    """
    Broadcom GPIO numbers (BCM)        
    https://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs
    :param gpio_pin_bcm: recebe um inteiro que representa o pino no schema BCM
    :param potencia: recebe um inteiro que representa a potencia em watts da resistencia
    """
    def __init__(self, gpio_pin_bcm, potencia):
        self.__gpio_pin_bcm = gpio_pin_bcm
        self.__pct_potencia = 0
        self.__potencia = potencia        
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.__gpio_pin_bcm, GPIO.OUT)
        self.__pwm = GPIO.PWM(self.__gpio_pin_bcm, 100)
        self.__pwm.start(0)
        self.__ligada = False
    
            
    def ligar(self):
        """
        Liga a resistencia

        :param  
        :param r 
        :param time: int

        :return float principal_amount * (1 + rate * time):
        """
        self.__ligada = True
        self.__pwm.ChangeDutyCycle(self.__pct_potencia)
    
    def desligar(self):
        """
        Liga a resistencia
        """
        self.__ligada = False
        self.__pwm.ChangeDutyCycle(0)

    @property
    def ligada(self):
        return self.__ligada 

    
    @property
    def potencia(self):
        return self.__potencia
    
    @property
    def pct_potencia(self):
        return self.__pct_potencia
    
    #porcentagem da potência é um valor inteiro entre 0 e 100, valores fora dessa faixa serão convertidos para inteiro 0 ou 100 
    @pct_potencia.setter
    def pct_potencia(self,pct_potencia : int):
        if pct_potencia >= 100 :
            pct_potencia = 100
        elif pct_potencia <= 0:
            pct_potencia = 0
        self.__pct_potencia = int(round(pct_potencia))

        #se estiver ligada, chama a funçao ligar ligar que vai alterar a potencia aplicada
        if self.ligada():
            self.ligar()
        else:
            self.desligar()