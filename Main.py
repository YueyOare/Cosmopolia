from map import *
from players import *

class Builder: # створення гравця
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
        return self
class Cosmopolia:
    """Основний клас гри"""

    def __init__(self):
        self.Players = []  # масив гравців
        self.Amount_of_Players = 0  # загальна кількість гравців
        self.Amount_of_Humans = 0  # кількість гравців - людей
        self.Amount_of_Bots = 0  # кількість гравців - ботів
        self.first_player = 0
        self.Current_Player = 0
        self.result = 0
        self.Number_of_sides_of_cube = 12
        self.map = Map()

    def Create_Players(self):  # створюємо гравців
        self.Amount_of_Players = int(input("введіть загальну кількість гравців: "))
        for i in range(self.Amount_of_Players):  # дамо ім'я гравцям та занесемо їх в масив
            b = Builder()
            N = input("введіть ім'я гравця: ")
            isH = int(input("введіть 1, якщо гравець людина, та 0, якщо гревець бот"))
            player = b.build()
            player = b.name(N)
            player = b.id(i)
            player = b.is_human(isH)
            self.Players.append(player)

    def Randomaise_first_player(self):  # генеруємо першого гравця, що здійснює хід
        self.first_player = self.Players[randint(0, self.Amount_of_Players - 1)]

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
                self.result = self.map.array_Fields[4].player_choice(action, Current_Player)  # здесь нужно поменять
            else:
                self.result = self.map.array_Fields[4].set_free(Current_Player)

    def Player_cube(self, Current_Player):  # дія гравця після кидка кубика
        self.Current_Player = Current_Player
        dice = int(self.Randomaise_dice())  # кидаємо кубик
        self.Current_Player.move_to(dice)  # знаходимо нову позицію гравця
        self.map.array_Fields[self.Current_Player.get_current_field()].event(
            self.Current_Player)  # подія з гравцем на цій позиції

Game = Cosmopolia()
Game.Create_Players()  # створюємо гравців
# while True:
for i in range(5):
    for Current_Player in Game.Players:  # проходимо по циклу гравців
        Game.Before_turn(Current_Player)  # дії до хода гравця
        if Game.result == 1:  # якщо ігрок у в'язниці
            continue
        Game.Player_cube(Current_Player)  # дії під час хода гравця
    Current_Player = Game.Players[0]  # після проходження масива повертаємося до першого гравця в масиві

