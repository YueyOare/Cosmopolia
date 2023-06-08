import tkinter as tk
from tkinter import *
import tkinter.font as tkfont
from PIL import Image, ImageTk
import random
from Configuration import Config
import numpy as np


class MapGUI():
    def __init__(self, root, players_amount=4):
        self.players_icons = None
        self.circles = None
        self.texts = None
        self.config = Config()
        self.root = root

        self.root.configure(bg="#4100CC")
        self.players_amount = players_amount
        square_size = 150
        self.squares_per_side = int(np.sqrt(self.config.fields_amount)) + 1

        # Створюємо полотно
        self.canvas = tk.Canvas(root, bg="#4100CC", highlightthickness=0)
        background_color = "#4100CC"
        circle_color = "#01004D"
        # Прив'язуємо функцію до події зміни розміру canvas
        self.canvas.bind("<Configure>", self.resize_image)
        self.canvas.pack(fill="both", expand=True)

    def create_circle(self, x, y, size, color, number):
        # Розраховуємо координати для круга
        x1 = x * size
        y1 = y * size
        x2 = x1 + size
        y2 = y1 + size

        # Створюємо круг на полотні
        circle = self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")

        # Додаємо номер у центр круга
        text = self.canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(number), fill="white",
                                       font=("Arial", 16))

        return circle, text

    def create_circles(self, square_size=150, circle_color="#01004D"):
        # Додаємо кружки
        locationB = [1, 2, 3, 4]
        locationC = [3, 2, 1, 0]
        locationD = [3, 2, 1]
        circles = []
        texts = []
        number = 1
        for x in range(self.squares_per_side):
            # Створюємо кружок та отримуємо його ідентифікатор
            circle, text = self.create_circle(x, 0, square_size, circle_color, number)

            # Додаємо ідентифікатор кружка до списку
            circles.append(circle)
            texts.append(text)

            number += 1

        number = 6
        for y in locationB:
            circle, text = self.create_circle(4, y, square_size, circle_color, number)
            circles.append(circle)
            texts.append(text)
            number += 1

        number = 11
        for z in locationC:
            circle, text = self.create_circle(z, 4, square_size, circle_color, number)
            circles.append(circle)
            texts.append(text)
            number += 1

        number = 14
        for q in locationD:
            circle, text = self.create_circle(0, q, square_size, circle_color, number)
            circles.append(circle)
            texts.append(text)
            number += 1
        return circles, texts

    def resize_image(self, event):
        canvas_width = event.width
        canvas_height = event.height

        # Завантажуємо зображення
        image = Image.open("Space_photo.gif")
        image = image.resize((canvas_width, canvas_height))
        photo = ImageTk.PhotoImage(image)

        # Оновлюємо зображення на canvas
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo  # Зберігаємо посилання на зображення, щоб уникнути видалення з пам'яті
        self.circles, self.texts = self.create_circles(min(canvas_height, canvas_width) / 5 - 1, "#01004D")
        self.players_icons = []
        for i in range(self.players_amount):
            player_icon = PlayerIcons(self.canvas, "star.png", min(canvas_height, canvas_width) / 5 - 1)
            self.players_icons.append(player_icon)

    def roll_dice(self):
        global number, player_num
        # Генеруємо випадкове число від 1 до 6
        roll = random.randint(1, 6)

        # Обчислюємо новий номер за алгоритмом: (номер + згенероване число) % 16
        number = (number + roll) % 16
        if number == 0:
            number = 16
        # Оновлюємо текст на кнопці "Випало"
        # dice_number.config(text=f"Випало: {roll}")

        # Переміщуємо зірку на нове положення
        self.players_icons[player_num].move_player()


class PlayerIcons():
    def __init__(self, canvas, img, size):
        self.canvas = canvas
        # Додаємо зображення зірки
        star_image = Image.open(img)
        star_image = star_image.resize((int(size / 2), int(size / 2)))
        star_photo = ImageTk.PhotoImage(star_image)

        # Отримуємо початкові координати для зірки
        x, y = get_coordinates(1, size)

        # Створюємо зірку на полотні
        self.star = canvas.create_image(0, 0, anchor=tk.NW, image=star_photo)

    def move_player(self):
        global number
        # Отримуємо координати для нового положення зірки
        x, y = get_coordinates(number)

        # Зміщуємо зірку на нові координати
        self.canvas.coords(self.star, x, y)

        # Підносимо зірку над іншими об'єктами на полотні
        self.canvas.lift(self.star)


def get_coordinates(number, square_size):
    if number <= 5:
        return (number - 1) * square_size, 0
    elif 5 < number <= 9:
        return 4 * square_size, (number - 5) * square_size
    elif number == 10:
        return 3 * square_size, 4 * square_size
    elif number == 11:
        return 2 * square_size, 4 * square_size
    elif number == 12:
        return 1 * square_size, 4 * square_size
    elif number == 13:
        return 0, 4 * square_size
    elif number == 14:
        return 0, 3 * square_size
    elif number == 15:
        return 0, 2 * square_size
    elif number == 16:
        return 0, 1 * square_size
    else:
        return 0, (16 - number) * square_size