from array import *
class Map():
    """���� ���� ������ ���� �����"""
    array_Fields = []
    array.append(int)
    class Field(): # ����� ������� �����
        def __init__(self, __name_of_class, __number_class, __event):
         """������ ��������� ������� ����"""
        self.__name_of_class = name_of_class
        self.__number_class = number_class
        self.__event = event

class System():
    """���� ���� ��������� ���������� ��� ��������� ����������"""
    def __init__(self, __name_of_sysytem, __amount_of_planet, __branches, __cost_of_branches, __planet):
     """"""
     self.__name_of_sysytem = name_of_sysytem
     self.__amount_of_planet = amount_of_planet
     self.__branches =  branches
     self.__cost_of_branches = __cost_of_branches
     self.__planet = planet

     class planet(Field): # ���� ���� ����������
          def __init__(self, __price_buy , __price_pay, __owner):
           self.__price_buy = price_buy
           self.__price_pay = price_pay
           self.__owner = _owner
          def set_owner(player): # ����� �� ����� �������� ����������
              return self.__owner
          if(self.__owner): # ������ ���� ����������� �� ��������
              if(self.__owner==player):
                def upgrade(player, __nunber_class): # ���������� ����������
                    return self.__price_pay
              else: # ���� ������� �� � ��������� ����������
                  def pay(player_who_pays,paid_player): # ����� �������� ����������
                      return 0
          else:
              def buy(player): # ������ ���� ���������� ���� ��������
                  return self.__owner

class Chance(Field):
    """���� ���� ����"""
    def __init__(self, __chance_map): # ������� ����� �����
        self.__chance_map = chance_map
    def random_map_selection(player): # ������� ������ �����
        return self.__chance_map
