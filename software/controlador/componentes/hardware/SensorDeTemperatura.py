from abc import ABC, abstractstaticmethod

class SensorDeTemperatura(ABC):

    @abstractstaticmethod
    def temperatura(self) -> float:
        pass
