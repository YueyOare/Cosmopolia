import tkinter.font as tkfont
import tkinter as tk
from map_gui import MapGUI
from Configuration import Config
from players import *

config = Config()
general_map = None


class StartMenuGUI:
    def __init__(self, parent, button1, button2):
        self.parent = parent
        self.parent.configure(bg=config.colour_background)
        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)
        self.custom_font = tkfont.Font(family="Comic Sans MS", size=20)
        self.button_font = tkfont.Font(family="Comic Sans MS", size=16, weight="bold")
        self.heading_font = tkfont.Font(family="Comic Sans MS", size=64, weight="bold")

        self.label1 = tk.Label(self.parent, text="Cosmopolia", bg=config.colour_background, font=self.heading_font,
                               fg=config.colour_text)
        self.label1.grid(row=0, pady=50, sticky="nsew")  # Center label horizontally and vertically

        self.button1 = tk.Button(self.parent, text="Розпочати гру", command=button1, font=self.button_font,
                                 bg=config.colour_button,
                                 fg=config.colour_text, relief=tk.RAISED)
        self.button1.grid(row=1, pady=20)  # Center button horizontally

        self.button2 = tk.Button(self.parent, text="Вийти", command=button2, font=self.button_font,
                                 bg=config.colour_button,
                                 fg=config.colour_text, relief=tk.RAISED)
        self.button2.grid(row=2, pady=20)  # Center button horizontally


class PlayerCreationGUI:
    def __init__(self, parent1, parent2):
        self.humans = None
        self.entrys = None
        self.label3 = None
        self.parent1 = parent1
        self.parent2 = parent2
        self.Amount_of_Players = 0
        self.Players = []
        self.current_player = 1

        self.parent1.grid_rowconfigure(0, weight=1)
        self.parent1.grid_rowconfigure(1, weight=1)
        self.parent1.grid_rowconfigure(2, weight=1)
        self.parent1.grid_columnconfigure(0, weight=1)
        self.parent1.grid_columnconfigure(1, weight=1)
        self.parent1.grid_columnconfigure(2, weight=1)
        self.parent2.grid_rowconfigure(0, weight=1)
        self.parent2.grid_columnconfigure(0, weight=2)
        self.parent2.grid_columnconfigure(1, weight=1)
        self.parent2.grid_columnconfigure(2, weight=1)
        self.parent1.configure(bg=config.colour_background)
        self.parent2.configure(bg=config.colour_background)

        self.custom_font = tkfont.Font(family="Comic Sans MS", size=20)
        self.button_font = tkfont.Font(family="Comic Sans MS", size=16)
        self.heading_font = tkfont.Font(family="Comic Sans MS", size=24)

        self.label2 = tk.Label(self.parent1, text="Введіть загальну кількість гравців:", bg=config.colour_background,
                               font=self.heading_font,
                               fg=config.colour_text)
        self.label2.grid(row=0, column=0, columnspan=3, pady=50, padx=50, sticky="nsew")

        self.button3 = tk.Button(self.parent1, text="2 гравці", command=lambda: self.create_players(2),
                                 font=self.button_font, bg=config.colour_button,
                                 fg=config.colour_text, relief=tk.RAISED)
        self.button3.grid(row=1, column=0, padx=20)

        self.button4 = tk.Button(self.parent1, text="3 гравці", command=lambda: self.create_players(3),
                                 font=self.button_font, bg=config.colour_button,
                                 fg=config.colour_text, relief=tk.RAISED)
        self.button4.grid(row=1, column=1, padx=20)

        self.button5 = tk.Button(self.parent1, text="4 гравці", command=lambda: self.create_players(4),
                                 font=self.button_font, bg=config.colour_button,
                                 fg=config.colour_text, relief=tk.RAISED)
        self.button5.grid(row=1, column=2, padx=20)

        self.back_button = tk.Button(self.parent1, text="Назад", command=back_to_menu, font=self.button_font,
                                     bg=config.colour_button, fg=config.colour_text, relief=tk.RAISED)
        self.back_button.grid(row=2, column=0, columnspan=3, pady=50)

    def create_players(self, num_players):
        self.Amount_of_Players = num_players

        for widget in self.parent2.winfo_children():
            widget.destroy()

        self.parent1.grid_forget()
        self.label3 = tk.Label(self.parent2, text="Введіть імена гравців та оберіть, людина вони чи бот",
                               bg=config.colour_background,
                               font=self.heading_font,
                               fg=config.colour_text)
        self.label3.grid(row=0, column=0, columnspan=3, pady=50, padx=50)
        self.entrys = []
        self.humans = [0 for i in range(self.Amount_of_Players)]
        for i in range(self.Amount_of_Players):
            name_entry = tk.Entry(self.parent2, font=self.custom_font)
            self.entrys.append(name_entry)
            name_entry.grid(row=i + 1, column=0, padx=20)
            human_button = tk.Button(self.parent2, text="Гравець людина", command=lambda i=i: self.set_player(1, i),
                                     font=self.button_font, bg=config.colour_button, fg=config.colour_text,
                                     relief=tk.RAISED, bd=3, padx=10,
                                     pady=5, borderwidth=2, highlightthickness=0, activebackground="#010632")
            human_button.grid(row=i + 1, column=1, padx=10)

            bot_button = tk.Button(self.parent2, text="Гравець бот", command=lambda i=i: self.set_player(0, i),
                                   font=self.button_font, bg=config.colour_button, fg=config.colour_text,
                                   relief=tk.RAISED, bd=3, padx=10,
                                   pady=5, borderwidth=2, highlightthickness=0, activebackground="#010632")
            bot_button.grid(row=i + 1, column=2, padx=10)

        back_button = tk.Button(self.parent2, text="Назад", command=self.back_to_menu, font=self.button_font,
                                bg=config.colour_button, fg=config.colour_text, relief=tk.RAISED)
        back_button.grid(row=self.Amount_of_Players + 1, column=0, pady=50, columnspan=3)

        start_button = tk.Button(self.parent2, text="Розпочати гру", command=self.add_players, font=self.button_font,
                                 bg=config.colour_button, fg=config.colour_text, relief=tk.RAISED)
        start_button.grid(row=self.Amount_of_Players + 2, column=0, pady=10, columnspan=3)
        self.parent2.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="nsew")

    def set_player(self, is_human, n):
        self.humans[n] = is_human

    def back_to_menu(self):
        self.parent2.grid_forget()
        self.parent1.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="nsew")

    def add_players(self):
        general_map.players_amount = self.Amount_of_Players
        general_map.star_image_tk_arr = [None for i in range(self.Amount_of_Players)]
        general_map.players_positions = [0 for i in range(self.Amount_of_Players)]
        for i in range(self.Amount_of_Players):
            name = self.entrys[i].get()
            if not name:
                return
            general_map.players.append(create_player(name, self.humans[i]))
        main_game()


def back_to_menu():
    frame2.grid_forget()
    frame1.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="nsew")


def switch_to_frame2():
    global general_map
    frame1.grid_forget()
    frame2.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="nsew")
    general_map = create_map(frame8)


def quit():
    root.quit()
    root.destroy()
    return


def start_menu():
    global general_map
    del general_map
    for widget in frame8.winfo_children():
        widget.destroy()
    frame1.grid_forget()
    frame2.grid_forget()
    frame3.grid_forget()
    frame4.grid_forget()
    frame5.grid_forget()
    frame6.grid_forget()
    frame7.grid_forget()
    frame8.grid_forget()
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    frame1.grid(row=0, column=0, rowspan=4, columnspan=2, sticky="nsew")


def create_map(frame):
    return MapGUI(frame, 25)


root = tk.Tk()
root.geometry("800x500")
root.configure(bg=config.colour_background)
# root.configure(bg="white")
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

left_width = window_width // 2
left_height = window_height

frame1 = tk.Frame(root, bg=config.colour_background)
frame2 = tk.Frame(root, bg=config.colour_background)
frame3 = tk.Frame(root, bg=config.colour_background)
frame4 = tk.Frame(root, width=left_width * 0.25, height=left_height * 0.25, bg="red")
frame5 = tk.Frame(root, width=left_width * 0.25, height=left_height * 0.25, bg="green")
frame6 = tk.Frame(root, width=left_width * 0.25, height=left_height * 0.25, bg="blue")
frame7 = tk.Frame(root, width=left_width * 0.25, height=left_height * 0.25, bg="yellow")
frame8 = tk.Frame(root, bg=config.colour_background)
menu = StartMenuGUI(frame1, switch_to_frame2, quit)
players_creation = PlayerCreationGUI(frame2, frame3)
start_menu()


def main_game():
    frame1.grid_forget()
    frame2.grid_forget()
    frame3.grid_forget()
    frame4.grid_forget()
    frame5.grid_forget()
    frame6.grid_forget()
    frame7.grid_forget()
    frame8.grid_forget()
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    frame4.grid(row=0, column=0, sticky="nsew")
    frame5.grid(row=1, column=0, sticky="nsew")
    frame6.grid(row=2, column=0, sticky="nsew")
    frame7.grid(row=3, column=0, sticky="nsew")
    frame8.grid(row=0, column=1, rowspan=4, sticky="nsew")
    back_button3 = tk.Button(frame4, text="Повернутися", command=start_menu, font=("Arial", 12), bg="white", fg="black")
    back_button3.grid(row=0, column=0, sticky="nsew")
    button4 = tk.Button(frame5, text="Кинути кубик", command=general_map.move_star, font=("Arial", 12), bg="white",
                        fg="black")
    button4.grid(row=0, column=0, sticky="nsew")


root.mainloop()
