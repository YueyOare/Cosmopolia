from tkinter import *
import tkinter.font as tkfont

class GameGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Гра")
        self.root.geometry("400x400")
        self.root.configure(bg="#B0B2FD")

        self.custom_font = tkfont.Font(family="Comic Sans MS", size=16)

        self.field_label = Label(self.root, text="", font=self.custom_font, bg="#B0B2FD")
        self.field_label.pack(pady=50)

        self.action_label = Label(self.root, text="Виберіть дію:", font=self.custom_font, bg="#B0B2FD")
        self.action_label.pack()

        self.frame = Frame(self.root, bg="#B0B2FD")
        self.frame.pack(pady=20)

        self.button1 = Button(self.frame, text="Хабарь", command=lambda: self.process_action("Хабарь"), font=self.custom_font,
                              bg="#010632", fg="white", relief="raised", padx=10)
        self.button1.pack(side=LEFT, padx=10)

        self.button2 = Button(self.frame, text="Сидіти далі", command=lambda: self.process_action("Сидіти далі"),
                              font=self.custom_font, bg="#010632", fg="white", relief="raised", padx=10)
        self.button2.pack(side=LEFT, padx=10)

        self.button3 = Button(self.frame, text="Збігти", command=lambda: self.process_action("Збігти"),
                              font=self.custom_font, bg="#010632", fg="white", relief="raised", padx=10)
        self.button3.pack(side=LEFT, padx=10)

        self.result_label = Label(self.root, text="", font=self.custom_font, bg="#B0B2FD")
        self.result_label.pack()

        self.root.mainloop()

    def process_action(self, action):
        # Логіка гри для обробки вибраної дії
        if action == "Хабарь":
            self.result_label.config(text="Гравець обрав дію: хабар")
        elif action == "Сидіти далі":
            self.result_label.config(text="Гравець обрав дію: сидіти далі")
        elif action == "Збігти":
            self.result_label.config(text="Гравець обрав дію: збігти")

GameGUI()

