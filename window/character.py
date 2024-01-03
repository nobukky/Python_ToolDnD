from window.nbk_editor import Fill, Side, Editor
from item.character import Character as itemCharacter
from item.character import Race, Affinity
from tkinter import filedialog
from misc.dice import Dice
import json
from PIL import Image
import numpy as np
import pathlib


class Character:
    def __init__(self):
        self.index = None

        self.name = None
        self.description = None
        self.image_path = None
        self.id = Dice.roll_dice(1, 999999)
        self.race = None
        self.affinity = None
        self.do_randomize_stats = False
        self.statistics: list[int] = list()
        self.labels_statistics = []
        self.row_index = None

        self.data_handler = None
        self.variable_method = None
        self.entry_name = None
        self.entry_description = None
        self.label_image = None
        self.frame_statistics = None
        self.label_id = None

    def open_window(self, data_handler):

        self.data_handler = data_handler
        self.index = len(data_handler.data.characters)

        window = Editor.create_window("Dnd Character Creator", '800x450', False)

        # sidebar
        frame_sidebar = Editor.frame(window, True, Fill.BOTH, Side.LEFT)
        Editor.label(frame_sidebar, title="List of characters", row=0, column=0,)
        for i in range(len(data_handler.data.characters)):
            Editor.button(frame_sidebar, text=data_handler.data.characters[i].name, command=lambda j=i: self.update_display(j), row=i+1, column=0)


        # main infos
        frame_main_infos = Editor.frame(window, True, Fill.BOTH, Side.LEFT)
        Editor.label(frame_main_infos, title="INFORMATION", row=0, column=0, pad_y=10)

        # name
        Editor.label(frame_main_infos, title="Name", row=1, column=0, pad_y=10)
        self.entry_name = Editor.entry(frame_main_infos, row=1, column=1)

        # background
        Editor.label(frame_main_infos, title="Background", row=3, column=0, pad_y=10)
        self.entry_description = Editor.entry(frame_main_infos, row=3, column=1)

        # image
        Editor.label(frame_main_infos, title="Image", row=5, column=0, pad_y=10)
        self.label_image = Editor.image(frame_main_infos, image=None, row=6, column=1)
        Editor.button(frame_main_infos, text="Get image", command=lambda: self.get_image(), row=5, column=1)

        # race
        Editor.label(frame_main_infos, title="Race", row=7, column=0, pad_y=10)
        self.race = Editor.dropbox(frame_main_infos, enum=Race, on_change_command=None, row=7, column=1)

        # affinity
        Editor.label(frame_main_infos,title="Class", row=8, column=0, pad_y=10)
        self.affinity = Editor.dropbox(frame_main_infos, enum=Affinity, on_change_command=None, row=8, column=1)


        # statistics
        self.frame_statistics = Editor.frame(window, True, Fill.BOTH, Side.RIGHT)
        Editor.label(self.frame_statistics, title="STATISTICS", row=0, column=0, pad_y=10)

        Editor.label(self.frame_statistics, title="Which randomize method do you use?", row=1, column=0)
        self.variable_method = Editor.string_var()
        Editor.radiobutton(self.frame_statistics, text="1d20", value=0, variable=self.variable_method, row=1, column=1)
        Editor.radiobutton(self.frame_statistics, text="3d6", value=1, variable=self.variable_method, row=1, column=2)

        Editor.button(self.frame_statistics, text="(re)Generate", command=lambda: self.generate_statistics(starting_row=4), row=2, column=0)

        Editor.label(self.frame_statistics, title="Your statistics:", row=3, column=0)
        self.generate_statistics(starting_row=4, do_generate_empty=True)

        # save button & id
        Editor.button(self.frame_statistics, text="SAVE", command=lambda: self.save_information(), row=9, column=0, pad_y=10)
        self.label_id = Editor.label(self.frame_statistics, title="ID: " + self.id.__str__(), row=10, column=0)

        window.mainloop()

    def generate_statistics(self, starting_row: int=0, do_generate_empty: bool=False):
        self.statistics = []
        if do_generate_empty:
            for i in range(0, 5):
                self.statistics.append(0)
        else:
            if self.variable_method.get() == 0:
                for i in range(0, 5):
                    self.statistics.append(Dice.roll_dice(1, 20))
            else:
                for i in range(0, 5):
                    self.statistics.append(Dice.roll_dice(3, 6))

        self.display_statistics(starting_row, do_generate_empty)

    def display_statistics(self, starting_row: int, do_generate_empty: bool=False):
        row_index = starting_row
        if len(self.statistics) != 0:
            for i in range(len(self.statistics)):

                # destroy former labels, if they exist
                if len(self.labels_statistics) > i and do_generate_empty is False:
                    self.labels_statistics[i].destroy()

                # get statistic name
                statistic_name = ""
                match i:
                    case 0:
                        statistic_name = "   Strength"
                    case 1:
                        statistic_name = "   Dexterity"
                    case 2:
                        statistic_name = "   Intelligence"
                    case 3:
                        statistic_name = "   Luck"
                    case 4:
                        statistic_name = "   Health points"

                # add new labels
                self.labels_statistics.append(Editor.label(self.frame_statistics, title=f"{statistic_name}: {self.statistics[i]}", row=row_index, column=0))
                row_index += 1

    def get_image(self, new_image_path: str = ""):
        # empty exception
        if new_image_path == "empty":
            return

        # open the Windows explorer
        self.image_path = filedialog.askopenfilename(title= "Open an image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;")])

        # null exception
        if not self.image_path:
            return

        # display the image on the tool
        Editor.update_image_from_path(self.label_image, image_path=self.image_path)

    def  update_display(self, index):
        self.index = index

        # information
        self.set_text(self.entry_name, self.data_handler.data.characters[index].name)
        self.set_text(self.entry_description, self.data_handler.data.characters[index].description)
        Editor.update_image_from_json(self.label_image, image_json=self.data_handler.data.characters[index].image)
        self.race.current(self.data_handler.data.characters[index].race.value)
        self.affinity.current(self.data_handler.data.characters[index].affinity.value)

        # statistics
        self.statistics = self.data_handler.data.characters[index].statistics
        self.display_statistics(starting_row=4)
        self.label_id.config(text = f"ID: {self.data_handler.data.characters[index].id}")


    @staticmethod
    def set_text(entry, text):
        entry.delete(0, "end")
        entry.insert(0, text)

    def save_information(self):
        # get enum value from their names
        race = Editor.get_enum_value_from_names(Race, self.race.get())
        affinity = Editor.get_enum_value_from_names(Affinity, self.affinity.get())

        # convert image using numpy
        image = Image.open(self.image_path)
        image_json = json.dumps(np.array(image).tolist())

        # creating new character
        new_character = itemCharacter(self.entry_name.get(), self.entry_description.get(), image_json, self.id, race, affinity, self.statistics)

        # add to the character to the data list, if it doesn't already exist
        # otherwise, override the former character at 'self.index'
        if self.index >= len(self.data_handler.data.characters):
            self.data_handler.data.characters.append(new_character)
        else:
            self.data_handler.data.characters[self.index] = new_character

        # save data information
        self.data_handler.save()