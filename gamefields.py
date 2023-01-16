from random import randint
from fields import Field
class Teleport(Field):
    """Клітина телепорт, що телепортує гравця до рандомної точки"""

    def __init__(self):
        super().__init__()

    # витягнути з мепу телепорти, щоб телепортувати гравця в рандомну клітину типу "телепорт"

    def event(self, player):
        randomvalue = randint(0, 9)
        print("Метод Телепорт працює")
        player.set_current_field(randomvalue)
        return 1


class Prison(Field): # state патерн - сможем разделить состояние игрока (свободен/в тюрьме)
    """Клітина в'язниця, що ув'язнює гравця на 2 ходи ( з можливістю втекти )"""

    def __init__(self):
        super().__init__()

    # уточнити, чи є необхідність в додатковому контейнері для гравця ( поточна кількість ходів, що має бути відсижена у в'язниці і т.д)
    prisoner_array = []

    def set_free(self, player, prisoner_index):
        print("Гравця звільнено. Метод set_free працює")
        # видаляємо з масиву
        player.set_enabled(True)
        return 0

    def get_move_main(self, prisoner):
        print("Метод get_move_main працює")
        return 1

    def player_choice(self, action, prisoner):  # гравець може вибрати сидіти у в'язниці або спробувати сплатити хабар ( може не спрацювати)
        print("Гравець зробив свій вибір. Метод player_choice працює")
        choice = randint(0, 2)
        value = randint(100, 600)
        random_amount = randint(0, 2)
        prisoner_index = 0
        # перевіряємо поточний хід (скільки залишилося у в'язниці ?  цикл ?)
        for player in self.prisoner_array:  # проходимо по масиву ув'язнених, перевіряючи, чи є даний гравець у в'язниці
            if player == prisoner:  # problem !!!!!!! якщо знайшли, що гравець у в'язниці, виконуємо наступні дії

                if action == 1:  # якщо гравець вирішив платити хабар, є шанс на те, що він попадеться
                    # player.set_less_money(value) забираємо грошу
                    if random_amount == 1:  # якщо гравець попався, то додається ще + 1 простою
                        print("Гравець попався на хабарі і сидить далі")
                        self.prisoner_array[prisoner_index] -= 1  # віднімається ход від поточних відсижених ходів ( тобто гравець сидить довше)
                        return 1
                    else:
                        # якщо гравець не попався, то він виходить достроково
                        print("Гравець звільнився, заплативши хабар")
                        return self.set_free(player, prisoner_index)
                elif action == 2:
                    # сидеть дальше
                    print("Гравець вибрав сидіти далі")
                    self.prisoner_array[prisoner_index] += 1
                    return 1
                else:  # с6ежать
                    if random_amount == 1:  # якщо гравець попався, то додається ще + 1 простою
                        print("Гравець попався при спробі втекти і сидить далі")
                        self.prisoner_array[prisoner_index] -= 1  # віднімається ход від поточних відсижених ходів ( тобто гравець сидить довше)
                        return 1
                    else:
                        # якщо гравець не попався, то він виходить достроково
                        print("Гравець втік")
                        return self.set_free(player, prisoner_index)

        # просто продовжити ?

    def event(self, prisoner):  # !!! уточнити, чи необхідно player ?
        print("Викликався event в'язниця")
        self.prisoner_array.append({prisoner.get_name(),0})  # додаємо у в'язницю, якщо гравця нема
        prisoner.set_enabled(False)  # ув'язнюємо
        return 1


class StartFinish(Field):  # видавати гроші необхідно і тоді, коли гравець проходить повз неї, тому це буде визначатися у гравця, але клітина має існувати
    """Клітина початку гри, що видає на кожному колі додатковий капітал"""

    def __init__(self):
        super().__init__()

    def event(self, player):
        print("Метод СтартФініш працює")
        return 1

class StrategyCasino:
    """Разділення міні-ігор на підкласи. Виконується, якщо вибір гравця - казино"""
    def getagoodbet(self,player):
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
        number = randint(0, 2)
        bet = self.getagoodbet(player)
        player.set_less_money(bet) # ставка зроблена
        if number == 1:  # зарандомити число
            print("Гравець ",player.get_name()," виграв")
            player.set_more_money(bet * 3)
            return 1
        else:
            print("Гравець ",player.get_name()," програв")
            return 1  # гравець програв, завершити програму

class StrategyRoulette:
    """Разділення міні-ігор на підкласи. Виконується, якщо вибір гравця - рулетка"""
    def startgame(self,player):# метод рулетка, що дає можливість гравцю зіграти на великий виграш з вірогідністю померти.
        print("Метод рулетка працює")
        number = randint(0, 2)
        bet = player.get_money()# граємо на весь капітал (мертвим гроші не потрібні)
        player.set_less_money(bet)
        if number == 1:  # зарандомити число
            print("Гравець ",player.get_name(),"виграв ",bet*3,"космічних монет")
            player.set_more_money(bet * 3)
            return 1
        else:
            print("Гравець ",player.get_name()," програв і помер")
            player.set_died()
            return 1  # гравець програв і помер, завершити програму


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
            askamount = input("Граємо в казино? [1/0]: ")
            askamount = int(askamount)
            if askamount == 1:  # якщо гравець вибрав грати, відправляюємо в рулетку
                return self.casino.startgame(player)
            else:  # якщо гравець відмовився, завершити гру
                print("Гравець",player.get_name(),"відмовився")
                return 1
        else:  # інакше відправляємо гравця в рулетку, і даємо право відмовитися
            askamount = input("Пограємо в рулетку на смерть? [1/0]: ")
            askamount = int(askamount)
            if askamount == 1:  # якщо гравець вибрав грати, відправляюємо в рулетку
                return self.roulette.startgame(player)
            else:  # якщо гравець відмовився, завершити гру
                print("Гравець",player.get_name(),"відмовився")
                return 1