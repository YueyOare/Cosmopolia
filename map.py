from array import *
class Map():
    """Клас який містить саму карту"""
    array_Fields = []
    array.append(int)
    class Field(): # класс клітинок карти
        def __init__(self, __name_of_class, __number_class, __event):
         """Основні параметри кожного поля"""
        self.__name_of_class = name_of_class
        self.__number_class = number_class
        self.__event = event

class System():
    """Клас який класифікує нерухомість для можливості покращення"""
    def __init__(self, __name_of_sysytem, __amount_of_planet, __branches, __cost_of_branches, __planet):
     """"""
     self.__name_of_sysytem = name_of_sysytem
     self.__amount_of_planet = amount_of_planet
     self.__branches =  branches
     self.__cost_of_branches = __cost_of_branches
     self.__planet = planet

     class planet(Field): # клас самої нерухомості
          def __init__(self, __price_buy , __price_pay, __owner):
           self.__price_buy = price_buy
           self.__price_pay = price_pay
           self.__owner = _owner
          def set_owner(player): # метод що змінює власника нерухомості
              return self.__owner
          if(self.__owner): # методи якщо нерухомістьл має власника
              if(self.__owner==player):
                def upgrade(player, __nunber_class): # покращення нерухомості
                    return self.__price_pay
              else: # якщо гравець не є власником нерухомості
                  def pay(player_who_pays,paid_player): # плата власнику нерухомості
                      return 0
          else:
              def buy(player): # методи якщо нерухомість немає власника
                  return self.__owner

class Chance(Field):
    """Клас поля Шанс"""
    def __init__(self, __chance_map): # варіанти карти шансу
        self.__chance_map = chance_map
    def random_map_selection(player): # гравець отримує карту
        return self.__chance_map
