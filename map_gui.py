import tkinter as tk
from PIL import Image, ImageTk
from Configuration import Config
import random
from map import Map
from players import *
from teleportbuttons import TeleportButton

config = Config()


class MapGUI:
    def __init__(self, root, num_circles, players_amount=2):
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
        self.map = Map()
        self.players = []
        self.current_player = 0

    def clear(self, players_amount=2):
        self.players_amount = players_amount
        self.players_positions = [0 for i in range(players_amount)]
        self.map = Map()
        self.players = []
        self.current_player = 0

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
            self.canvas.create_image(x, y, anchor=tk.NW, image=self.star_image_tk_arr[i])

    def show_cells(self):
        for i in range(config.fields_amount):
            self.load_cell_image(i)
            x, y = self.circles_coords[i]
            self.canvas.create_image(x, y, anchor=tk.NW, image=self.cell_image_tk_arr[i])

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
        for i in range(self.num_circles):
            column = i % num_columns
            row = i // num_columns

            x = x_start + column * (2 * self.circle_radius + gap)
            y = y_start + row * (2 * self.circle_radius + gap)

            if row != 0 and row != num_rows - 1 and column != 0 and column != num_columns - 1:
                image = Image.new("RGBA", (int(2 * self.circle_radius), int(2 * self.circle_radius)),
                                  "#00000000")
                image_tk = ImageTk.PhotoImage(image)
                self.canvas.create_image(x, y, anchor=tk.NW, image=image_tk)

            else:
                self.canvas.create_oval(x, y, x + 2 * self.circle_radius, y + 2 * self.circle_radius, outline='yellow',
                                        width=2)
        for i, coord in enumerate(self.circles_coords):
            x, y = coord
            text_x = x + self.circle_radius / 2  # Adjust the text position as needed
            text_y = y + self.circle_radius / 2  # Adjust the text position as needed
            self.canvas.create_text(text_x, text_y, text=str(i), anchor=tk.CENTER, fill="white")
        self.show_players()

    def move_star(self):
        player = self.current_player
        self.players_positions[player] = (self.players_positions[player] + random.randint(1, 6)) % config.fields_amount
        position = self.players_positions[player]

        if position in [2, 11, 14]:
            teleport_button = TeleportButton()
            index = teleport_button.action_teleport(self.players_positions[player])
            print("Гравця телепортувало в клітину:", index, "з клітини",  self.players_positions[player])
            self.players_positions[player] = index


        print(player, self.players_positions[player])
        self.show_players()
        self.current_player += 1
        self.current_player %= self.players_amount
