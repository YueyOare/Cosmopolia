import random
from random import randint
from fields import Field
class Teleport(Field):
    """Клітина телепорт, що телепортує гравця до рандомної точки"""

    def __init__(self):
        super().__init__()

    def event(self, player):
        randomvalue = randint(0, 9)
        if random.choice([True, False]):
            player.move_to(randomvalue)
            print("Метод Телепорт працює, переміщає на ", randomvalue," клітин уперед")# буде перенесено в мейн
        else:
            player.move_to(-randomvalue)
            print("Метод Телепорт працює, переміщає на ", randomvalue," клітинок назад")# буде перенесено в мейн
        return 1


class Prison(Field): # state патерн - сможем разделить состояние игрока (свободен/в тюрьме)
    """Клітина в'язниця, що ув'язнює гравця на 2 ходи ( з можливістю втекти )"""

    def __init__(self):
        super().__init__()
        self.prisoner_array = dict()

    def set_free(self, player):
        print("Гравця ",player.get_name()," звільнено. Метод set_free працює")
        # видаляємо з масиву
        del self.prisoner_array[player.get_name()]
        player.set_enabled(True)
        return 1

    def get_move_main(self, prisoner):

        if prisoner.get_name() in self.prisoner_array:
                print("Метод get_move_main працює, відсижених ходів - ", self.prisoner_array[prisoner.get_name()])
                return self.prisoner_array[prisoner.get_name()]# повертаємо поточні ходи відсижені в'язнем
        else:
                print("Метод get_move_main працює")
                return -1


    def player_choice(self, action, current):  # гравець може вибрати сидіти у в'язниці або спробувати сплатити хабар ( може не спрацювати)
        print("Гравець ",current.get_name()," зробив свій вибір. Метод player_choice працює")
        value = randint(100, 600) # ася питає в гравця
        random_amount = randint(0, 1)
        if current.get_name() in self.prisoner_array:
                if action == 1:  # якщо гравець вирішив платити хабар, є шанс на те, що він попадеться
                    current.set_less_money(value)# забираємо грошу
                    if random_amount == 1:  # якщо гравець попався, то додається ще + 1 простою
                        print("Гравець",current.get_name(),"попався на хабарі і сидить далі")#до мейну
                        self.prisoner_array[current.get_name()] -= 1  # віднімається ход від поточних відсижених ходів ( тобто гравець сидить довше)
                        return 0
                    else:
                        # якщо гравець не попався, то він виходить достроково
                        print("Гравець ",current.get_name()," звільнився, заплативши хабар")#до мейну
                        return self.set_free(current)
                elif action == 2:# сидеть дальше
                    print("Гравець ",current.get_name()," вибрав сидіти далі")#до мейну
                    self.prisoner_array[current.get_name()] += 1
                    return 0
                elif action == 3:  # попытка сбежать
                    if random_amount == 1:  # якщо гравець попався, то додається ще + 1 простою
                        print("Гравець ",current.get_name()," попався при спробі втекти і сидить далі")#до мейну
                        self.prisoner_array[current.get_name()] -= 1  # віднімається ход від поточних відсижених ходів ( тобто гравець сидить довше)
                        return 0
                    else:
                        # якщо гравець не попався, то він виходить достроково
                        print("Гравець ",current.get_name()," втік")#до мейну
                        return self.set_free(current)
    def event(self,player):
        print("Викликався event в'язниця")
        prisoner = player.get_name()
        self.prisoner_array[prisoner] = 0  # додаємо у в'язницю
        player.set_enabled(False)  # ув'язнюємо
        return 0


class StartFinish(Field):  # видавати гроші необхідно і тоді, коли гравець проходить повз неї, тому це буде визначатися у гравця, але клітина має існувати
    """Клітина початку гри, що видає на кожному колі додатковий капітал"""

    def __init__(self):
        super().__init__()

    def event(self, player):
        print("Метод СтартФініш працює")
        return 1

class StrategyCasino:
    """Разділення міні-ігор на підкласи. Виконується, якщо вибір гравця - казино"""
    def getagoodbet(self,player):#Мейн
        while True:
            try:
                bet = input("Гравець, вашa ставкa: ")
                bet = int(bet)
                if bet > player.get_money():
                    print("Ставка є більшою за поточний рахунок гравця. Статки гравця ",player.get_name(),": ",player.get_money())
                elif bet <= 0:
                    print("Ваша ставка має бути більшою за 0")
                else:
                    return bet
            except ValueError:
                print("Ваша ставка має бути додатнім числом")
    def startgame(self,player):  # метод казино, що дозволяє гравцю зробити ставку
        print("Метод казино працює")
        number = randint(0, 1)
        bet = self.getagoodbet(player)
        player.set_less_money(bet) # ставка зроблена
        if number == 1:  # зарандомити число
            print("Гравець ",player.get_name()," виграв")#Мейн
            player.set_more_money(bet * 3)
            return 1
        else:
            print("Гравець ",player.get_name()," програв")#Мейн
            return 0  # гравець програв, завершити програму

class StrategyRoulette:
    """Разділення міні-ігор на підкласи. Виконується, якщо вибір гравця - рулетка"""
    def startgame(self,player):# метод рулетка, що дає можливість гравцю зіграти на великий виграш з вірогідністю померти.
        print("Метод рулетка працює")
        number = randint(0, 1)
        bet = player.get_money()# граємо на весь капітал (мертвим гроші не потрібні)
        player.set_less_money(bet)
        if number == 1:  # зарандомити число
            print("Гравець ",player.get_name(),"виграв ",bet*3,"космічних монет")#Мейн
            player.set_more_money(bet * 3)
            return 1
        else:
            print("Гравець ",player.get_name()," програв і помер")#Мейн
            player.set_died()
            return 0  # гравець програв і помер, завершити програму


class Casino(Field):# strategy паттерн -разделить мини-игры казино ( казино, рулетка) на отдельные подклассы, чтобы не загружать само казино и была возможность внедрять новые миниигры
    """Клітина казіно, що дає гравцю вибір зіграти в казино або в рулетку"""

    def __init__(self):
        super().__init__()
        self.casino = StrategyCasino()
        self.roulette = StrategyRoulette()

    def event(self, player):  # івент клітини казіно
        print("Викликався event казино")
        random_value = randint(0, 2)
        if random_value == 0:  # - якщо зарандомилася цифра 0, відправляємо гравця в казино без права відмовитися
            # вернуть число, которое означает, что выбрано казино, чтобы спросить, будет ли игрок играть или нет
            askamount = input("Граємо в казино? [1/0]: ") # мейн
            askamount = int(askamount)
            if askamount == 1:  # якщо гравець вибрав грати, відправляюємо в рулетку
                return self.casino.startgame(player)
            else:  # якщо гравець відмовився, завершити гру
                print("Гравець",player.get_name(),"відмовився")#Мейн
                return 0
        else:  # інакше відправляємо гравця в рулетку, і даємо право відмовитися
            askamount = input("Пограємо в рулетку на смерть? [1/0]: ") # мейн
            askamount = int(askamount)
            if askamount == 1:  # якщо гравець вибрав грати, відправляюємо в рулетку
                return self.roulette.startgame(player)
            else:  # якщо гравець відмовився, завершити гру
                print("Гравець",player.get_name(),"відмовився")#Мейн
                return 0

