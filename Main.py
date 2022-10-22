from random import randint
class Cosmopolia(): 
    """Основний клас гри"""
    def __init__(self):
        self.Players = [] #масив гравців
        self.Amount_of_Players = 0 #загальна кількість гравців
        self.Amount_of_Humans = 0 #кількість гравців - людей
        self.Amount_of_Bots = 0 #кількість гравців - ботів
        self.first_player = 0
        self.Current_Player = 0
        self.result = 0
        self.Number_of_sides_of_cube = 12
        self.action = 0
    def Create_Players(self): #створюємо гравців
        self.Amount_of_Players = int(input("введіть загальну кількість гравців: "))
        self.Amount_of_Humans = int(input("введіть кількість живих гравців: "))
        for i in range(self.Amount_of_Humans): #дамо ім'я гравцям-люядям та занесемо їх в масив
            Name = input("введіть ім'я гравця: ")
            player = Player(name = Name)
            self.Players.append(player)
            self.Players[i](id = i, is_human = 1)
        self.Amount_of_Bots = self.Amount_of_Players - self.Amount_of_Humans #знаходимо кількість ботів
        for i in range(Bot_amount): #дамо ім'я гравцям-ботам та занесемо їх в масив
            Name = input("введіть ім'я бота: ")
            self.Players.append(Player(Name))
            self.Players[i+Amount_of_Humans](id = (i+Amount_of_Humans))
    def Randomaise_first_player(self): #генеруємо першого гравця, що здійснює хід
        self.first_player = self.Players[randint(0, Amount_of_Players - 1)]

    def Randomaise_dice(self): #Кидаємo кубик
        randint(0, self.Number_of_sides_of_cube)

    def Print_field_to_Player(self): #Выводим поле на консоль
        print("field")

    def Before_turn(self, Current_Player): #действия до хода
        self.Current_Player = Current_Player
        Print_field_to_Player(self.Current_Player) #Выводим поле на консоль
        if(Player.get_enabled(self.Current_Player) == False): #Может ли игрок совершать ход? Если нет...
            if(Player.get_move_main(self.Current_Player) != 3): #Если в тюрьме меньше трех ходов...
                self.action = int(input("Enter variant of action in prison: 1 - заплатити, 2 - сідіти далі, 3 - збігти")) #Действие игрока в тюрьме
 #       result = Prison(action, Current_Player)

    def Player_cube(self, Current_Player): #действие игрока после броска кубика
        self.Current_Player = Current_Player
        dice = int(self.Randomaise_dice()) #Кидаем кубик
        Player.set_current_field(self.Current_Player, dice) #находим новую позицию игрока
        Map.array_Fields[self.Current_Player.get_current_field()].event(Current_Player) #Событие с игроком на этой позиции

Game = Cosmopolia()
Game.Create_Players() #Створюємо гравців
Game.Current_Player = Game.Randomaise_first_player() #генеруємо першого гравця
while(True): 
    for i in range(Game.Amount_of_Players(Current_Player)): #проходимо по циклу гравців
        Game.Before_turn(Current_Player) #Дії до хода гравця
#        if (result == 1): #Якщо ігрок в 
#            if (i!=(Game.Amount_of_Players - 1)): #Умова, що це не останній ігрок в масиві
#                Current_Player = Game.Players[Cosmopolia.Players.index(Current_Player + 1)]
#            continue
        Game.Player_cube(Current_Player) #Дії під час хода гравця
        if (i!=(Game.Amount_of_Players - 1)): #Умова, що це не останній ігрок в масиві
            Current_Player = Game.Players[Game.Players.index(Current_Player + 1)] #переходимо до наступного гравця
    Current_Player = Game.Players[0] #після проходження масива повертаємося до першого гравця в масиві

