import tkinter as tk
from players import *
import random
from fields import Field
from Configuration import Config


class TeleportButton(Field):
    def __init__(self):
        super().__init__()

    def action_teleport(self, curr):
        conf = Config()
        teleport_indices = [i for i, field in enumerate(conf.array_Fields) if field == "телепорт"]

        if teleport_indices:
            current_field = curr
            valid_indices = [index for index in teleport_indices if index != current_field]

            if valid_indices:
                teleport_index = random.choice(valid_indices)
                return teleport_index

        return None

# player1 = client(HumanCreator(), "name")
# print(player1.get_current_field())
#
# teleport_button = TeleportButton()
# teleport_button.action_teleport(player1)
#
# print(player1.get_current_field())
# 2, 11, 14