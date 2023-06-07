from fields import Field
from gamefields import *
from random import randint
from players import *
from array import *
from abc import ABC, abstractmethod
from enum import Enum
from Configuration import Config


class System():
    """Клас який класифікує нерухомість для можливості покращення"""

    class Planet(Field):  # клас нерухомості
        def __init__(self, name_of_planet="earth", price_buy=13, price_pay=648, owner = 0, amount_of_branches=0,  branches="супутники", cost_of_branches=1993, rent_increase=30):
            super().__init__()
            self.__name_of_planet = name_of_planet
            self.__price_buy = price_buy # ціна покупки
            self.__price_pay = price_pay # ціна оренди (гравець на чужій клітині)
            self.__owner = owner
            self.__amount_of_branches = amount_of_branches # кількість філіалів
            self.__branches = branches  # філіали
            self.__cost_of_branches = cost_of_branches
            self.__rent_increase = rent_increase

        def print_planet(self):
            if self.__owner == 0:
              print(self.__name_of_planet, self.__price_buy, self.__price_pay, self.__amount_of_branches, "none owner" )
            else: 
              print(self.__name_of_planet, self.__price_buy, self.__price_pay, self.__amount_of_branches, self.__owner.get_name() )


        def set_owner(self, player):  # метод зміни власника нерухомості
            #print("Метод set_owner працює")
            self.__owner=player

        def upgrade(self):  # Покращення нерухомості
            #print("Метод upgrade працює")
            self.__owner.set_less_money(self.__cost_of_branches)
            self.__amount_of_branches+=1
            self.__price_pay+= self.__rent_increase

        def pay(self,player):  # метод оплати оренди
            #print("Метод pay працює")
            if player.get_money() < self.__price_pay:
                return "Player does not have enough money to buy"
            player.set_less_money(self.__price_pay)
            self.__owner.set_more_money(self.__price_pay)
            return "Player pay rent"

        def buy(self, player):  # метод покупки планети
            #print("Метод buy працює")
            if player.get_money() < self.__price_buy:
                return "Player does not have enough money to buy"
            player.set_less_money(self.__price_buy)
            player.own_planet(self)
            self.set_owner(player)
            return "Player buy planet"

        def event(self, player):
            #print("Викликався event планети")
            if (self.__owner):  # якщо у поля є власник
                if (self.__owner == player): # якщо власник поля - гравець, що став на поле
                    return "player is in his field"
                else:  # якщо власник хтось інший
                    return "player must pay"
            else:
                return "player can buy"  # якщо поле не має власник, повертається питання про купівлю нерухомості

    array_planets = []

    def __init__(self, name_of_sysytem="Sunny", amount_of_planet=10):
        super().__init__()
        self.__name_of_sysytem = name_of_sysytem
        self.__amount_of_planet = amount_of_planet
        for i in range(amount_of_planet):
            self.array_planets.append(i)

class WhatChoose(Enum) :
    earn = 1
    lost = 2
    prison = 3 
    start_finish = 4

class Strategy(ABC):

    @abstractmethod
    def choose_type_card(self, mood: WhatChoose) -> bool:
        print()
    
    @abstractmethod
    def choose_card(self, string, player, cache):
        pass
        print()

class EarnStrategy(Strategy):

   def choose_type_card(self, type: WhatChoose) -> bool:
     if WhatChoose.earn:
         return True
     return False

   def choose_card(self, string, player, cache):
    player.set_more_money(cache)
    print(string)

class LostStrategy(Strategy):

   def choose_type_card(self, choose_type: WhatChoose) -> bool:
     if WhatChoose.lost:
         return True
     return False


   def choose_card(self, string, player, cache):
     player.set_less_money(cache)
     print(string)

class PrisonStrategy(Strategy):

   def choose_type_card(self, choose_type: WhatChoose) -> bool:
     if WhatChoose.prison:
         return True
     return False

   def choose_card(self, string, player, cache):
     player.set_current_field(4)
     print(string)
    

class StartFinishStrategy(Strategy):
   def choose_type_card(self, choose_type: WhatChoose) -> bool:
     if WhatChoose.start_finish:
         return True
     return False

   def choose_card(self, string, player, cache):
     player.set_current_field(0)
     print(string)



class Chance:
   array_maps = []
   def __init__(self, strategy = LostStrategy, choose_type = WhatChoose,  string = "Player took card" , amount_of_maps=20, cache = 10):
      super().__init__()
      self.__strategy = strategy
      self.__choose_type = choose_type
      self.__string = string
      self.__amount_of_maps = amount_of_maps
      self.__cache = cache

   def set_choose_type(self, strategy: Strategy):
       self.__strategy = strategy

   def take_choose (self, string, player, cache):
       if self.__strategy.choose_type_card(self.__choose_type, self.__strategy):
          self.__strategy.choose_card(self, string, player, cache)

   def event(self, player):
        print("event")
        random_amount = randint(0, 3) # варіації шансу
        if random_amount==0:
            self.set_choose_type(EarnStrategy)
        elif random_amount==1:
            self.set_choose_type(LostStrategy)
        elif random_amount==2:
            self.set_choose_type(PrisonStrategy)
        else:
            self.set_choose_type(StartFinishStrategy)
        self.take_choose(self.__string, player, self.__cache)


#system1 = System()
#system2 = System()
#planet1 = system1.Planet()
#planet2 = system1.Planet()
#planet11 = system1.Planet()
#planet12 = system1.Planet()
#player1 = Player()
#player2 = Player()
#planet1.print_planet()
#planet1.event(player1)
#planet1.buy(player1)
#planet1.print_planet()
#planet12.buy(player2)
#planet12.pay(player1)
#planet12.print_planet()
#planet12.event(player1)

#chance = Chance()
#chance.event(player1)
