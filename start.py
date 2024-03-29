import random
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
        self.humans = [1 for i in range(self.Amount_of_Players)]
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
root.title("Cosmopolia")
root.configure(bg=config.colour_background)
# root.configure(bg="white")
window_width = root.winfo_screenwidth()
window_height = root.winfo_screenheight()

left_width = window_width // 2
left_height = window_height

frame1 = tk.Frame(root, bg=config.colour_background)
frame2 = tk.Frame(root, bg=config.colour_background)
frame3 = tk.Frame(root, bg=config.colour_background)
frame4 = tk.Frame(root, width=left_width * 0.25, height=left_height * 0.25, bg=config.colour_background)
frame5 = tk.Frame(root, width=left_width * 0.25, height=left_height * 0.25, bg=config.colour_background)
frame6 = tk.Frame(root, width=left_width * 0.25, height=left_height * 0.25, bg=config.colour_frame3)
frame7 = tk.Frame(root, width=left_width * 0.25, height=left_height * 0.25, bg=config.colour_background)
frame8 = tk.Frame(root, bg=config.colour_background)
menu = StartMenuGUI(frame1, switch_to_frame2, quit)
players_creation = PlayerCreationGUI(frame2, frame3)
start_menu()

current_buttons = []


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
    frame4.grid_rowconfigure(0, weight=1)
    frame4.grid_columnconfigure(0, weight=1)
    frame4.grid_columnconfigure(1, weight=1)
    frame4.grid_columnconfigure(2, weight=1)
    frame6.grid_rowconfigure(0, weight=1)
    frame6.grid_rowconfigure(1, weight=1)
    frame4.grid(row=0, column=0, sticky="nsew")
    frame5.grid(row=1, column=0, sticky="nsew")
    frame6.grid(row=2, column=0, sticky="nsew")
    frame7.grid(row=3, column=0, sticky="nsew")
    frame8.grid(row=0, column=1, rowspan=4, sticky="nsew")
    back_button3 = tk.Button(frame4, text="Повернутися", command=start_menu, font=(config.font, config.font_size),
                             bg=config.colour_button, fg=config.colour_text)
    back_button3.grid(row=0, column=0)
    label0 = tk.Label(frame5, text="",
                      bg=config.colour_background,
                      fg=config.colour_text)
    label0.grid(row=0, column=1, sticky="nsew")
    label1 = tk.Label(frame6, text="Гра починається",
                      bg=config.colour_frame3,
                      fg=config.colour_frame3_text,
                      font=(config.font, config.font_size))
    label1.grid(row=0, column=0, sticky="nsew")
    label2 = tk.Label(frame6, text="",
                      bg=config.colour_frame3,
                      fg=config.colour_frame3_text,
                      font=(config.font, config.font_size))
    label2.grid(row=1, column=0, sticky="nsew")
    label_player = tk.Label(frame4, text="",
                            bg=config.colour_background,
                            fg=config.colour_text)
    label_player.grid(row=0, column=1, sticky="nsew")
    label_player_money = tk.Label(frame4, text="",
                                  bg=config.colour_background,
                                  fg=config.colour_text)
    label_player_money.grid(row=0, column=2, sticky="nsew")

    def hide_button_show_buttons():
        button_dice_roll.grid_forget()  # Приховуємо кнопку 1
        for i, button in enumerate(current_buttons):
            button.grid(row=i, column=0)  # Відображаємо кнопку

    def playcasinod(bet):
        hide_buttons_show_button()
        player = general_map.current_player - 1
        number = randint(0, 1)
        summ = general_map.players[player].get_money() * bet
        if number == 1:  # рандомне число
            general_map.players[player].set_more_money(summ)
            label1.configure(text="Гравець " + general_map.players[player].get_name() + "\n виграв в казіно")
            label_player_money.configure(text='Грошей: ' + str(general_map.players[player].get_money()))
            hide_buttons_show_button()
            return "WinCasino"
        else:
            general_map.players[player].set_less_money(summ)
            label1.configure(text="Гравець " + general_map.players[player].get_name() + "\n програв в казіно")
            label_player_money.configure(text='Грошей: ' + str(general_map.players[player].get_money()))
            hide_buttons_show_button()
            return "LoseCasino"  # гравець програв, завершити програму

    def playcasinoaction():
        global current_buttons
        current_buttons1 = [button_cas_play_act10, button_cas_play_act20, button_cas_play_act50]  # вибір з 3х кнопок
        button_dice_roll.grid_forget()  # Приховуємо кнопку кинути кубик
        for i, button in enumerate(current_buttons):
            button.grid_forget()  # приховуємо кнопки
        for i, button in enumerate(current_buttons1):
            button.grid(row=i, column=0)  # Відображаємо кнопки
        current_buttons = current_buttons1

    def playrouletteaction():
        hide_buttons_show_button()
        player = general_map.current_player - 1
        number = randint(0, 1)
        bet = general_map.players[player].get_money()
        general_map.players[player].set_less_money(bet)
        if number == 1:  # рандомне число
            general_map.players[player].set_more_money(bet * 3)
            label1.configure(text="Гравець " + general_map.players[player].get_name() + "\n виграв в рулетці")
            label_player_money.configure(text='Грошей: ' + str(general_map.players[player].get_money()))
            hide_buttons_show_button()
            return "WinRoulette"
        else:
            #  player.set_died() потом добавим в граф. часть
            label1.configure(
                text="Гравець " + general_map.players[player].get_name() + "\n 'застрелився' ")
            hide_buttons_show_button()  # кнопки надо убрать
            return "LoseRoulette"  # гравець програв і помер, завершити програму

    def escapeaction():
        player = general_map.current_player - 1
        label1.configure(text="Гравець " + general_map.players[player].get_name() + "\n відмовився грати\n в казіно")
        hide_buttons_show_button()

    def hide_buttons_show_button():
        for button in current_buttons:
            button.grid_forget()
        button_dice_roll.grid(row=0, column=0)

    def buy_planet():
        player = general_map.current_player - 1
        label1.configure(
            text="Гравець " + general_map.players[player].get_name() + "\n купив планету")
        general_map.map.array_Fields_in_map[general_map.players_positions[player]].buy(general_map.players[player])
        general_map.own_planet(player)
        label_player_money.configure(text='Грошей: ' + str(general_map.players[player].get_money()))
        hide_buttons_show_button()

    def refuse_to_buy_planet():
        player = general_map.current_player - 1
        label1.configure(
            text="Гравець " + general_map.players[player].get_name() + " відмовився\n купувати планету")
        hide_buttons_show_button()

    def upgrade_planet():
        player = general_map.current_player - 1
        label1.configure(
            text="Гравець " + general_map.players[player].get_name() + "\n покращив планету")
        general_map.map.array_Fields_in_map[general_map.players_positions[player]].upgrade()
        general_map.own_planet(player)
        label_player_money.configure(text='Грошей: ' + str(general_map.players[player].get_money()))
        hide_buttons_show_button()

    def refuse_to_upgrade_planet():
        player = general_map.current_player - 1
        label1.configure(
            text="Гравець " + general_map.players[player].get_name() + " відмовився\n покращувати планету")
        hide_buttons_show_button()

    def handle_button_click():  # при нажатии "бросить кубик"
        global current_buttons
        result = general_map.roll_dice()  # гравця переміщує та повертається на який тип клітини його перемістило
        label_player.configure(text="Гравець " + general_map.players[
                    general_map.current_player].get_name())
        label_player_money.configure(text='Грошей: ' + str(general_map.players[
                    general_map.current_player].get_money()))
        if result[0] != -1:
            label0.config(text="Випало: " + str(general_map.dice))
        if result[0] == 1:  # телепорт
            label1.configure(
                text="Гравця " + general_map.players[
                    general_map.current_player].get_name() + " телепортувало\n з клітини " + str(
                    result[1]) + "\n в клітину " + str(result[2]))
            label2.configure(text="")
        elif result[0] == 2:  # тюрьма первое попадание, запретить ходить
            label1.configure(
                text="Гравець " + general_map.players[
                    general_map.current_player].get_name() + " потрапив\n у тюрму, він тепер\n не може ходити")
            general_map.players[general_map.current_player].set_enabled(False)
            label2.configure(text="")
        elif result[0] == 3:  # шанс
            label1.configure(text="Вам випала подія")
            if random.randint(0, 1):
                label2.configure(text="Ви отримуєте гроші")
                general_map.players[general_map.current_player].set_more_money()
            else:
                label2.configure(text="Ви втрачаєте гроші")
                general_map.players[general_map.current_player].set_less_money()
        elif result[0] == 0:  # планета
            label2.configure(text="")
            if result[1] == 0:  # пуста планета
                label1.configure(
                    text="Гравець " + general_map.players[
                        general_map.current_player].get_name() + " потрапив\n на пусту планету\n і може її купити")
                current_buttons = [button_buy, button_refuse1]
                hide_button_show_buttons()
            elif result[1] == 1:  # чужа планета
                player = general_map.current_player
                label1.configure(
                    text="Гравець " + general_map.players[
                        player].get_name() + " потрапив\n на чужу планету\n і має сплатити\n податок")
                general_map.map.array_Fields_in_map[general_map.players_positions[player]].pay(
                    general_map.players[player])
                label_player_money.configure(text='Грошей: ' + str(general_map.players[
                            general_map.current_player].get_money()))
            elif result[1] == 2:  # своя планета
                label1.configure(
                    text="Гравець " + general_map.players[
                        general_map.current_player].get_name() + " потрапив\n на свою планету\n і може її\n покращити")
                current_buttons = [button_upgrade, button_refuse2]
                hide_button_show_buttons()

        elif result[0] == 4:  # казіно
            label1.configure(
                text="Гравець " + general_map.players[general_map.current_player].get_name() + "\n потрапив у казіно")
            label2.configure(text="")
            current_buttons = [button_cas_play, button_rou_play, button_escape]
            hide_button_show_buttons()
        # если следующий игрок не может ходить, мы его выпускаем, ход выдаем следующему. он сидеть будет 1 ход
        general_map.current_player += 1
        general_map.current_player %= general_map.players_amount
        # спосіб не давати робити хід гравцю у тюрмі, але тоді ламається логіка там, де юзається general_map.current_player - 1
        # while not general_map.players[general_map.current_player].get_enabled():
        #     general_map.players[general_map.current_player].set_enabled(True)
        #     general_map.current_player += 1
        #     general_map.current_player %= general_map.players_amount

    button_dice_roll = tk.Button(frame5, text="Кинути кубик", command=handle_button_click,
                                 font=(config.font, config.font_size),
                                 bg=config.colour_button, fg=config.colour_text)
    button_dice_roll.grid(row=0, column=0, sticky="nsew")
    button_buy = tk.Button(frame5, text="Купити планету", command=buy_planet,
                           font=(config.font, config.font_size),
                           bg=config.colour_button, fg=config.colour_text)
    button_refuse1 = tk.Button(frame5, text="Відмовитись", command=refuse_to_buy_planet,
                               font=(config.font, config.font_size),
                               bg=config.colour_button, fg=config.colour_text)
    button_upgrade = tk.Button(frame5, text="Покращити планету", command=upgrade_planet,
                               font=(config.font, config.font_size),
                               bg=config.colour_button, fg=config.colour_text)
    button_refuse2 = tk.Button(frame5, text="Відмовитись", command=refuse_to_upgrade_planet,
                               font=(config.font, config.font_size),
                               bg=config.colour_button, fg=config.colour_text)

    # кнопки 1 частини казино, де гравець може зіграти в рулетку, в казино або піти геть
    button_cas_play = tk.Button(frame5, text="Грати в казіно", command=playcasinoaction,
                                bg=config.colour_button, fg=config.colour_text,
                                font=(config.font, config.font_size))
    button_rou_play = tk.Button(frame5, text="Грати в рулетку", command=playrouletteaction,
                                bg=config.colour_button, fg=config.colour_text,
                                font=(config.font, config.font_size))
    button_escape = tk.Button(frame5, text="Відмовитися", command=escapeaction,
                              bg=config.colour_button, fg=config.colour_text,
                              font=(config.font, config.font_size))

    # кнопки 2 частини казино, де гравець обирає скільки хоче поставити
    button_cas_play_act10 = tk.Button(frame5, text="Поставити 10%",
                                      command=lambda: playcasinod(0.1),
                                      bg=config.colour_button, fg=config.colour_text,
                                      font=(config.font, config.font_size))

    button_cas_play_act20 = tk.Button(frame5, text="Поставити 20%",
                                      command=lambda: playcasinod(0.2),
                                      bg=config.colour_button, fg=config.colour_text,
                                      font=(config.font, config.font_size))

    button_cas_play_act50 = tk.Button(frame5, text="Поставити 50%",
                                      command=lambda: playcasinod(0.5),
                                      bg=config.colour_button, fg=config.colour_text,
                                      font=(config.font, config.font_size))


root.mainloop()
