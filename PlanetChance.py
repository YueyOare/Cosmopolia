from fields import Field
from gamefields import *
from random import randint
from players import Player
from array import *


class System():
    """Клас який класифікує нерухомість для можливості покращення"""

    class Planet(Field):  # клас нерухомості
        def __init__(self, name_of_planet="earth", price_buy=134, price_pay=648, owner=0, amount_of_branches=0,  branches="Sput", cost_of_branches=1993, rent_increase = 30):
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
            print(self.__name_of_planet, self.__price_buy, self.__price_pay, self.__owner,  self.__amount_of_branches )

        def set_owner(self, player):  # метод зміни власника нерухомості
            print("Метод set_owner працює")
            self.__owner=player

        def upgrade(self):  # Покращення нерухомості
            print("Метод upgrade працює")
            self.__owner.set_less_money(self.__cost_of_branches)
            self.__amount_of_branches+=1
            self.__price_pay+= self.__rent_increase

        def pay(self,player):  # метод оплати оренди
            print("Метод pay працює")
            player.set_less_money(self.__price_pay)
            self.__owner.set_more_money(self.__price_pay)

        def buy(self, player):  # метод покупки планети
            print("Метод buy працює")
            player.set_less_money(self.__price_buy)
            player.own_planet(self)
            self.set_owner(player)

        def event(self, player):
            print("Викликався event планети")
            if (self.__owner):  # якщо у поля є власник
                if (self.__owner == player): # якщо власник поля - гравець, що став на поле
                    return "player is in his field"
                else:  # якщо власник хтось інший
                    self.pay(player)
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


class Chance(Field):
    """клас шанс на полі"""
    array_maps = []

    def __init__(self, amount_of_maps=20, cache = 10, string = "Player took card "):  # кількість карт шансу
        super().__init__()
        self.__amount_of_maps = amount_of_maps
        self.__cache = cache
        self.__string = string
        for i in range(amount_of_maps): # масив карт
            self.array_maps.append(i)

    def event(self, player):
        print("Викликався event шанса")
        random_amount = randint(0, 3) # варіації шансу
        if random_amount==0:
            print(self.__string + "end earn money")
            player.set_more_money(+ self.__cache)
        elif random_amount==1:
            print(self.__string + "and lost money")
            player.set_less_money(self.__cache)
        elif random_amount==2:
            print(self.__string + "and go to prison")
            return "go to prison"
        else:
            print(self.__string + "and go to start")
            return "go around to start"

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
#planet12.upgrade()
#planet12.print_planet()
#planet12.event(player1)

#chance = Chance()
#chance.event(player1)
