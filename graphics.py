import numpy as np
import pygame
import sys
from Configuration import Config
from Main import Cosmopolia

width, height = 1000, 600

fps = 60
fpsClock = pygame.time.Clock()
pygame.init()
# Set up the drawing window
screen = pygame.display.set_mode((width, height), flags=pygame.RESIZABLE)
pygame.display.set_caption('Cosmopolia')
# Run until the user asks to quit
running = True
menu = True
players_choose = False
menu_objects = []
players_menu_objects = []
game_objects = []


def fontsize(size):
    font = pygame.font.SysFont('Times New Roman', size)
    return font


font_default = fontsize(20)


class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False, surface="menu"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.alreadyPressed = False
        if surface == "menu":
            menu_objects.append(self)
        elif surface == "game":
            game_objects.append(self)
        else:
            players_menu_objects.append(self)
        self.fillColors = {
            'normal': '#c295d6',
            'hover': '#666666',
            'pressed': '#333333',
        }
        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font_default.render(buttonText, True, (20, 20, 20))

    def process(self):
        mousePos = pygame.mouse.get_pos()
        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])
                if self.onePress:
                    self.onclickFunction()
                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True
            else:
                self.alreadyPressed = False
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


class Label:
    """ CLASS FOR TEXT LABELS ON THE SCREEN SURFACE """

    def __init__(self, text, x, y, size=20, color="black", surface="menu"):
        self.font = fontsize(size)
        self.image = self.font.render(text, 1, color)
        _, _, w, h = self.image.get_rect()
        self.rect = pygame.Rect(x, y, w, h)
        self.screen = screen
        self.text = text
        if surface == "menu":
            menu_objects.append(self)
        elif surface == "game":
            game_objects.append(self)
        else:
            players_menu_objects.append(self)

    def change_text(self, newtext, color="black"):
        self.image = self.font.render(newtext, 1, color)

    def change_font(self, newfont, size, color="black"):
        self.font = pygame.font.SysFont(newfont, size)
        self.change_text(self.text, color)

    def process(self):
        self.screen.blit(self.image, (self.rect))


class TextInput(pygame.sprite.Sprite):
    def __init__(self, x, y, width=100, height=50, color=(0, 0, 0),
                 bgcolor=(0, 255, 0), selectedColor=(0, 0, 255)):
        super().__init__()
        self.text_value = ""
        self.isSelected = False
        self.color = color
        self.bgcolor = bgcolor
        self.selectedColor = selectedColor

        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(self.text_value, True, self.color)
        self.bg = pygame.Rect(x, y, width, height)

    def clicked(self, mousePos):
        if self.bg.collidepoint(mousePos):
            self.isSelected = not (self.isSelected)
            return True
        return False

    def update(self, mousePos):
        pass

    def update_text(self, new_text):
        temp = self.font.render(new_text, True, self.color)
        if temp.get_rect().width >= (self.bg.width - 20):
            return
        self.text_value = new_text
        self.text = temp

    def process(self):
        self.pos = self.text.get_rect(center=(self.bg.x + self.bg.width / 2,
                                              self.bg.y + self.bg.height / 2))
        if self.isSelected:
            pygame.draw.rect(screen, self.selectedColor, self.bg)
        else:
            pygame.draw.rect(screen, self.bgcolor, self.bg)
        screen.blit(self.text, self.pos)


class CustomGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.current = None

    def current(self):
        return self.current


def choose_players():
    global menu, players_choose
    menu = False
    players_choose = True


def end():
    pygame.quit()


def show_menu():
    global menu
    menu = True


def start():
    global menu, players_choose
    menu = False
    players_choose = False


Button(150, 130, 300, 50, 'Розпочати гру', choose_players, surface="menu")
Button(150, 240, 300, 50, 'Завершити гру', end, surface="menu")
Button(0, 0, 200, 35, 'Повернутися в меню', show_menu, surface="game")
Button(0, 0, 200, 35, 'Повернутися в меню', show_menu, surface="players_choose")
Button(150, 330, 300, 50, 'Розпочати', start, surface="players_choose")
Label("Cosmopolia", 150, 30, 60, surface="menu")
Label("Оберіть гравців", 150, 30, 48, surface="players_choose")
Label("Бот?", 500, 30, 48, surface="players_choose")
Label("Гравець 1", 10, 100, 30, surface="players_choose")
Label("Гравець 2", 10, 200, 30, surface="players_choose")
TextInputGroup = CustomGroup()
TextInputGroup.add(TextInput(x=150, y=100, width=300))
TextInputGroup.add(TextInput(x=150, y=200, width=300))

ibeam = pygame.cursors.Cursor(pygame.SYSTEM_CURSOR_IBEAM)

while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for textinput in TextInputGroup:
                if textinput.clicked(mouse_pos):
                    if TextInputGroup.current:
                        TextInputGroup.current.isSelected = False
                    textinput.isSelected = True
                    TextInputGroup.current = textinput
                    break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                TextInputGroup.current.update_text(TextInputGroup.current.text_value[:-1])

            if event.key == pygame.K_RETURN:
                if TextInputGroup.current:
                    print(TextInputGroup.current.text_value)
        if event.type == pygame.TEXTINPUT:
            TextInputGroup.current.update_text(TextInputGroup.current.text_value + event.text)

    # Fill the background with white
    screen.fill((255, 255, 255))

    if menu:
        for object in menu_objects:
            object.process()
    elif players_choose:
        for object in players_menu_objects:
            object.process()
        for textinput in TextInputGroup:
            textinput.update(mouse_pos)
            textinput.process()
        if TextInputGroup.current and TextInputGroup.current.bg.collidepoint(mouse_pos):
            pygame.mouse.set_cursor(ibeam)
        else:
            pygame.mouse.set_cursor(pygame.cursors.Cursor())
    else:
        for object in game_objects:
            object.process()
        Game = Cosmopolia()
        Game.Create_Players()  # створюємо гравців
        for Current_Player in Game.Players:  # проходимо по циклу гравців
            Game.Before_turn(Current_Player)  # дії до хода гравця
            if Game.result == 0:  # якщо ігрок у в'язниці
                continue
            Game.Player_cube(Current_Player)  # дії під час хода гравця
        Current_Player = Game.Players[0]  # після проходження масива повертаємося до першого гравця в масиві

    # Flip the display
    pygame.display.flip()
    fpsClock.tick(fps)

# Done! Time to quit.
pygame.quit()
