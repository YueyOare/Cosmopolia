from tkinter import *
import tkinter.font as tkfont
from PlanetChance import *
from gamefields import *
from map import *
from players import *


class GameGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Гра")
        self.root.geometry("400x400")
        self.root.configure(bg="#B0B2FD")

        self.custom_font = tkfont.Font(family="Comic Sans MS", size=12)

        self.result_text = StringVar()
        self.result_label = Label(self.root, textvariable=self.result_text, font=self.custom_font, bg="#B0B2FD")
        self.result_label.pack(pady=50)

    def switch_first(self, ev):
        self.word = ev
        if self.word == "Casino":
            if self.player.get_is_human():
                self.bid = int(input("Ви на клітинці Казино. Виберіть ставку: "))
            else:
                self.bid = self.player.take_action(1, self.player.get_money())
            while True:
                if self.bid > 0 and self.bid <= self.player.get_money():
                    game = StrategyCasino()
                    res = game.startgame(self.player, self.bid)
                    self.switch_second(res)
                    break
                print("Ставка некоректна. Гравець ", self.player.get_name(), " має таку суму грошей: ", self.player.get_money())
                self.bid = int(input("Виберіть ставку: "))
        elif self.word == "Free":
            self.result_text.set("Гравця Ім'я було звільнено зі в'язниці")
        elif self.word == "Teleport":
            self.result_text.set("Ви попали на клітинку Телепорт. Ваша нова позиція: Кількість грошей")
        elif self.word == "Imprisoned":
            self.result_text.set("На жаль, ви потрапили до в'язниці")
        elif self.word == "StartFinish":
            self.result_text.set("Ви потрапили на клітинку Старт/Фініш")
        elif self.word == "Roulette":
            while True:
                if self.player.get_is_human():
                    answer = int(input("Ви потрапили на клітинку Рулетка. Чи хочете зіграти на своє життя? 1 - Так, 0 - Ні"))
                else:
                    answer = self.player.take_action(0, 1)
                    if answer:
                        print("Гравець", self.player.get_name(), "обрав зіграти в рулетку")
                    else:
                        print("Гравець", self.player.get_name(), "обрав не грати в рулетку")
                if answer == 1:
                    game = StrategyRoulette()
                    res = game.startgame(self.player)
                    self.switch_second(res)
                    break
                elif answer == 0:
                    break
        elif self.word == "player must pay":
            self.result_text.set("Ви потрапили на чуже поле, тому повинні заплатити аренду")
            payment = System().Planet()
            re = payment.pay(self.player)
            if re == "Player does not have enough money to pay":
                self.result_text.set("Недостатньо грошей для сплати")
            elif re == "Player pay rent":
                self.result_text.set("Гравець вдало сплатив аренду")
        elif self.word == "player can buy":
            while True:
                if self.player.get_is_human():
                    answer = int(input("Ви потрапили на вільне поле, чи хочете його купити? 1 - так, 0 - ні: "))
                else:
                    answer = self.player.take_action(0, 1)
                    if answer:
                        print("Гравець", self.player.get_name(), "обрав купити поле")
                    else:
                        print("Гравець", self.player.get_name(), "обрав не купувати поле")
                if answer == 1:
                    payment = System().Planet()
                    re = payment.buy(self.player)
                    if re == "Player does not have enough money to buy":
                        self.result_text.set("Недостатньо грошей для покупки")
                    elif re == "Player buy planet":
                        self.result_text.set("Покупка завершена")
                    break
                elif answer == 0:
                    break
        elif self.word == "player is in his field":
            self.result_text.set("Ви потрапили на своє поле")

    def switch_second(self, res):
        self.word = res
        if self.word == "WinCasino":
            self.result_text.set("Перемога. Гравець Ім'я виграв Кількість грошей, тепер має таку суму грошей: Кількість грошей")
        elif self.word == "LoseCasino":
            self.result_text.set("Програш. Гравець Ім'я програв Кількість грошей, залишок: Кількість грошей")
        elif self.word == "WinRoulette":
            self.result_text.set("Перемога. Гравець Ім'я тепер має таку суму грошей: Кількість грошей")
        elif self.word == "LoseRoulette":
            self.result_text.set("Програш. Гравець Ім'я помер :)")

    def run(self):
        self.root.mainloop()

game = GameGUI()
game.switch_first("Casino")
game.run()
