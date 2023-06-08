import tkinter as tk
from PIL import Image, ImageTk


class Config():
   """клас, який містить дані для створення поля"""

   fields_amount = 16 #кількість клітинок на полі
   array_Fields=["старт", "планета", "телепорт", "планета", "тюрма", "планета", "планета","шанс",
                 "планета", "планета", "планета", "телепорт","планета","планета","телепорт", "планета"]
   #масив, котрий визначає розташування різних типів клітинок на полі

   colour_background = "#05152e"
   colour_button = "#8b298e"
   colour_frame3 = "#000000"
   colour_frame4 = "#0e254e"
   colour_text = "#dae7f0"
   colour_frame3_text = "#92b7ff"

   font = "Comic Sans MS"
   font_size = 16
   font_weight = "bold"

   image_for_map = Image.open("space_for_map.jpg")

   image_start_finish= Image.open("Start_Finish.PNG")
   image_prison = Image.open("Prison.PNG")
   image_teleport= Image.open("Teleport.PNG")
   image_chance = Image.open("Chance.PNG")

   image_planet_red= Image.open("Planet_Red.PNG")
   image_planet_blue = Image.open("Planet_Blue.PNG")
   image_planet_green = Image.open("Planet_Green.PNG")
   image_planet_yellow = Image.open("Planet_Yellow.PNG")

   image_ufo_red = Image.open("UFO_Red.PNG")
   image_ufo_blue = Image.open("UFO_Blue.PNG")
   image_ufo_green = Image.open("UFO_Green.PNG")
   image_ufo_yellow = Image.open("UFO_Yellow.PNG")

