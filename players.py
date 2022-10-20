n = 20  # кіл-ть клітинок на полі
from random import randint

class Player:
    """клас гравця, який визначає основні поля та методи для кожного з учасників гри (людини або бота)"""
    __index = 0

    def __new__(cls, *args, **kwargs):
        cls.__index += 1
        return super().__new__(cls)

    # у сетери та конструктор додати перевірку на тип даних
    def __init__(self, name="", is_human=0, money=100, current_field=0, enabled=1, skipped_in_a_row=0, own_planets=[]):
        """створення гравця: поля 'ім'я', 'людина/бот (True/False)',
        'кіл-ть грошей', 'поточне поле', 'може ходити (True/False)',
        'кіл-ть підряд пропущених ходів', 'куплені планети'"""
        self.__id = self.__index
        self.__name = name
        self.__is_human = is_human
        self.__money = money
        self.__current_field = current_field
        self.__enabled = enabled
        self.__skipped_in_a_row = skipped_in_a_row
        self.__own_planets = own_planets

    def __del__(self):
        Player.__index = 0
        # видалити гравця з власників усіх планет, якими він володів

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_is_human(self):
        return self.__is_human

    def set_is_human(self, is_human):
        self.__is_human = is_human

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
        if self.__enabled:
            print('Тепер гравець', self.__name, 'може ходити\n')
        else:
            print('Тепер гравець', self.__name, 'не може ходити\n')

    def get_skipped_in_a_row(self):
        return self.__skipped_in_a_row

    def set_skipped_in_a_row(self, turns_amount):
        self.__skipped_in_a_row = turns_amount
    def get_own_planets(self):
        return self.__own_planets

    def set_own_planets(self, own_planets):
        self.__own_planets = own_planets

    def setMoreMoney(self, value):
        self.set_money(self.__money + value)
        print('Тепер у гравця', self.__name, self.__money, 'грошей')

    def setLessMoney(self, value):
        self.set_money(self.__money - value)  # додати перевірку self.__money - value > 0
        print('Тепер у гравця', self.__name, self.__money, 'грошей')

    def is_bankroot(self):
        return self.__money == 0

    # переміщує гравця на dice_roll клітинок вперед
    def move_to(self, dice_roll):
        self.set_current_field((self.__current_field + dice_roll) % n)
        print('Тепер гравець', self.__name, 'знаходиться на клітинці', self.__current_field)

    def own_planet(self, planet):
        print('Тепер гравець', self.__name, 'володіє планетою', planet)
        self.__own_planets.append(planet)

    def disown_planet(self, planet):
        print('Гравець', self.__name, 'більше не володіє планетою', planet)
        # видалити цю планету зі списку
        return

    def can_upgrade(self):
        print('В гравця', self.__name, 'немає планет для апгрейду')
        return False # перевірити чи є планети, які можна апгрейднути

    def set_died(self):
        # видалити всю інфу про гравця
        print('Гравця', self.__name, 'майже видалено')
        return


# player1 = Player(name="player1", is_human=1)
# player2 = Player(name="player2", is_human=1)
# player3 = Player(name="player3", is_human=0)

# print(player1.get_money())
# player1.setMoreMoney(50)
# print(player1.get_money())
# print(player1.get_current_field())
# player1.move_to(randint(0, 7))
# print(player1.get_current_field())
