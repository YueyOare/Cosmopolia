class Player:
    """клас гравця, який визначає основні поля та методи для кожного з учасників гри (людини або бота)"""

    def __init__(self, id, name, is_human, money, current_field, enabled):
        """створення гравця"""
        self.id = id
        self.name = name
        self.is_human = is_human
        self.money = money
        self.current_field = current_field
        self.enabled = enabled

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_is_human(self):
        return self.is_human

    def set_is_human(self, is_human):
        self.is_human = is_human

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def get_current_field(self):
        return self.current_field

    def set_current_field(self, current_field):
        self.current_field = current_field

    def get_enabled(self):
        return self.enabled

    def set_enabled(self, enabled):
        self.enabled = enabled

    def setMoreMoney(self, value):
        self.money += value

    def setLessMoney(self, value):
        self.money -= value

    def is_bankroot(self):
        return self.money == 0
