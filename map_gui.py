import tkinter as tk
from PIL import Image, ImageTk
from Configuration import Config

config = Config()


class MapGUI:
    def __init__(self, root, num_circles):
        self.star_image = None
        self.circle_radius = None
        self.root = root
        self.num_circles = num_circles
        self.star_image_tk = None
        self.current_circle = 0

        self.canvas = tk.Canvas(self.root, bg=config.colour_background)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<Configure>", self.redraw_table)

    def load_star_image(self):
        self.star_image = Image.open("star.png")  # Замініть "star.png" на шлях до вашого зображення зірки
        self.star_image = self.star_image.resize((int(self.circle_radius), int(self.circle_radius)))
        self.star_image_tk = ImageTk.PhotoImage(self.star_image)

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

        for i in range(self.num_circles):
            column = i % num_columns
            row = i // num_columns

            x = x_start + column * (2 * self.circle_radius + gap)
            y = y_start + row * (2 * self.circle_radius + gap)

            if row != 0 and row != num_rows - 1 and column != 0 and column != num_columns - 1:
                image = Image.new("RGBA", (int(2 * self.circle_radius), int(2 * self.circle_radius)),
                                  config.transparent_color)
                image_tk = ImageTk.PhotoImage(image)
                self.canvas.create_image(x, y, anchor=tk.NW, image=image_tk)

            else:
                self.canvas.create_oval(x, y, x + 2 * self.circle_radius, y + 2 * self.circle_radius, outline='black')

        self.load_star_image()
        self.canvas.create_image(x_start, y_start, anchor=tk.NW, image=self.star_image_tk)

    def move_star(self):
        self.current_circle = (self.current_circle + 1) % self.num_circles
        self.redraw_table()

        column = self.current_circle % 5
        row = self.current_circle // 5

        x_start = 5 + (self.canvas.winfo_width() - self.canvas.winfo_reqwidth()) / 2
        y_start = 5 + (self.canvas.winfo_height() - self.canvas.winfo_reqheight()) / 2

        x = x_start + column * (2 * self.circle_radius + 0)
        y = y_start + row * (2 * self.circle_radius + 0)

        self.canvas.create_image(x, y, anchor=tk.NW, image=self.star_image_tk)
