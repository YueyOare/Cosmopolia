from tkinter import *
import tkinter.font as tkfont


class PlayerCreationGUI:
    def __init__(self, root):
        self.root = root
        self.Amount_of_Players = 0
        self.Players = []
        self.current_player = 1

        self.root.configure(bg="#B0B2FD")

        self.custom_font = tkfont.Font(family="Comic Sans MS", size=20)
        self.button_font = tkfont.Font(family="Comic Sans MS", size=16, weight="bold")
        self.heading_font = tkfont.Font(family="Comic Sans MS", size=24, weight="bold")

        self.label = Label(self.root, text="Введіть загальну кількість гравців:", bg="#B0B2FD", font=self.heading_font,
                           fg="#010632")
        self.label.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.entry = Entry(self.root, font=self.custom_font)
        self.entry.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.button = Button(self.root, text="Далі", command=self.create_players, font=self.button_font, bg="#010632",
                             fg="white", relief=RAISED)
        self.button.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.root.mainloop()

    def create_players(self):
        self.Amount_of_Players = int(self.entry.get())

        self.label.destroy()
        self.entry.destroy()
        self.button.destroy()

        self.create_player()

    def create_player(self):
        if self.current_player > self.Amount_of_Players:
            self.display_players()
            return

        if hasattr(self, 'player_label'):
            self.player_label.destroy()
            self.name_entry.destroy()

        self.player_label = Label(self.root, text=f"Введіть ім'я гравця {self.current_player}:", bg="#B0B2FD",
                                  font=self.heading_font, fg="#010632")
        self.player_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.name_entry = Entry(self.root, font=self.custom_font)
        self.name_entry.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.create_player_buttons()

    def create_player_buttons(self):
        if hasattr(self, 'human_button'):
            self.human_button.destroy()
            self.bot_button.destroy()

        button_frame = Frame(self.root, bg="#B0B2FD")
        button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.human_button = Button(button_frame, text="Гравець людина", command=lambda: self.add_player(True),
                                   font=self.button_font, bg="#010632", fg="white", relief=RAISED, bd=3, padx=10,
                                   pady=5, borderwidth=2, highlightthickness=0, activebackground="#010632")
        self.human_button.pack(side=LEFT, padx=10)

        self.bot_button = Button(button_frame, text="Гравець бот", command=lambda: self.add_player(False),
                                 font=self.button_font, bg="#010632", fg="white", relief=RAISED, bd=3, padx=10, pady=5,
                                 borderwidth=2, highlightthickness=0, activebackground="#010632")
        self.bot_button.pack(side=LEFT, padx=10)

    def add_player(self, is_human):
        name = self.name_entry.get()

        if not name:
            return

        self.Players.append((name, is_human))
        self.current_player += 1
        self.create_player()

    def display_players(self):
        if hasattr(self, 'player_label'):
            self.player_label.destroy()
            self.name_entry.destroy()

        if hasattr(self, 'human_button'):
            self.human_button.destroy()
            self.bot_button.destroy()

        players_text = "\n".join([f"Гравець {i + 1}: {player[0]} - {'Людина' if player[1] else 'Бот'}" for i, player in
                                  enumerate(self.Players)])

        self.players_label = Label(self.root, text=players_text, bg="#B0B2FD", font=self.custom_font, fg="black")
        self.players_label.place(relx=0.5, rely=0.5, anchor=CENTER)

