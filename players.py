from __future__ import annotations
from Configuration import Config
from random import randint
from abc import ABC, abstractmethod
from typing import List

players_counter = 0


class Creator(ABC):
    """
    The Creator class declares the factory method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def factory_method(self, id=0, name="", money=100, current_field=0, enabled=1, skipped_in_a_row=0,
                       own_planets={}):
        pass

    def create_product(self, id=0, name="", money=100, current_field=0, enabled=1, skipped_in_a_row=0,
                       own_planets={}):
        return self.factory_method(id, name, money, current_field, enabled, skipped_in_a_row,
                                   own_planets)


class HumanCreator(Creator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """

    def factory_method(self, id=0, name="", money=100, current_field=0, enabled=1, skipped_in_a_row=0,
                       own_planets={}) -> Product:
        return HumanProduct(id, name, money, current_field, enabled, skipped_in_a_row,
                            own_planets)


class BotCreator(Creator):
    def factory_method(self, id=0, name="", money=100, current_field=0, enabled=1, skipped_in_a_row=0,
                       own_planets={}) -> Product:
        return BotProduct(id, name, money, current_field, enabled, skipped_in_a_row,
                          own_planets)


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def __init__(self, id=0, name="", money=100, current_field=0, enabled=1, skipped_in_a_row=0,
                 own_planets={}):
        pass

    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def set_id(self, id):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def set_name(self, name):
        pass

    @abstractmethod
    def get_is_human(self):
        pass

    @abstractmethod
    def get_money(self):
        pass

    @abstractmethod
    def set_money(self, money):
        pass

    @abstractmethod
    def get_current_field(self):
        pass

    @abstractmethod
    def set_current_field(self, number):
        pass

    @abstractmethod
    def get_enabled(self):
        pass

    @abstractmethod
    def set_enabled(self, enabled):
        pass

    @abstractmethod
    def get_skipped_in_a_row(self):
        pass

    @abstractmethod
    def set_skipped_in_a_row(self, turns_amount):
        pass

    @abstractmethod
    def get_own_planets(self):
        pass

    @abstractmethod
    def set_own_planets(self, own_planets):
        pass

    @abstractmethod
    def set_more_money(self, value):
        pass

    @abstractmethod
    def set_less_money(self, value):
        pass

    @abstractmethod
    def is_bankroot(self):
        pass

    @abstractmethod
    def move_to(self, dice_roll):
        pass

    @abstractmethod
    def own_planet(self, planet):
        pass

    @abstractmethod
    def disown_planet(self, planet):
        pass

    @abstractmethod
    def can_upgrade(self):
        pass

    @abstractmethod
    def set_died(self):
        pass


"""
Concrete Products provide various implementations of the Product interface.
"""


class Context():
    """
    The Context defines the interface of interest to clients.
    """

    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        The Context maintains a reference to one of the Strategy objects. The
        Context does not know the concrete class of a strategy. It should work
        with all strategies via the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Usually, the Context allows replacing a Strategy object at runtime.
        """

        self._strategy = strategy

    def choose_action(self, options_from, options_to) -> None:
        """
        The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own.
        """
        return self._strategy.do_algorithm(options_from, options_to)


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: List):
        pass


"""
Concrete Strategies implement the algorithm while following the base Strategy
interface. The interface makes them interchangeable in the Context.
"""


class StrategyBot1(Strategy):
    def do_algorithm(self, options_from, options_to):
        return randint(options_from, options_to)


class HumanProduct(Product):
    def __init__(self, id=0, name="", money=100, current_field=0, enabled=1, skipped_in_a_row=0,
                 own_planets={}):
        self.__id = id
        self.__name = name
        self.__money = money
        self.__current_field = current_field
        self.__enabled = enabled
        self.__skipped_in_a_row = skipped_in_a_row
        self.__own_planets = own_planets

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_is_human(self):
        return 1

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def get_current_field(self):
        return self.__current_field

    def set_current_field(self, number):
        self.__current_field = number

    def get_enabled(self):
        return self.__enabled

    def set_enabled(self, enabled):
        self.__enabled = enabled

    def get_skipped_in_a_row(self):
        return self.__skipped_in_a_row

    def set_skipped_in_a_row(self, turns_amount):
        self.__skipped_in_a_row = turns_amount

    def get_own_planets(self):
        return self.__own_planets

    def set_own_planets(self, own_planets):
        self.__own_planets = own_planets

    def set_more_money(self, value):
        self.set_money(self.__money + value)

    def set_less_money(self, value):
        self.set_money(self.__money - value)
        # if self.__money - value > 0:
        #     self.set_money(self.__money - value)
        #     return 0
        # else:
        #     return -1  # вивести повідомлення про неможливість цієї дії

    def is_bankroot(self):
        return self.__money == 0

    # переміщує гравця на dice_roll клітинок вперед
    def move_to(self, dice_roll):
        if self.__current_field + dice_roll > config.fields_amount:
            self.set_more_money(100)  # скільки грошей додається при проходженні старту?
        self.set_current_field((self.__current_field + dice_roll) % config.fields_amount)
        return self.__current_field

    def own_planet(self, planet):
        self.__own_planets.update({planet: 1})

    def disown_planet(self, planet):
        self.__own_planets.pop(planet)
        return

    def can_upgrade(self):
        return False  # перевірити чи є планети, які можна апгрейднути

    def set_died(self):
        # видалити всю інфу про гравця
        del self.__own_planets
        return


class BotProduct(Product):
    def __init__(self, id=0, name="", money=100, current_field=0, enabled=1, skipped_in_a_row=0,
                 own_planets={}, current_strategy=StrategyBot1()):
        self.__id = id
        self.__name = name
        self.__money = money
        self.__current_field = current_field
        self.__enabled = enabled
        self.__skipped_in_a_row = skipped_in_a_row
        self.__own_planets = own_planets
        self.__strategy = Context(current_strategy)

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_is_human(self):
        return 0

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def get_current_field(self):
        return self.__current_field

    def set_current_field(self, number):
        self.__current_field = number

    def get_enabled(self):
        return self.__enabled

    def set_enabled(self, enabled):
        self.__enabled = enabled

    def get_skipped_in_a_row(self):
        return self.__skipped_in_a_row

    def set_skipped_in_a_row(self, turns_amount):
        self.__skipped_in_a_row = turns_amount

    def get_own_planets(self):
        return self.__own_planets

    def set_own_planets(self, own_planets):
        self.__own_planets = own_planets

    def set_more_money(self, value):
        self.set_money(self.__money + value)

    def set_less_money(self, value):
        if self.__money - value > 0:
            self.set_money(self.__money - value)
            return 0
        else:
            return -1  # вивести повідомлення про неможливість цієї дії

    def is_bankroot(self):
        return self.__money == 0

    # переміщує гравця на dice_roll клітинок вперед
    def move_to(self, dice_roll):
        if self.__current_field + dice_roll > config.fields_amount:
            self.set_more_money(100)  # скільки грошей додається при проходженні старту?
        self.set_current_field((self.__current_field + dice_roll) % config.fields_amount)
        return self.__current_field

    def own_planet(self, planet):
        self.__own_planets.update({planet: 1})

    def disown_planet(self, planet):
        self.__own_planets.pop(planet)
        return

    def can_upgrade(self):
        return False  # перевірити чи є планети, які можна апгрейднути

    def set_died(self):
        # видалити всю інфу про гравця
        del self.__own_planets
        return

    def set_strategy(self, strat):
        self.__strategy.strategy = strat

    def take_action(self, options_from, options_to):
        return self.__strategy.choose_action(options_from, options_to)


def client(creator: Creator, name):
    return creator.create_product(players_counter, name)


def create_player(name, is_human):
    global players_counter
    players_counter += 1
    if is_human:
        return client(HumanCreator(), name)
    else:
        return client(BotCreator(), name)


config = Config()

# class Player:
#     """клас гравця, який визначає основні поля та методи для кожного з учасників гри (людини або бота)"""
#
#     # у сетери та конструктор додати перевірку на тип даних
#     def __init__(self, id=0, name="", is_human=0, money=100, current_field=0, enabled=1, skipped_in_a_row=0,
#                  own_planets=[]):
#         """створення гравця: поля 'ім'я', 'людина/бот (True/False)',
#         'кіл-ть грошей', 'поточне поле', 'може ходити (True/False)',
#         'кіл-ть підряд пропущених ходів', 'куплені планети'"""
#         self.__id = id
#         self.__name = name
#         self.__is_human = is_human
#         self.__money = money
#         self.__current_field = current_field
#         self.__enabled = enabled
#         self.__skipped_in_a_row = skipped_in_a_row
#         self.__own_planets = own_planets
#
#     def __del__(self):
#         Player.__index = 0
#         # видалити гравця з власників усіх планет, якими він володів
#
#     def get_id(self):
#         return self.__id
#
#     def set_id(self, id):
#         self.__id = id
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_is_human(self):
#         return self.__is_human
#
#     def set_is_human(self, is_human):
#         self.__is_human = is_human
#
#     def get_money(self):
#         return self.__money
#
#     def set_money(self, money):
#         self.__money = money
#
#     def get_current_field(self):
#         return self.__current_field
#
#     def set_current_field(self, number):
#         self.__current_field = number
#
#     def get_enabled(self):
#         return self.__enabled
#
#     def set_enabled(self, enabled):
#         self.__enabled = enabled
#
#     def get_skipped_in_a_row(self):
#         return self.__skipped_in_a_row
#
#     def set_skipped_in_a_row(self, turns_amount):
#         self.__skipped_in_a_row = turns_amount
#
#     def get_own_planets(self):
#         return self.__own_planets
#
#     def set_own_planets(self, own_planets):
#         self.__own_planets = own_planets
#
#     def set_more_money(self, value):
#         self.set_money(self.__money + value)
#
#     def set_less_money(self, value):
#         self.set_money(self.__money - value)  # додати перевірку self.__money - value > 0
#
#     def is_bankroot(self):
#         return self.__money == 0
#
#     # переміщує гравця на dice_roll клітинок вперед
#     def move_to(self, dice_roll):
#         self.set_current_field((self.__current_field + dice_roll) % config.fields_amount)
#         return self.__current_field
#
#     def own_planet(self, planet):
#         self.__own_planets.append(planet)
#
#     def disown_planet(self, planet):
#         # видалити цю планету зі списку
#         return
#
#     def can_upgrade(self):
#         return False  # перевірити чи є планети, які можна апгрейднути
#
#     def set_died(self):
#         # видалити всю інфу про гравця
#         return
