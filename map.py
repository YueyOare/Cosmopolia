from array import *
class Map():
    """Клас який містить саму карту""" 
    class Field(): # класс клітинок карти
      def __init__(self, name_of_class, number_class):
       """Основні параметри кожного поля"""
       self.name_of_class = name_of_class
       self.number_class = number_class
      def print_field(self):
          print(self.__name_of_class + self.__number_class)
      def event():
       return 1

    array_Fields=[]
    def __init__ (self, number = 10):
        self.number = number 
        for i in range (number):
           self.array_Fields.append(i)
   

class System():
    """Клас який класифікує нерухомість для можливості покращення"""
    class planet(Map.Field): # клас самої нерухомості
      def __init__(self, name_of_planet = "earth", price_buy = 1345, price_pay = 648, owner = 0, amount_of_branches = 5):
         self.__name_of_planet = name_of_planet
         self.__price_buy = price_buy
         self.__price_pay = price_pay
         self.__owner = owner
         self.__amount_of_branches = amount_of_branches
      def print_planet(self):
               print(self.__name_of_planet, self.__price_buy, self.__price_pay, self.__owner)
      def set_owner(self, player): # метод що змінює власника нерухомості
               print("метод set_owner працює")
               return self.__owner
      def upgrade(self,player, number_class):  # покращення нерухомості
               print("метод upgrade працює")
               return self.__price_pay
      def pay(self,player,owner): # плата власнику нерухомості
               print("метод pay працює")
               return 1
      def buy(self,player): # методи якщо нерухомість немає власника
               print("метод buy працює")
               return self.__owner  
      def event(self, player):
        if(self.__owner): # методи якщо нерухомість має власника
          if(self.__owner==player):
             return 1
          else:  # якщо гравець не є власником нерухомості
            self.pay(player,self.__owner)
        else:
            return 2 # питання чи буде гравець купляти поле
    
    array_planets=[]
    def __init__(self, name_of_sysytem = "Sunny", amount_of_planet = 10, branches = "Sput", cost_of_branches = 1993):
       self.__name_of_sysytem = name_of_sysytem
       self.__amount_of_planet = amount_of_planet
       self.__branches =  branches # філіали
       self.__cost_of_branches = cost_of_branches
       for i in range (amount_of_planet):
           self.array_planets.append(i)

     
class Chance(Map.Field):
    """Клас поля Шанс"""
    array_maps=[]
    def __init__(self, amount_of_maps = 20): # варіанти карти шансу
        self.__amount_of_maps = amount_of_maps
        for i in range (amount_of_maps):
           self.array_maps.append(i)
    def event(self, player): # гравець отримує карту
        print("метод chance працює")
        return 1

Map1 = Map()
Field1 = Map1.Field("шанс", 2)
System1 = System("Sun", 2, "sputniki", 8139838)
System2 = System("Sirius", 4)
Planet11 = System2.planet("Alfa", 22, 77, "Human1")
Planet = System1.planet(12232, 123, "Human2")
Planet1 = System1.planet("Mars",2222, 111, "Bot")
Planet11.print_planet()
Planet1.event(2)
Chance.event(2,2)
