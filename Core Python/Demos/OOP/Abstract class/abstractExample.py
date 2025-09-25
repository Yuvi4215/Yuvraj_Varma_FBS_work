### Abstact class example
from abc import ABC,abstractmethod

class Vehical(ABC):

    @abstractmethod # decorator
    def stop(self):
        pass

class Bike(Vehical):
    def start(self):
        print("Bike- Start method.")

    def stop(self):
        print("Bike-Stop method.")

b1=Bike()
b1.start()
b1.stop()