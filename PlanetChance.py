from fields import Field
from random import randint
from players import Player
from array import *


class System():
    """Клас який класифікує нерухомість для можливості покращення"""

    class Planet(Field):  # клас нерухомості
        def __init__(self, name_of_planet="earth", price_buy=1345, price_pay=648, owner=0, amount_of_branches=5):
            super().__init__()
            self.__name_of_planet = name_of_planet
            self.__price_buy = price_buy # ціна покупки
            self.__price_pay = price_pay # ціна оренди (гравець на чужій клітині)
            self.__owner = owner
            self.__amount_of_branches = amount_of_branches # кількість філіалів

        def print_planet(self):
            print(self.__name_of_planet, self.__price_buy, self.__price_pay, self.__owner)

        def set_owner(self, player):  # метод зміни власника нерухомості
            print("Метод set_owner працює")
            self.__owner=player

        def upgrade(self, player, number_class):  # Покращення нерухомості
            print("Метод upgrade працює")
            player.set_less_money(self.__cost_of_branches)
            self.__branches+=1
            self.__price_pay+=10
            return 1

        def pay(self,player, owner):  # метод оплати оренди
            print("Метод pay працює")
            player.set_less_money(self.__price_pay)
            owner.set_more_money(self.__price_pay)
            return 1

        def buy(self, player):  # метод покупки планети
            print("Метод buy працює")
            player.set_less_money(self.__price_buy)
            self.set_owner(player)
            return 1

        def event(self, player):
            print("Викликався event планети")
            if (self.__owner):  # якщо у поля є власник
                if (self.__owner == player): # якщо власник поля - гравець, що став на поле
                    return 1
                else:  # якщо власник хтось інший
                    self.pay(player, self.__owner)
            else:
                return 2  # якщо поле не має власник, повертається питання про купівлю нерухомості

    array_planets = []

    def __init__(self, name_of_sysytem="Sunny", amount_of_planet=10, branches="Sput", cost_of_branches=1993):
        super().__init__()
        self.__name_of_sysytem = name_of_sysytem
        self.__amount_of_planet = amount_of_planet
        self.__branches = branches  # філіали
        self.__cost_of_branches = cost_of_branches
        for i in range(amount_of_planet):
            self.array_planets.append(i)


class Chance(Field):
    """клас шанс на полі"""
    array_maps = []

    def __init__(self, amount_of_maps=20):  # кількість карт шансу
        super().__init__()
        self.__amount_of_maps = amount_of_maps
        for i in range(amount_of_maps): # масив карт
            self.array_maps.append(i)

    def event(self, player):
        print("Викликався event шанса")
        random_amount = randint(0, 3) # варіації шансу
        if random_amount==0:
            player.set_more_money(+100)
        elif random_amount==1:
            player.set_less_money(-100)
        elif random_amount==2:
            return "go to prison"
        else:
            return "go around to start"
        return 1
