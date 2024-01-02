from window.nbk_editor import Fill, Side, Editor
from item.character import Character as itemCharacter
from item.character import Race, Affinity
from misc.dice import Dice
import json


class Character:
    def __init__(self):
        self.name = None
        self.description = None
        self.image = None
        self.id = Dice.roll_dice(1, 999999)
        self.race = None
        self.affinity = None
        self.do_randomize_stats = False

        self.data_handler = None
        self.entry_name = None
        self.entry_description = None

    def open_window(self, data_handler):

        self.data_handler = data_handler

        window = Editor.create_window("Dnd Character Creator", '800x420', False)

        # sidebar
        frame_sidebar = Editor.frame(window, True, Fill.BOTH, Side.LEFT)
        Editor.label(frame_sidebar, "List of characters")
        Editor.generate_buttons(frame_sidebar, data_handler.data.characters)


        # title
        frame_main = Editor.frame(window, True, Fill.BOTH, Side.RIGHT)
        Editor.label(frame_main, "Create new character")

        # name
        Editor.label(frame_main, "Name")
        self.entry_name = Editor.entry(frame_main)
        self.name = Editor.label(frame_main, "")

        # background
        Editor.label(frame_main, "Background")
        self.entry_description = Editor.entry(frame_main)
        self.description = Editor.label(frame_main, "")

        # image


        # race
        Editor.label(frame_main, "Race")
        self.race = Editor.dropbox(frame_main, Race, 'HUMAN')

        # affinity
        Editor.label(frame_main, "Class")
        self.race = Editor.dropbox(frame_main, Affinity, 'WARRIOR')

        # statistics
        Editor.label(frame_main, "Statistics")
        self.race = Editor.checkbox(frame_main, "randomize statistics")


        # save button
        frame_save = Editor.frame(frame_main, True, Fill.BOTH, Side.TOP)
        Editor.button(frame_save, "SAVE", command=lambda: self.save_information())

        # id
        frame_background = Editor.frame(frame_main, True, Fill.BOTH, Side.TOP)
        self.id = Editor.label(frame_background, "ID: " + self.id.__str__())

        window.mainloop()

    def save_information(self):

        # creating new character
        new_character = itemCharacter(self.name, self.description, self.image, self.id, self.race, self.affinity, self.do_randomize_stats)

        # save data information
        self.data_handler.data.characters.append(new_character)
        self.data_handler.save()