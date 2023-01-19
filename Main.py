from map import *
from players import *
from PlanetChance import *
from gamefields import *


class Cosmopolia:
    """Основний клас гри"""

    def __init__(self):
        self.Players = []  # масив гравців
        self.Amount_of_Players = 0  # загальна кількість гравців
        #self.Amount_of_Humans = 0   кількість гравців - людей
        #self.Amount_of_Bots = 0   кількість гравців - ботів
        self.first_player = 0
        self.Current_Player = 0
        self.result = 1
        self.Number_of_sides_of_cube = 12
        self.map = Map()
    def Randomaise_first_player(self):  # генеруємо першого гравця, що здійснює хід
        self.first_player = self.Players[randint(0, self.Amount_of_Players - 1)]
    def Create_Players(self):  # створюємо гравців
        self.Amount_of_Players = int(input("введіть загальну кількість гравців: "))
        for i in range(self.Amount_of_Players):  # дамо ім'я гравцям та занесемо їх в масив
            isH = int(input("введіть 1, якщо гравець людина, та 0, якщо гравець бот: "))
            while True:
                if isH == 1 or isH == 0:
                    break
                isH = int(input("введіть 1, якщо гравець людина, та 0, якщо гравець бот: "))
            Name = input("введіть ім'я гравця: ")
            player = Player(name=Name, id=i, is_human=isH)
            self.Players.append(player)  # заносимо гравця до масиву
    def Randomaise_dice(self):  # кидаємo кубик
        return randint(1, self.Number_of_sides_of_cube)

    def Print_field_to_Player(self, Current_Player):  # виводимо поле на консоль
        print("field")

    def Before_turn(self, Current_Player):  # дії до хода
        self.Print_field_to_Player(Current_Player)  # виводимо поле на консоль
        if not Current_Player.get_enabled():  # чи може гравець здійснювати хід? Якщо ні...
            if self.map.array_Fields[4].get_move_main(Current_Player) < 3:  # якщо у в'язниці менше трьох ходів...
                action = int(input(
                    "Enter variant of action in prison: 1 - хабарь, 2 - сідіти далі, 3 - збігти"))  # дія гравця у в'язниці
                self.result = self.map.array_Fields[4].player_choice(action, Current_Player)
            else:
                self.result = self.map.array_Fields[4].set_free(Current_Player)
            if self.result == 1:
                print("Гравець тепер на волі")
            elif self.result == 0:
                print("Гравець залишається у в'язниці")

    def Player_cube(self, Current_Player):  # дія гравця після кидка кубика
        self.Current_Player = Current_Player
        dice = int(self.Randomaise_dice())  # кидаємо кубик
        self.Current_Player.move_to(dice)  # знаходимо нову позицію гравця
        word = self.map.array_Fields[self.Current_Player.get_current_field()].event(
            self.Current_Player)  # подія з гравцем на цій позиції
        second_action = Console_fields(Current_Player)  # викликаємо дію гравця на полі
        second_action.switch_first(word)
class Console_fields:
    """Клас взаємодії полей з користувачем"""
    def __init__(self, player = Player()):
        self.word = ""
        self.player = player
        self.bid = 0
    def switch_first(self, ev): # вибір поля, на який потравив гравець
        self.word = ev
        if self.word == "Casino": # гравець потравив на поле казино
            self.bid =int(input("Ви на клітинці Казино. Виберіть ставку: ")) # гравець вибирає ставку
            while True:
                if self.bid > 1 and self.bid < self.player.get_money(): # перевірка коректності введених даних користувачем
                    game = StrategyCasino()
                    res = game.startgame(self.player, self.bid)  #!!!!!!!!! вызывается свитч только один раз, для результата нужен второй
                    self.switch_second(res)
                    break
                print("Ставка некорректна. Гравець ", self.player.get_name(), " має таку суму грошей: ", self.player.get_money)
                self.bid =int(input("Виберіть ставку: "))
        elif self.word == "Free": # гравця було звільнено зі в'язниці
            print("Гравця ", self.player.get_name(), " було звільнено зі в'язниці")
        elif self.word == "Teleport": # гравець на полі телепорт
            print("Ви попали на клітинку Телепорт. Ваша нова позиція: ", self.player.get_current_field())
        elif self.word == "Imprisoned": # гравець потравим до в'язниці
            print("На жаль, ви потрапили до в'язниці")
        elif self.word == "StartFinish": # гравець потравив на поле Старт/Фіниш
            print("Ви потрапили на клітинку Старт/Фініш")
        elif self.word == "Roulette": # гравець потравив на поле рулетка. Чи хоче він грати?
            answer = input("Ви потрапили на клітинку Рулетка. Чи хочете зіграти на свое життя? 1 - Так, 0 - Ні")
            while True:
                if answer == 1: # якщо так - граємо
                    game = StrategyRoulette()
                    res = game.startgame(self.player)
                    self.switch_second(res)
                    break
                elif answer == 0: # якщо ні, йдемо далі
                    break
        elif self.word == "player must pay": # гравець потрапил на чуже поле, тому повинен заплатити аренду
            print("Ви потрапили на чуже поле, тому повинні заплатити аренду")
            payment = System().Planet()
            payment.pay(self.player)
        elif self.word == "player can buy": # гравець потрапил на вільне поле, чи хочете його купити?
            while True:
                answer = int(input("Ви потрапили на вільне поле, чи хочете його купити? 1 - так, 0 - ні: "))
                if answer == 1:
                    payment = System().Planet() # якщо так, покупає
                    payment.buy(self.player)
                    break
                elif answer == 0: # якщо ні, йдемо далі
                    break
    def switch_second(self, res):  # результати казино та рулетки
        self.word = res
        if self.word == "WinCasino": # гравець виграв в казино
            print("Перемога. Гравець ", self.player.get_name(), " виграв ", self.bid*3,", тепер має таку суму грошей: ", self.player.get_money)
        elif self.word == "LoseCasino": # гравець програв в казино
            print("Програш. Гравець ", self.player.get_name(), " програв ", self.bid, ", залишок: ", self.player.get_money)
        elif self.word == "WinRoulette": # гравець виграв в рулетку
            print("Перемога. Гравець ", self.player.get_name(), " тепер має таку суму грошей: ", self.player.get_money)
        elif self.word == "LoseRoulette": # гравець програв в рулетку
            print("Програш. Гравець ", self.player.get_name(), " помер :)")
            self.player.set_died()

"""class Builder:
    def __init__(self):
        self.player = Player()
    def build(self):
        return self.player
    def name(self, N):
        self.player.name = N
        return self
    def id(self, i):
        self.player.id = i
        return self
    def is_human(self, isH):
        self.player.is_human = isH
        return self"""

Game = Cosmopolia()
Game.Create_Players()  # створюємо гравців
# while True:
for i in range(5):
    for Current_Player in Game.Players:  # проходимо по циклу гравців
        Game.Before_turn(Current_Player)  # дії до хода гравця
        if Game.result == 0:  # якщо ігрок у в'язниці
            continue
        Game.Player_cube(Current_Player)  # дії під час хода гравця
    Current_Player = Game.Players[0]  # після проходження масива повертаємося до першого гравця в масиві

