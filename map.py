from random import randint
from players import Player

from array import *


class Map():
    """���� ���� ������ ���� �����"""

    class Field():  # ����� ������� �����
        def __init__(self, name_of_class = 0, number_class = 0):
            """������ ��������� ������� ����"""
            self.name_of_class = name_of_class
            self.number_class = number_class

        def print_field(self):
            print(self.__name_of_class + self.__number_class)

        def event(self):
            return 1

    array_Fields = []

    def __init__(self, number=10):
        self.number = number
        for i in range(number):
            self.array_Fields.append(i)


class System():
    """���� ���� ��������� ���������� ��� ��������� ����������"""

    class planet(Map.Field):  # ���� ���� ����������
        def __init__(self, name_of_planet="earth", price_buy=1345, price_pay=648, owner=0, amount_of_branches=5):
            super().__init__()
            self.__name_of_planet = name_of_planet
            self.__price_buy = price_buy
            self.__price_pay = price_pay
            self.__owner = owner
            self.__amount_of_branches = amount_of_branches

        def print_planet(self):
            print(self.__name_of_planet, self.__price_buy, self.__price_pay, self.__owner)

        def set_owner(self, player):  # ����� �� ����� �������� ����������
            print("����� set_owner ������")
            return self.__owner

        def upgrade(self, player, number_class):  # ���������� ����������
            print("����� upgrade ������")
            return self.__price_pay

        def pay(self, player, owner):  # ����� �������� ����������
            print("����� pay ������")
            return 1

        def buy(self, player):  # ������ ���� ���������� ���� ��������
            print("����� buy ������")
            return self.__owner

        def event(self, player):
            if (self.__owner):  # ������ ���� ���������� �� ��������
                if (self.__owner == player):
                    return 1
                else:  # ���� ������� �� � ��������� ����������
                    self.pay(player, self.__owner)
            else:
                return 2  # ������� �� ���� ������� ������� ����

    array_planets = []

    def __init__(self, name_of_sysytem="Sunny", amount_of_planet=10, branches="Sput", cost_of_branches=1993):
        super().__init__()
        self.__name_of_sysytem = name_of_sysytem
        self.__amount_of_planet = amount_of_planet
        self.__branches = branches  # ������
        self.__cost_of_branches = cost_of_branches
        for i in range(amount_of_planet):
            self.array_planets.append(i)


class Chance(Map.Field):
    """���� ���� ����"""
    array_maps = []

    def __init__(self, amount_of_maps=20):  # ������� ����� �����
        super().__init__()
        self.__amount_of_maps = amount_of_maps
        for i in range(amount_of_maps):
            self.array_maps.append(i)

    def event(self, player):  # ������� ������ �����
        print("����� chance ������")
        return 1


# классы Саши. В данный момент они в виде псевдокода. Описана общая логика
class Teleport(Map.Field):
    """Клітина телепорт, що телепортує гравця до рандомної точки"""

    def __init__(self):
        super().__init__()

    # витягнути з мепу телепорти, щоб телепортувати гравця в рандомну клітину типу "телепорт"

    def event(self, Player):
        randomvalue = randint(0, 21)
        print("Метод Телепорт працює")
        Player.set_current_field(randomvalue)
        return 1


class Prison(Map.Field):
    """Клітина в'язниця, що ув'язнює гравця на 2 ходи ( з можливістю втекти )"""

    def __init__(self):
        super().__init__()

    # уточнити, чи є необхідність в додатковому контейнері для гравця ( поточна кількість ходів, що має бути відсижена у в'язниці і т.д)
    prisoner_array = []

    def set_free(self, player, prisoner_index):
        print("Гравця звільнено. Метод set_free працює")
        # видаляємо з масиву
        player.set_enabled(True)
        return 1

    def player_choice(self, player,
                      prisoner_index):  # гравець може вибрати сидіти у в'язниці або спробувати сплатити хабар ( може не спрацювати)
        print("Гравець зробив свій вибір. Метод player_choice працює")
        choice = randint(0, 2)
        value = randint(100, 600)
        random_amount = randint(0, 2)
        if choice == 1:  # якщо гравець вирішив платити хабар, є шанс на те, що він попадеться
            # player.setlessmoney(value) забираємо грошу
            if random_amount == 1:  # якщо гравець попався, то додається ще + 1 простою
                self.prisoner_array[
                    prisoner_index] -= 1  # віднімається ход від поточних відсижених ходів ( тобто гравець сидить довше)
                return 1
            else:
                # якщо гравець не попався, то він виходить достроково
                return self.set_free(player, prisoner_index)
        else:  # якщо гравець відмовився платити хабар, він чекає далі
            print("Гравець сидить далі")
            self.prisoner_array[prisoner_index] += 1
            return 1
        # просто продовжити ?

    def event(self, prisoner):  # !!! уточнити, чи необхідно player ?
        # перевіряємо поточний хід (скільки залишилося у в'язниці ?  цикл ?)
        for player in self.prisoner_array:  # проходимо по масиву ув'язнених, перевіряючи, чи є даний гравець у в'язниці
            if player == prisoner:  # problem !!!!!!! якщо знайшли, що гравець у в'язниці, виконуємо наступні дії
                if player <= 2:
                    # якщо гравець ще має сидіти у в'язниці, запропонувати гравцю вибір
                    return self.player_choice(prisoner, 0)
                else:  # строк сидіння закінчився, гравець звільнився
                    return self.set_free()
        self.prisoner_array.append({prisoner,0})  # додаємо у в'язницю, якщо гравця нема
        prisoner.set_enabled(False)  # ув'язнюємо
        return 1


class StartFinish(Map.Field):  # скоріш за все, додавати гроші буде зручніше через мейн та гравця
    """Клітина початку гри, що видає на кожному колі додатковий капітал"""

    def __init__(self):
        super().__init__()

    def event(self, Player):
        print("Метод СтартФініш працює")
        return 1


class Casino(Map.Field):
    """Клітина казіно, що дає гравцю вибір зіграти в казино або в рулетку"""

    def __init__(self):
        super().__init__()

    def casino(self, player, bet):  # метод казино, що дозволяє гравцю зробити ставку
        print("Метод казино працює")
        number = randint(0, 2)
        player.setLessMoney(bet)  # ставка зроблена
        if number == 1:  # зарандомити число
            print("Гравець виграв")
            player.setMoreMoney(bet * 3)
            return 1
        else:
            print("Гравець програв")
            return 1  # гравець програв, завершити програму

    def roulette(self, player, bet):  # метод рулетка, що дає можливість гравцю зіграти на великий виграш з вірогідністю померти.
        print("Метод рулетка працює")
        number = randint(0, 2)
        player.setLessMoney(bet)
        if number == 1:  # зарандомити число
            print("Гравець виграв")
            player.setMoreMoney(bet * 3)
            return 1
        else:
            print("Гравець програв і помер")
            player.set_died()
            return 1  # гравець програв і помер, завершити програму

    def event(self, player):  # івент клітини казіно
        # Random_value ( 0 or 1) - рандомиться цифра 1 або 0, що визначає, піде гравець в казино або в рулетку
        random_value = randint(0, 2)
        askamount = randint(0, 2)
        if random_value == 0:  # - якщо зарандомилася цифра 0, відправляємо гравця в казино без права відмовитися
            # вернуть число, которое означает, что выбрано казино, чтобы спросить, будет ли игрок играть или нет
            return self.casino(player, 0)
        else:  # інакше відправляємо гравця в рулетку, і даємо право відмовитися
            # Ask Asya for number - питаю в мейну вибір гравця
            if askamount == 1:  # якщо гравець вибрав грати, відправляюємо в рулетку
                # вернуть число, означающее игру в рулетку, чтобы спросить, будет ли игрок играть или нет
                return self.roulette(player, 0)
            else:  # якщо гравець відмовився,  завершити гру
                print("Гравець відмовився")
                return 1


# Map1 = Map()
# Field1 = Map1.Field("����", 2)
# System1 = System("Sun", 2, "sputniki", 8139838)
# System2 = System("Sirius", 4)
# Planet11 = System2.planet("Alfa", 22, 77, "Human1")
# Planet = System1.planet(12232, 123, "Human2")
# Planet1 = System1.planet("Mars", 2222, 111, "Bot")
# Planet11.print_planet()
# Planet1.event(2)
#
# player1 = Player(name="player1", is_human=1)
# casino1 = Casino()
# prison1 = Prison()
# startfinish1 = StartFinish()
# teleport1 = Teleport()
#
# prison1.event(player1)
# prison1.event(player1)
# casino1.event(player1)
# startfinish1.event(player1)
# teleport1.event(player1)

