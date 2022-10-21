class Cosmopolia(): 
    """Основний клас гри"""
    def __init__(self):
        self.Players = [] #масив гравців
        self.Amount_of_Players = 0 #загальна кількість гравців
        self.Amount_of_Humans = 0 #кількість гравців - людей
        self.Amount_of_Bots = 0 #кількість гравців - ботів
        self.first_player = 0
        self.Current_Player = 0
    def Create_Players(self): #створюємо гравців
        self.Amount_of_Players = int(input("введіть загальну кількість гравців: "))
        self.Amount_of_Humans = int(input("введіть кількість живих гравців: "))
        for i in range(Amount_of_Humans): #дамо ім'я гравцям-люядям та занесемо їх в масив
            Name = input("введіть ім'я гравця: ")
            Players.append(Player(Name))
            Players[i](id = i, is_human = 1)
        Amount_of_Bots = Amount_of_Players - Amount_of_Humans #знаходимо кількість ботів
        for i in range(Bot_amount): #дамо ім'я гравцям-ботам та занесемо їх в масив
            Name = input("введіть ім'я бота: ")
            Players.append(Player(Name))
            Players[i+Amount_of_Humans](id = (i+Amount_of_Humans))

    def Randomaise_first_player(): #генеруємо першого гравця, що здійснює хід
        first_player = randint(0, Amount_of_Players - 1)

    def Randomaise_dice(): #Кидаємo кубик
        Number_of_sides_of_cube = 12
        randint(0, Number_of_sides_of_cube)

    def Print_field_to_Player(Current_Player): #Выводим поле на консоль
        print("field")

    def Before_turn(Current_Player): #действия до хода
        Print_field_to_Player(Current_Player) #Выводим поле на консоль
        if(get_enabled(Current_Player) == False): #Может ли игрок совершать ход? Если нет...
            if(get_move_main(Current_Player) != 3): #Если в тюрьме меньше трех ходов...
                action = int(input("Enter variant of action in prison: 1 - заплатити, 2 - сідіти далі, 3 - збігти")) #Действие игрока в тюрьме
        result = Prison(action, Current_Player)
    def Player_cube(Current_Player): #действие игрока после броска кубика
        dice = int(Randomaise_dice()) #Кидаем кубик
        set_current_field(Current_Player, dice) #находим новую позицию игрока
        Field.event(Current_Player) #Событие с игроком на этой позиции
