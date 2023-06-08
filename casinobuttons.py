import tkinter as tk
from players import HumanCreator, client
from random import randint
from gamefields import Casino, Prison
from prisonbuttons import ButtonsPrison
from Configuration import Config

# кнопки казино, важный момент, что они должны как-то взаимодействовать с остальным полем (например, отказ ведет к переходу к след. игроку)
class CasinoButtons(tk.Frame):
    def __init__(self, master, casino, player):
        super().__init__(master)

        self.casino = casino
        self.player = player
        self.choice = None
        conf = Config()

        self.button_cas_play = tk.Button(self, text="Грати в казіно", command=self.playcasinoaction,
                                         width=20, height=2,
                                         bg=conf.colour_button,
                                         bd=2, relief=tk.SOLID, font=("Arial", 12), activebackground="#6600ff")
        self.button_rou_play = tk.Button(self, text="Грати в рулетку", command=self.playrouletteaction,
                                         width=20, height=2,
                                         bg=conf.colour_button,
                                         bd=2, relief=tk.SOLID, font=("Arial", 12))
        self.button_escape = tk.Button(self, text="Відмовитися", command=self.escapeaction,
                                       width=20, height=2,
                                       bg=conf.colour_button,
                                       bd=2, relief=tk.SOLID, font=("Arial", 12))

        self.button_cas_play.grid(row=0, column=0, padx=10, sticky="ew")
        self.button_rou_play.grid(row=1, column=0, padx=10, sticky="ew")
        self.button_escape.grid(row=2, column=0, padx=10, sticky="ew")

    def playcasinod(self, bet):
        result = self.casino.playcasino(self.player, bet)
        if result == "WinCasino":
            label = tk.Label(self, text="Ви виграли",  # проблема в том чтобы спрятать прошлые кнопки
                             bg="#B0B2FD",
                             fg="#010632")
            label.grid(row=0, pady=50, padx=50)
        else:
            label = tk.Label(self, text="Ви програли",
                             bg="#B0B2FD",
                             fg="#010632")
            label.grid(row=0, pady=50, padx=50)

    def playcasinoaction(self):
        conf = Config()
        button_cas_play_act10 = tk.Button(self, text="Поставити 10%",
                                          command=lambda: self.playcasinod(self.player.get_money() * 0.1),
                                          width=20, height=2,
                                          bg=conf.colour_button, bd=2, relief=tk.SOLID, font=(conf.font,conf.font_size),)

        button_cas_play_act20 = tk.Button(self, text="Поставити 20%",
                                          command=lambda: self.playcasinod(self.player.get_money() * 0.2),
                                          width=20, height=2,
                                          bg=conf.colour_button, bd=2, relief=tk.SOLID, font=(conf.font,conf.font_size),)

        button_cas_play_act50 = tk.Button(self, text="Поставити 50%",
                                          command=lambda: self.playcasinod(self.player.get_money() * 0.5),
                                          width=20, height=2,
                                          bg=conf.colour_button, bd=2, relief=tk.SOLID, font=(conf.font,conf.font_size),)

        button_cas_play_act10.grid(row=0, column=0, padx=10, sticky="ew")
        button_cas_play_act20.grid(row=1, column=0, padx=10, sticky="ew")
        button_cas_play_act50.grid(row=2, column=0, padx=10, sticky="ew")
        return 0

    def playrouletteaction(self):
        self.casino.playroulette(self.player)
        self.destroy()

    def escapeaction(self):
        print("гравець звільнився")
        self.destroy()
        # ход следующего игрока


# player1 = client(HumanCreator(), "name")
# casino1 = Casino()
# root = tk.Tk()
# root.geometry("400x300")
#
# frame_left = tk.Frame(root)
# frame_left.pack(side=tk.LEFT, padx=10, pady=10)
#
# frame_right = tk.Frame(root)
# frame_right.pack(side=tk.LEFT, padx=10, pady=10)
#
# buttons = CasinoButtons(frame_right, casino1, player1)
# buttons.pack()
#
# root.mainloop()
#
# print(player1.get_money())
# print(player1.get_enabled())
