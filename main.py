import tkinter as tk
from PIL import Image, ImageTk
import random

def create_circle(canvas, x, y, size, color, number):
    # Розраховуємо координати для круга
    x1 = x * size
    y1 = y * size
    x2 = x1 + size
    y2 = y1 + size

    # Створюємо круг на полотні
    circle = canvas.create_oval(x1, y1, x2, y2, fill=color, outline="black")

    # Додаємо номер у центр круга
    canvas.create_text((x1 + x2) // 2, (y1 + y2) // 2, text=str(number), fill="white", font=("Arial", 16))

    return circle

def roll_dice():
    global number
    # Генеруємо випадкове число від 1 до 6
    roll = random.randint(1, 6)

    # Обчислюємо новий номер за алгоритмом: (номер + згенероване число) % 16
    number = (number + roll) % 16
    if number == 0:
        number = 16
    # Оновлюємо текст на кнопці "Випало"
    dice_number.config(text=f"Випало: {roll}")

    # Переміщуємо зірку на нове положення
    move_star()

def move_star():
    global number
    # Отримуємо координати для нового положення зірки
    x, y = get_coordinates(number)

    # Зміщуємо зірку на нові координати
    canvas.coords(star, x, y)

    # Підносимо зірку над іншими об'єктами на полотні
    canvas.lift(star)

def get_coordinates(number):
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

root = tk.Tk()
root.title("Монополія")
root.geometry("800x600")
root.configure(bg="#4100CC")

square_size = 150
squares_per_side = 5

canvas_width = square_size * squares_per_side
canvas_height = square_size * squares_per_side

# Створюємо фрейм для розміщення полотна
frame = tk.Frame(root, bg="#4100CC")
frame.pack(side=tk.LEFT)

# Створюємо полотно
canvas = tk.Canvas(frame, width=canvas_width, height=canvas_height, bg="#4100CC", highlightthickness=0)
canvas.pack()

background_color = "#4100CC"
circle_color = "#01004D"

# Додаємо зображення заднього фону
image = Image.open("Space_photo.gif")
image = image.resize((int(image.width * 1.3), int(image.height * 1.3)))
photo = ImageTk.PhotoImage(image)
image_width = photo.width()
image_height = photo.height()
image_x = (canvas_width - image_width) // 2
image_y = (canvas_height - image_height) // 2
canvas.create_image(image_x, image_y, anchor=tk.NW, image=photo)

number = 1
locationB = [1, 2, 3, 4]
locationC = [3, 2, 1, 0]
locationD = [3, 2, 1]

circles = []  # Список для збереження ідентифікаторів кружків

# Додаємо кружки
for x in range(squares_per_side):
    # Створюємо кружок та отримуємо його ідентифікатор
    circle = create_circle(canvas, x, 0, square_size, circle_color, number)

    # Додаємо ідентифікатор кружка до списку
    circles.append(circle)

    number += 1

number = 6
for y in locationB:
    circle = create_circle(canvas, 4, y, square_size, circle_color, number)
    circles.append(circle)
    number += 1

number = 11
for z in locationC:
    circle = create_circle(canvas, z, 4, square_size, circle_color, number)
    circles.append(circle)
    number += 1

number = 14
for q in locationD:
    circle = create_circle(canvas, 0, q, square_size, circle_color, number)
    circles.append(circle)
    number += 1

# Додаємо зображення зірки
star_image = Image.open("star.png")
star_image = star_image.resize((int(square_size / 2), int(square_size / 2)))
star_photo = ImageTk.PhotoImage(star_image)

# Отримуємо початкові координати для зірки
x, y = get_coordinates(1)

# Створюємо зірку на полотні
star = canvas.create_image(x, y, anchor=tk.NW, image=star_photo)

# Додаємо кнопку "Кинути кубик"
button_frame = tk.Frame(root, bg="#4100CC")
button_frame.pack(side=tk.LEFT, padx=20)
dice_button = tk.Button(button_frame, text="Кинути кубик", command=roll_dice)
dice_button.pack(pady=10)
dice_number = tk.Label(button_frame, text="Випало: ", font=("Arial", 16), bg="#B0B2FD")
dice_number.pack()
frame.place(x=700, y=20)
root.mainloop()