from PlanetChance import *
from gamefields import *
from threading import Lock
from array import *


class Singleton(type):
  _instances = {}
  _lock: Lock = Lock()
  def __call__(cls, *args, **kwargs):
      with cls._lock:
          if cls not in cls._instances:
              instance = super().__call__(*args, **kwargs)
              cls._instances[cls] = instance
      return cls._instances[cls]

class Map(metaclass=Singleton):
    """Клас який містить саму мапа"""
    array_Fields = []

    def __init__(self, number=10): # кількість клітинок на полі
        self.number = number
        system1 = System() # створення мапи
        planet = system1.Planet()
        self.array_Fields.append(StartFinish())
        self.array_Fields.append(planet)
        self.array_Fields.append(planet)
        self.array_Fields.append(planet)
        self.array_Fields.append(Prison())
        self.array_Fields.append(Teleport())
        self.array_Fields.append(Chance())
        self.array_Fields.append(Casino())
        self.array_Fields.append(planet)
        self.array_Fields.append(planet)


   # startfinish1 = StartFinish()
    #startfinish1.event(player1)
# Map1 = Map()
# Field1 = Map1.Field("����", 2)
# System1 = System("Sun", 2, "sputniki", 8139838)
# System2 = System("Sirius", 4)
# Planet11 = System2.planet("Alfa", 22, 77, "Human1")
# Planet = System1.planet(12232, 123, "Human2")
# Planet1 = System1.planet("Mars", 2222, 111, "Bot")
# Planet11.print_planet()
# Planet1.event(2)
# casino1 = Casino()
# prison1 = Prison()
# teleport1 = Teleport()
# prison1.event(player1)
# prison1.event(player1)
# casino1.event(player1)
# teleport1.event(player1)
