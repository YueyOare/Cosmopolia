import tkinter as tk
from Configuration import Config
from players import HumanCreator, client
from random import randint
from gamefields import Prison

# кнопки тюрьмы, ситуация как и с казино, необходима связь с стартом ..?
class ButtonsPrison(tk.Frame):
    def __init__(self, master, prison1, player):
        super().__init__(master)
        self.prison = prison1
        self.player = player
        self.choice = None
        conf = Config()

        self.button_pr_wait = tk.Button(self, text="Чекати", command=self.wait_action,
                                        width=15, height=1,
                                        bg=conf.colour_button,
                                        bd=2, relief=tk.SOLID, font=(conf.font, conf.font_size))
        self.button_pr_escape = tk.Button(self, text="Втекти", command=self.escape_action,
                                          width=15, height=1,
                                          bg=conf.colour_button,
                                          bd=2, relief=tk.SOLID, font=(conf.font, conf.font_size))
        self.button_pr_pay = tk.Button(self, text="Заплатити хабар", command=self.pay_action,
                                       width=15, height=1,
                                       bg=conf.colour_button,
                                       bd=2, relief=tk.SOLID, font=(conf.font, conf.font_size))

        self.button_pr_wait.grid(row=0, column=0, padx=10, sticky="ew")
        self.button_pr_escape.grid(row=1, column=0, padx=10, sticky="ew")
        self.button_pr_pay.grid(row=2, column=0, padx=10, sticky="ew")

    def wait_action(self):
        self.choice = "wait"
        self.prison.prisoner_array[self.player.get_name()] += 1
        print("гравець чекає")  # запустить ход следующего игрока или передать сигнал об єтом
        # self.destroy()
        return 0  # повертаю 0 - гравець сидить

    def escape_action(self):
        self.choice = "escape"
        random_amount = randint(0, 1)
        if random_amount == 1:
            self.prison.prisoner_array[self.player.get_name()] -= 1
            print("гравець попався")  # запустить ход следующего игрока
            # self.destroy()
            return 0
        else:
            print("гравець звільнився")
            self.prison.set_free(self.player)  # запустить ход этого игрока
            self.destroy()

    def pay_action(self):
        self.choice = "pay"
        value = 50
        random_amount = randint(0, 1)
        if value >= self.player.get_money():
            print("мало грошей")  # запустить ход следующего игрока
            return 0
        else:
            self.player.set_less_money(value)  # забираємо грошу
            if random_amount == 1:  # якщо гравець попався, то додається ще + 1 простою
                self.prison.prisoner_array[self.player.get_name()] -= 1  # гравець сидить довше
                print("гравець попався")  # запустить ход следующего игрока
                return 0  # повертаю 0 - гравець сидить
            else:
                # якщо гравець не попався, то він виходить достроково
                print("гравець звільнився")  # запустить ход этого игрока
                self.destroy()

    def start_prison(self, frame, player, prison):
        buttons = ButtonsPrison(frame, prison, player)
        buttons.grid(row=0, column=0, padx=10, sticky="ew")


# player1 = client(HumanCreator(), "name")
# prison = Prison()
# prison.event(player1)
# root = tk.Tk()
# frame_right = tk.Frame(root)
#
# ButtonsPrison(frame_right, prison, player1).start_prison(frame_right, player1, prison)
# frame_right.pack()
# root.mainloop()

# print(player1.get_enabled())
#
#
# root.geometry("400x300")
#
# frame_left = tk.Frame(root)
# frame_left.pack(side=tk.LEFT, padx=10, pady=10)
#
#
# frame_right.pack(side=tk.LEFT, padx=10, pady=10)
#
# buttons = ButtonsPrison(frame_right, prison, player1)
# buttons.pack()
#
# root.mainloop()
#
# print(player1.get_money())
# print(player1.get_enabled())
