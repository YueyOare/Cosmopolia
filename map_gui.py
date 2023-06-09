import random
import tkinter as tk

from PIL import Image, ImageTk

from map import Map
from players import *
from teleportbuttons import TeleportButton

config = Config()


class MapGUI:
    def __init__(self, root, num_circles, players_amount=2):
        self.dice = None
        self.cell_image_tk = None
        self.star_image_tk = None
        self.circles_coords = None
        self.star_image = None
        self.cell_image = None
        self.circle_radius = None
        self.root = root
        self.num_circles = num_circles
        self.star_image_tk_arr = [None for i in range(players_amount)]
        self.cell_image_tk_arr = [None for i in range(config.fields_amount)]
        self.players_positions = [0 for i in range(players_amount)]
        self.players_amount = players_amount
        self.canvas = tk.Canvas(self.root, bg=config.colour_background)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.redraw_table)
        self.map = Map()  # масив об'єктів полів
        self.players = []  # масив об'єктів "гравець"
        self.current_player = 0  # номер поточного гравця
        self.prison = self.map.array_Fields_in_map[4]  # об'єкт "тюрма" з масива об'єктів полів
        self.owners = [None for i in range(config.fields_amount)]

    def clear(self, players_amount=2):
        self.players_amount = players_amount
        self.players_positions = [0 for i in range(players_amount)]
        self.map = Map()
        self.players = []
        self.current_player = 0
        self.star_image_tk_arr = [None for i in range(players_amount)]
        self.owners = [None for i in range(config.fields_amount)]
        for i in range(players_amount):
            self.load_star_image(i)

    def load_star_image(self, num):
        self.star_image = config.players_icons[num]
        self.star_image = self.star_image.resize((int(self.circle_radius), int(self.circle_radius)))
        self.star_image_tk = ImageTk.PhotoImage(self.star_image)
        self.star_image_tk_arr[num] = self.star_image_tk

    def load_cell_image(self, num):
        self.cell_image = config.planets_icons[num]
        self.cell_image = self.cell_image.resize((int(self.circle_radius * 2), int(self.circle_radius * 2)))
        self.cell_image_tk = ImageTk.PhotoImage(self.cell_image)
        self.cell_image_tk_arr[num] = self.cell_image_tk

    def show_players(self):
        for i in range(self.players_amount):
            self.load_star_image(i)
            x, y = self.circles_coords[self.players_positions[i]]
            self.canvas.create_image(x+5*i, y, anchor=tk.NW, image=self.star_image_tk_arr[i])

    def show_cells(self):
        for i in range(config.fields_amount):
            self.load_cell_image(i)
            x, y = self.circles_coords[i]
            self.canvas.create_image(x, y, anchor=tk.NW, image=self.cell_image_tk_arr[i])

    def own_planet(self, player):
        self.owners[self.players_positions[player]] = player

    def redraw_table(self, event=None):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        self.circle_radius = min(width - 20, height - 20) / 10
        gap = 0

        num_columns = 5
        num_rows = (self.num_circles + num_columns - 1) // num_columns

        total_width = num_columns * (2 * self.circle_radius + gap) - gap
        total_height = num_rows * (2 * self.circle_radius + gap) - gap

        x_start = 5 + (width - total_width) / 2
        y_start = 5 + (height - total_height) / 2
        self.circles_coords = []
        for i in range(num_columns):
            self.circles_coords.append([x_start + i * (2 * self.circle_radius + gap),
                                        y_start + 0 * (2 * self.circle_radius + gap)])
        for i in range(1, num_rows):
            self.circles_coords.append([x_start + (num_columns - 1) * (2 * self.circle_radius + gap),
                                        y_start + i * (2 * self.circle_radius + gap)])
        for i in range(num_columns - 2, -1, -1):
            self.circles_coords.append([x_start + i * (2 * self.circle_radius + gap),
                                        y_start + (num_rows - 1) * (2 * self.circle_radius + gap)])
        for i in range(num_columns - 2, 0, -1):
            self.circles_coords.append([x_start + 0 * (2 * self.circle_radius + gap),
                                        y_start + i * (2 * self.circle_radius + gap)])
        self.show_cells()
        for i in range(config.fields_amount):
            if self.owners[i] is not None:
                x, y = self.circles_coords[i]
                self.canvas.create_oval(x, y, x + 2 * self.circle_radius, y + 2 * self.circle_radius, outline=config.players_colours[self.owners[i]],
                                        width=2)
        for i, coord in enumerate(self.circles_coords):
            x, y = coord
            text_x = x + self.circle_radius / 2  # Adjust the text position as needed
            text_y = y + self.circle_radius / 2  # Adjust the text position as needed
            self.canvas.create_text(text_x, text_y, text=str(i), anchor=tk.CENTER, fill="white")
        self.show_players()

    def planet_action(self):
        self.show_players()
        answer = self.map.array_Fields_in_map[self.players_positions[self.current_player]].event(self.players[self.current_player])
        if answer == "player can buy":
            return 0, 0   # поле - планета, дії - пуста планета
        elif answer == "player must pay":
            return 0, 1   # поле - планета, дії - чужа планета
        elif answer == "player is in his field":
            return 0, 2   # поле - планета, дії - своя планета
        else:
            return [-1]

    def teleport_action(self):
        player = self.current_player
        teleport_button = TeleportButton()
        teleport_index = self.players_positions[player]
        player_index = teleport_button.action_teleport(self.players_positions[player])
        self.players_positions[player] = player_index
        self.players[player].set_current_field(player_index)
        self.show_players()
        return 1, teleport_index, player_index

    def prison_action(self):
        self.show_players()
        return [2]

    def chance_action(self):
        self.show_players()
        return [3]

    def casino_action(self):
        self.show_players()
        return [4]

    def roll_dice(self):
        player = self.current_player  # дізнаємось поточного гравця
        if self.players[player].get_enabled():
            self.dice = random.randint(1, 6)
            self.players[player].move_to(self.dice)  # двигаємо поточного гравця
            self.players_positions[player] = self.players[
                player].get_current_field()  # оновлюємо його позицію в масиві позицій
            position = self.players_positions[player]  # зберігаємо його позицію
            if config.array_Fields[position] == "телепорт":  # якщо він наступив на телепорт
                return self.teleport_action()
            elif config.array_Fields[position] == "планета":  # якщо він наступив на планету
                return self.planet_action()
            elif config.array_Fields[position] == "тюрма":  # якщо він наступив на тюрму
                return self.prison_action()
            elif config.array_Fields[position] == "казіно":   # тут має бути казіно
                return self.casino_action()
            elif config.array_Fields[position] == "шанс":  # якщо він наступив на шанс
                return self.chance_action()
        else:
            self.players[player].set_enabled(True)
        return [-1]