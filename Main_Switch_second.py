from tkinter import *
import tkinter.font as tkfont

class GameGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Гра")
        self.root.geometry("400x400")
        self.root.configure(bg="#B0B2FD")

        self.custom_font = tkfont.Font(family="Comic Sans MS", size=16)

        self.result_text = StringVar()
        self.result_label = Label(self.root, textvariable=self.result_text, font=self.custom_font, bg="#B0B2FD")
        self.result_label.pack(pady=50)

    def switch_second(self, res):
        self.word = res
        if self.word == "WinCasino":
            self.result_text.set("Перемога. Гравець Ім'я виграв Кількість грошей, тепер має таку суму грошей: Кількість грошей")
        elif self.word == "LoseCasino":
            self.result_text.set("Програш. Гравець Ім'я програв Кількість грошей, залишок: Кількість грошей")
        elif self.word == "WinRoulette":
            self.result_text.set("Перемога. Гравець Ім'я тепер має таку суму грошей: Кількість грошей")
        elif self.word == "LoseRoulette":
            self.result_text.set("Програш. Гравець Ім'я помер :)")

    def run(self):
        self.root.mainloop()

game = GameGUI()
game.switch_second("WinCasino")
game.run()
