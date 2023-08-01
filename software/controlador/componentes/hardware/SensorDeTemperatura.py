from abc import ABC, abstractstaticmethod

class SensorDeTemperatura:

    @abstractstaticmethod
    def temperatura(self) -> float:
        pass
