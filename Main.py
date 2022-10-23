from random import randint
from map import *
from players import *

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
        self.Amount_of_Humans = int(input("введіть кількість живих гравців: "))
        for i in range(self.Amount_of_Humans):  # дамо ім'я гравцям-люядям та занесемо їх в масив
            Name = input("введіть ім'я гравця: ")
            player = Player(name=Name, id=i, is_human=1)
            self.Players.append(player)
        self.Amount_of_Bots = self.Amount_of_Players - self.Amount_of_Humans  # знаходимо кількість ботів
        for i in range(self.Amount_of_Bots):  # дамо ім'я гравцям-ботам та занесемо їх в масив
            Name = input("введіть ім'я бота: ")
            player = Player(name=Name, id=i + self.Amount_of_Humans, is_human=0)
            self.Players.append(player)

    def Randomaise_first_player(self):  # генеруємо першого гравця, що здійснює хід
        self.first_player = self.Players[randint(0, self.Amount_of_Players - 1)]

    def Randomaise_dice(self):  # Кидаємo кубик
        return randint(1, self.Number_of_sides_of_cube)

    def Print_field_to_Player(self, Current_Player):  # Выводим поле на консоль
        print("field")

    def Before_turn(self, Current_Player):  # действия до хода
        self.Print_field_to_Player(Current_Player)  # Выводим поле на консоль
        if not Current_Player.get_enabled():  # Может ли игрок совершать ход? Если нет...
            if self.Current_Player.get_move_main(Current_Player) < 3:  # Если в тюрьме меньше трех ходов...
                action = int(input(
                    "Enter variant of action in prison: 1 - хабарь, 2 - сідіти далі, 3 - збігти"))  # Действие игрока в тюрьме
                self.result = self.map.array_Fields[4].player_choise(action, Current_Player)  # здесь нужно поменять
            else:
                self.result = self.map.array_Fields[4].set_free(Current_Player)

    def Player_cube(self, Current_Player):  # действие игрока после броска кубика
        self.Current_Player = Current_Player
        dice = int(self.Randomaise_dice())  # Кидаем кубик
        self.Current_Player.move_to(dice)  # находим новую позицию игрока
        self.map.array_Fields[self.Current_Player.get_current_field()].event(
            self.Current_Player)  # Событие с игроком на этой позиции


Game = Cosmopolia()
Game.Create_Players()  # Створюємо гравців
while True:
    for Current_Player in Game.Players:  # проходимо по циклу гравців
        Game.Before_turn(Current_Player)  # Дії до хода гравця
        if Game.result == 1:  # Якщо ігрок у в'язниці
            continue
        Game.Player_cube(Current_Player)  # Дії під час хода гравця
    Current_Player = Game.Players[0]  # після проходження масива повертаємося до першого гравця в масиві

