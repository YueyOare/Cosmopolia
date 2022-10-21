from array import *
class Map():
    """���� ���� ������ ���� �����""" 
    class Field(): # ����� ������� �����
      def __init__(self, name_of_class, number_class):
       """������ ��������� ������� ����"""
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
    """���� ���� ��������� ���������� ��� ��������� ����������"""
    class planet(Map.Field): # ���� ���� ����������
      def __init__(self, name_of_planet = "earth", price_buy = 1345, price_pay = 648, owner = 0, amount_of_branches = 5):
         self.__name_of_planet = name_of_planet
         self.__price_buy = price_buy
         self.__price_pay = price_pay
         self.__owner = owner
         self.__amount_of_branches = amount_of_branches
      def print_planet(self):
               print(self.__name_of_planet, self.__price_buy, self.__price_pay, self.__owner)
      def set_owner(self, player): # ����� �� ����� �������� ����������
               print("����� set_owner ������")
               return self.__owner
      def upgrade(self,player, number_class):  # ���������� ����������
               print("����� upgrade ������")
               return self.__price_pay
      def pay(self,player,owner): # ����� �������� ����������
               print("����� pay ������")
               return 1
      def buy(self,player): # ������ ���� ���������� ���� ��������
               print("����� buy ������")
               return self.__owner  
      def event(self, player):
        if(self.__owner): # ������ ���� ���������� �� ��������
          if(self.__owner==player):
             return 1
          else:  # ���� ������� �� � ��������� ����������
            self.pay(player,self.__owner)
        else:
            return 2 # ������� �� ���� ������� ������� ����
    
    array_planets=[]
    def __init__(self, name_of_sysytem = "Sunny", amount_of_planet = 10, branches = "Sput", cost_of_branches = 1993):
       self.__name_of_sysytem = name_of_sysytem
       self.__amount_of_planet = amount_of_planet
       self.__branches =  branches # ������
       self.__cost_of_branches = cost_of_branches
       for i in range (amount_of_planet):
           self.array_planets.append(i)

class Chance(Map.Field):
    """���� ���� ����"""
    array_maps=[]
    def __init__(self, amount_of_maps = 20): # ������� ����� �����
        self.__amount_of_maps = amount_of_maps
        for i in range (amount_of_maps):
           self.array_maps.append(i)
    def event(self, player): # ������� ������ �����
        print("����� chance ������")
        return 1


# классы Саши. В данный момент они в виде псевдокода. Описана общая логика
class Teleport(Map.Field):
    """Клітина телепорт, що телепортує гравця до рандомної точки"""
    def event(self, Player):
        print("Метод Телепорт працює")
        # set_player_pos(Random_value) - чий це метод ?
        return 1


class Prison(Map.Field):
    """Клітина в'язниця, що ув'язнює гравця на 2 ходи ( з можливістю втекти )"""
    # уточнити, чи є необхідність в додатковому контейнері для гравця ( поточна кількість ходів, що має бути відсижена у в'язниці і т.д)
    def set_free(self):
        print("Гравця звільнено. Метод set_free працює")
        # обнулити кількість ходів та флаг того, что гравець у в'язниці ?
        return 1
    def get_move_main(self):
        print("Отримано дані про ходи, що має відсидіти гравець. Метод get_move_main працює")
        # отримати дані про поточні ходи, що залишилися гравцю у в'язниці ( можливо, з можливістю додавати додаткові чи обнуляти)
    def player_choice(self): # гравець може вибрати сидіти у в'язниці або спробувати сплатити хабар ( може не спрацювати)
        print("Гравець зробив свій вибір. Метод player_choice працює")
        # спитати в мейну, чи хоже гравець сидіти чи заплатити хабар (якийсь фіксований)
        if(choice == 1): #якщо гравець вирішив платити хабар, є шанс на те, що він попадеться
            # setlessmoney(value)
            if(random_amount == 1) : # якщо гравець попався, то додається ще + 1 ход (або 2) простою
                get_move_main() # !!! можливо, в цьому методі буде додавання зайвих ходів простою ?
            else :
            # якщо гравець не попався, то він виходить достроково
                set_free()
        else: # якщо гравець відмовився платити хабар, він чекає далі
            print("Гравець сидить далі")
         # просто продовжити ?


    def event(self, Player): # !!! уточнити, чи необхідно player ?
        # перевіряємо поточний хід (скільки залишилося у в'язниці ?  цикл ?)
        if (self.get_move_main() < 2 and self.get_move_main() > 0): # якщо гравець ще має сидіти у в'язниці, запропонувати гравцю вибір
            self.player_choice()
        else: # строк сидіння закінчився, гравець звільнився
            set_free()
            return 1


class StartFinish(Map.Field):
    """Клітина початку гри, що видає на кожному колі додатковий капітал"""
    def event(self, Player):
        print("Метод СтартФініш працює")
        #set_more_money(value)

class Casino(Map.Field):
    """Клітина казіно, що дає гравцю вибір зіграти в казино або в рулетку"""
    def casino(self, player): # метод казино, що дозволяє гравцю зробити ставку
        print("Метод казино працює")
        # get_the_value() - поспитати в мейну яку ставку зробить гравець
        # setlessmoney(value) - ставка зроблена
        if(number == 1): # зарандомити число
            print("Гравець виграв")
            # setmoremoney(value)
            return 1
        else:
            print("Гравець програв")
            return 1 # гравець програв, завершити програму

    def roulette(self, player): # метод рулетка, що дає можливість гравцю зіграти на великий виграш з вірогідністю померти.
        print("Метод рулетка працює")
        if(number == 1): # зарандомити число
            print("Гравець виграв")
            # setmoremoney(value)
            return 1
        else:
            print("Гравець програв і помер")
            # kill()
            return 1 # гравець програв і помер, завершити програму і видалити гравця
    def event(self, Player): # івент клітини казіно
        #Random_value ( 0 or 1) - рандомиться цифра 1 або 0, що визначає, піде гравець в казино або в рулетку
        if (Random_value == 0): # - якщо зарандомилася цифра 0, відправляємо гравця в казино без права відмовитися
            self.casino()
        else: # інакше відправляємо гравця в рулетку, і даємо право відмовитися
            # Ask Asya for number - питаю в мейну вибір гравця
            if(AskAmount == 1):# якщо гравець вибрав грати, відправляюємо в рулетку
                self.roulette()
            else: # якщо гравець відмовився,  завершити гру
                print("Гравець відмовився")
                return 1





Map1 = Map()
Field1 = Map1.Field("����", 2)
System1 = System("Sun", 2, "sputniki", 8139838)
System2 = System("Sirius", 4)
Planet11 = System2.planet("Alfa", 22, 77, "Human1")
Planet = System1.planet(12232, 123, "Human2")
Planet1 = System1.planet("Mars",2222, 111, "Bot")
Planet11.print_planet()
Planet1.event(2)
