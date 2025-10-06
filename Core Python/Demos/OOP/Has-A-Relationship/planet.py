### HAs - A - Relationship
from abc import ABC, abstractmethod


class Planet(ABC):

    def __init__(self, galaxy, position):
        self.galaxy = galaxy
        self.position = position

    def revolveDays():
        pass


class Mars(Planet):
    def __init__(self, galaxy, position, radiation):
        super().__init__(galaxy, position)
        self.radiation = radiation

    def revolveDays(self):
        print("Mars revolve in : 687 Days")


class Earth(Planet):

    def __init__(self, galaxy, position, species):
        super().__init__(galaxy, position)
        self.species = species

    def revolveDays(self):
        print("Earth revolve in : 365 Days")


m1 = Mars("Milkey Way", 4, "High radiation")
e1 = Earth("Milkey way", 3, "Living Species")

list_planet = [m1, e1]

for obj in list_planet:
    obj.revolveDays()
