import RPi.GPIO as GPIO

class Resistencia():
	"""
	Broadcom GPIO numbers (BCM)        
	https://raspi.tv/2013/rpi-gpio-basics-4-setting-up-rpi-gpio-numbering-systems-and-inputs
	:param gpio_pin_bcm: recebe um inteiro que representa o pino no schema BCM
	:param potencia: recebe um inteiro que representa a potencia em watts da resistencia
	"""
	def __init__(self, gpio_pin_bcm: int, potencia: int, id: str, descricao: str):
		self.__gpio_pin_bcm = gpio_pin_bcm
		self.__pct_potencia = 0
		self.__potencia = potencia        
		self.__id = id
		self.__descricao = descricao
		self.__ligada = False

		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.__gpio_pin_bcm, GPIO.OUT)
		self.__pwm = GPIO.PWM(self.__gpio_pin_bcm, 100)
		self.__pwm.start(0)
		
		
	
			
	def ligar(self) -> bool:
		"""
		Liga a resistencia
		:return bool indica se a resistencia esta ligada ou desligada
		"""
		self.__ligada = True
		self.__pwm.ChangeDutyCycle(self.__pct_potencia)
		return self.__ligada
		
	
	def desligar(self) -> bool:
		"""
		Desliga a resistencia
		:return bool indica se a resistencia esta ligada ou desligada
		"""
		self.__ligada = False
		self.__pwm.ChangeDutyCycle(0)
		return self.__ligada

	@property
	def ligada(self) -> bool:
		"""
		:return bool indica se a resistencia esta ligada ou desligada
		"""
		return self.__ligada 

	
	@property
	def potencia(self) -> int:
		"""
		:return int retorna a potencia da resistencia
		"""
		return self.__potencia
	
	@property
	def pct_potencia(self) -> int:
		"""
		:return int retorna a pct_potencia
		"""
		return self.__pct_potencia
	
	#porcentagem da potência é um valor inteiro entre 0 e 100, valores fora dessa faixa serão convertidos para inteiro 0 ou 100 
	@pct_potencia.setter
	def pct_potencia(self,pct_potencia: int) -> int:
		"""
		altera o valor do pct_potencia e altera o ChangeDutyCycle passando esse valor
		"""
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

		return self.__pct_potencia
	

	def info(self)-> dict:
		"""
		Retorna um dicionario com as informações do buzzer
		gpio_pin_bcm
		potencia
		id
		descricao
		pct_potencia
		ligada
		"""
		dados ={
			"gpio_pin_bcm":self.__gpio_pin_bcm,
			"potencia":self.__potencia,
			"id":self.__id,
			"descricao":self.__descricao,
			"pct_potencia":self.__pct_potencia,
			"ligada":self.__ligada
		}
		return dados