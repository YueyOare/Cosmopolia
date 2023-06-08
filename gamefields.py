import random
from random import randint
from fields import Field


class Teleport(Field):
    """Клітина телепорт, що телепортує гравця до рандомної точки"""

    def __init__(self):
        super().__init__()

    def event(self, player):
        randomvalue = randint(0, 9)  # поменять для конфига
        if random.choice([True, False]):
            player.move_to(randomvalue)
        else:
            player.move_to(-randomvalue)
        return "Teleport"


class Prison(Field):
    """Клітина в'язниця, що ув'язнює гравця на 2 ходи (з можливістю втекти)"""

    def __init__(self):
        super().__init__()
        self.prisoner_array = dict()

    def set_free(self, player):
        # видаляємо з масиву
        player.set_enabled(1)
        del self.prisoner_array[player.get_name()]
        return 1  # повертаю 1 - значить, що гравця звільнено

    def get_move_main(self, prisoner):

        if prisoner.get_name() in self.prisoner_array:
            return self.prisoner_array[prisoner.get_name()]  # повертаємо поточні ходи відсиджені в'язнем
        else:
            return -1  # повертаю -1 якщо є помилка знаходження гравця за ключем

    def player_choice(self, action, player):  # гравець може вибрати сидіти у в'язниці або спробувати сплатити хабар
        value = 500  # ася питає в гравця (або так і залишаємо рандом, але не більше за статок)
        random_amount = randint(0, 1)
        if player.get_name() in self.prisoner_array:
            if action == 1:  # якщо гравець вирішив платити хабар, є шанс на те, що він попадеться
                if value >= player.get_money():
                    return 0
                else:
                    player.set_less_money(value)  # забираємо грошу
                    if random_amount == 1:  # якщо гравець попався, то додається ще + 1 простою
                        self.prisoner_array[player.get_name()] -= 1  # гравець сидить довше
                        return 0  # повертаю 0 - гравець сидить
                    else:
                        # якщо гравець не попався, то він виходить достроково
                        return self.set_free(player)
            elif action == 2:  # сидіти далі
                self.prisoner_array[player.get_name()] += 1
                return 0  # повертаю 0 - гравець сидить
            elif action == 3:  # спроба втекти
                if random_amount == 1:  # якщо гравець попався, то додається ще + 1 простою
                    self.prisoner_array[player.get_name()] -= 1  # гравець сидить довше
                    return 0  # повертаю 0 - гравець сидить
                else:
                    self.set_free(player)  # якщо гравець не попався, то він виходить достроково

    def event(self, player):
        prisoner = player.get_name()
        self.prisoner_array[prisoner] = 0  # додаємо у в'язницю
        player.set_enabled(0)  # ув'язнюємо
        return "Imprisoned"


class StartFinish(Field):  # клітина має існувати, з неї починається гра, після її проходження видаємо гроші
    """Клітина початку гри, що видає на кожному колі додатковий капітал"""

    # важливе зауваження, що гравець отримує гроші за проходження кола, навіть не потрапляючи на цю клітину
    def __init__(self):
        super().__init__()

    def event(self, player):
        return "StartFinish"


class StrategyCasino:
    """Розділяємо мініігри на підкласи. Виконується, якщо вибір гравця - казино"""

    def startgame(self, player, bet, ):  # метод казино, що дозволяє гравцю зробити ставку
        print("Метод казино працює")
        number = randint(0, 1)
        player.set_less_money(bet)  # ставка зроблена
        if number == 1:  # рандомне число
            player.set_more_money(bet * 3)
            # отсюда можно сделать вызов новых кнопок..?
            return "WinCasino"
        else:
            return "LoseCasino"  # гравець програв, завершити програму


class StrategyRoulette:
    """Розділення мініігор на підкласи. Виконується, якщо вибір гравця - рулетка"""

    def startgame(self, player):  # метод рулетка, що дає можливість гравцю зіграти на великий виграш
        number = randint(0, 1)
        bet = player.get_money()  # граємо на весь капітал (мертвим гроші не потрібні)
        player.set_less_money(bet)
        if number == 1:  # рандомне число
            player.set_more_money(bet * 3)
            return "WinRoulette"
        else:
            player.set_died()
            return "LoseRoulette"  # гравець програв і помер, завершити програму


class Casino(Field):  # strategy паттерн
    """Клітина казино, що дає гравцю вибір зіграти в казино або в рулетку"""

    def __init__(self):
        super().__init__()
        self.casino = StrategyCasino()
        self.roulette = StrategyRoulette()

    def playcasino(self, player, bet):
        self.casino.startgame(player, bet)

    def playroulette(self, player):
        self.roulette.startgame(player)

    def event(self, player):  # івент клітини казино
        random_value = randint(0, 2)
        if random_value == 0:  # - якщо рандом цифра 0, відправляємо гравця в казино без права відмовитися
            return "Casino"  # !!! SWITCH !!!!повертаю мейну, що значить, що гравець потрапив у казино
        # і необхідно спитати в нього чи буде він грати, а потім спитати ставку
        else:  # інакше відправляємо гравця в рулетку, і даємо право відмовитися
            return "Roulette"  # повертаю мейну, що значить, що гравець потрапив у рулетку
