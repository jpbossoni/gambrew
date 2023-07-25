from datetime import datetime, timedelta

class Rampa():
    def __init__(self, temperatua: float, tempo: int):
        self.__temperatura = temperatua
        self.__tempo = tempo
        self.__inicio_rampa #data hora
        self.__fim_rampa #data hora
        self.__rampa_iniciada = False
        
    def definir_rampa(self, temperatua: float, tempo: int) -> None:
        self.__temperatura = temperatua
        self.__tempo = tempo
    
    def iniciar_rampa(self):
        self.__rampa_iniciada = True
        self.__inicio_rampa =  datetime.datetime.now()
        self.__fim_rampa = self.__inicio_rampa + timedelta(minutes=self.__tempo)
    
    def finalizar_rampa(self):
        self.__rampa_iniciada = False
        self.__inicio_rampa = None
        self.__fim_rampa = None
        self.__tempo = None
        self.__temperatura = None
