from PlanetChance import *
from gamefields import *
from threading import Lock
from array import *
from Configuration import Config


config = Config()
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
    array_Fields_in_map = []
    def __init__(self, number=16): # кількість клітинок на полі
        self.number = number
        counter_of_planet = 0
        system1 = System("Червона", 2) # створення мапи
        system2 = System("Синя", 3)
        system3 = System("Жовта", 2)  # створення мапи
        system4 = System("Зелена", 3)
        planet11 = system1.Planet("Планета11", 100, 25,  cost_of_branches=150, rent_increase=50)
        planet12 = system1.Planet("Планета12", 110, 30,  cost_of_branches=170, rent_increase=70)
        planet21 = system1.Planet("Планета21", 200, 55,  cost_of_branches=220, rent_increase=100)
        planet22 = system1.Planet("Планета22", 220, 60,  cost_of_branches=250, rent_increase=110)
        planet23 = system1.Planet("Планета23", 240, 75,  cost_of_branches=270, rent_increase=130)
        planet31 = system1.Planet("Планета31", 310, 100,  cost_of_branches=350, rent_increase=150)
        planet32 = system1.Planet("Планета32", 320, 105,  cost_of_branches=370, rent_increase=170)
        planet41 = system1.Planet("Планета41", 430, 150,  cost_of_branches=460, rent_increase=200)
        planet42 = system1.Planet("Планета42", 450, 155,  cost_of_branches=490, rent_increase=220)
        planet43 = system1.Planet("Планета43", 455, 165,  cost_of_branches=500, rent_increase=250)
        array_planets = [planet11, planet12, planet21, planet22, planet23, planet31, planet32, planet41, planet42, planet43]
        for i in range(config.fields_amount):
            if config.array_Fields[i] == "старт":
                self.array_Fields_in_map.append(StartFinish())
            elif config.array_Fields[i] == "планета":
                self.array_Fields_in_map.append(array_planets[counter_of_planet])
                counter_of_planet += 1
            elif config.array_Fields[i] == "тюрма":
                self.array_Fields_in_map.append(Prison())
            elif config.array_Fields[i] == "телепорт":
                self.array_Fields_in_map.append(Teleport())
            elif config.array_Fields[i] == "шанс":
                self.array_Fields_in_map.append(Chance())
            elif config.array_Fields[i] == "казіно":
                self.array_Fields_in_map.append(Casino())


# Map1 = Map()

#startfinish1 = StartFinish()
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

