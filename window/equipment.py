from window.nbk_editor import Fill, Side, Editor
from item.equipment import Equipment as itemEquipment
from item.equipment import Effect, Range, EquipmentType
from tkinter import filedialog
from misc.dice import Dice
from PIL import Image
import numpy as np
import json


class Equipment:
    def __init__(self):
        # equipment data
        self.index = None
        self.name = None
        self.description = None
        self.id = Dice.roll_dice(1, 999999)
        self.type = None
        self.effect = None
        self.range = None
        self.strength = None
        self.defense = None

        # tool utils
        self.data_handler = None
        self.window = None
        self.frame_main_infos = None
        self.entry_name = None
        self.entry_description = None
        self.label_image = None
        self.label_id = None

    def open_window(self, data_handler):

        # save data
        self.data_handler = data_handler
        self.index = len(data_handler.data.equipments)

        self.window = Editor.create_window("Dnd Equipment Creator", '800x420', False)


        ### SIDEBAR
        frame_sidebar = Editor.frame(self.window, True, Fill.BOTH, Side.LEFT)
        Editor.label(frame_sidebar, title="List of equipments", row=0, column=0, pad_x=10, pad_y=10)
        for i in range(len(data_handler.data.equipments)):
            Editor.button(frame_sidebar, text=data_handler.data.equipments[i].name, command=lambda j=i: self._update_display(j), row=i + 1, column=0)


        ### MAIN INFOS
        self.frame_main_infos = Editor.frame(self.window, True, Fill.BOTH, Side.LEFT)
        Editor.label(self.frame_main_infos, title="INFORMATION", row=0, column=0, pad_y=10)

        # name
        Editor.label(self.frame_main_infos, title="Name", row=1, column=0, pad_y=10)
        self.entry_name = Editor.entry(self.frame_main_infos, row=1, column=1)

        # background
        Editor.label(self.frame_main_infos, title="Description", row=2, column=0, pad_y=10)
        self.entry_description = Editor.entry(self.frame_main_infos, row=2, column=1)

        # image
        Editor.label(self.frame_main_infos, title="Image", row=3, column=0, pad_y=10)
        self.label_image = Editor.image(self.frame_main_infos, image=None, row=4, column=1)
        Editor.button(self.frame_main_infos, text="Get image", command=lambda: self._get_image(), row=3, column=1)


        ### DETAILS
        self.frame_weapon = Editor.frame(self.window, True, Fill.BOTH, Side.RIGHT)
        Editor.label(self.frame_weapon, title="DETAILS", row=0, column=0, pad_y=10)

        # type
        Editor.label(self.frame_weapon, "Type", row=1, column=0, pad_y=10)
        self.type = Editor.dropbox(self.frame_weapon, EquipmentType, on_change_command=self._display_details, row=1, column=2)

        ### WEAPON
        # strength
        Editor.label(self.frame_weapon, title="Strength: ", row=2, column=0, pad_y=10)
        self.strength = Editor.label(self.frame_weapon, title="0", row=2, column=1, pad_y=10)
        Editor.button(self.frame_weapon, text="(re)Generate", command=lambda : self._randomize_stat(self.strength, 3, 4), row=2, column=2)

        # effect
        Editor.label(self.frame_weapon, title="Effect", row=3, column=0, pad_y=10)
        self.effect = Editor.dropbox(self.frame_weapon, enum=Effect, on_change_command=None, row=3, column=2)

        # range
        Editor.label(self.frame_weapon, title="Range", row=4, column=0, pad_y=10)
        self.range = Editor.dropbox(self.frame_weapon, enum=Range, on_change_command=None, row=4, column=2)

        ### SHIELD
        # defense
        Editor.label(self.frame_weapon, title="Defense: ", row=5, column=0, pad_y=10)
        self.defense = Editor.label(self.frame_weapon, title="0", row=5, column=1, pad_y=10)
        Editor.button(self.frame_weapon, text="(re)Generate", command=lambda : self._randomize_stat(self.defense, 2, 4), row=5, column=2)

        ### ARMOR
        # defense
        Editor.label(self.frame_weapon, title="Defense: ", row=6, column=0, pad_y=10)
        self.defense = Editor.label(self.frame_weapon, title="0", row=6, column=1, pad_y=10)
        Editor.button(self.frame_weapon, text="(re)Generate", command=lambda : self._randomize_stat(self.defense, 2, 4), row=6, column=2)

        # resistance
        Editor.label(self.frame_weapon, title="Resistance", row=7, column=0, pad_y=10)
        self.effect = Editor.dropbox(self.frame_weapon, enum=Effect, on_change_command=None, row=7, column=2)


        ### FOOTER
        # save button & id
        Editor.button(self.frame_weapon, "SAVE", command=lambda: self._save_information(), row=8, column=0, pad_y=10)
        self.label_id = Editor.label(self.frame_weapon, "ID: " + self.id.__str__(), row=9, column=0)

        self.window.mainloop()

    def _display_details(self, event):
        print(f"updating with {self.type.get()}...")

    @staticmethod
    def _randomize_stat(label, amount: int = 1, value: int = 6):
        label.config(text=f"{Dice.roll_dice(amount, value)}")

    def _get_image(self):
        """
        Opens a window explorer window to pick an image.
        Then, displays this image on the tool window using an 'Editor.image'
        """
        # open the Windows explorer
        self.image_path = filedialog.askopenfilename(title= "Open an image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;")])

        # null exception
        if not self.image_path:
            return

        # display the image on the tool
        Editor.update_image_from_path(self.label_image, image_path=self.image_path)

    def _update_display(self, index):
        """
        Updates the display based on the data store in 'data_handler.data.equipments[index]' such as name, description, image, race, affinity, statistics and id
        """
        self.index = index

        # information
        Editor.set_text_entry(self.entry_name, self.data_handler.data.equipments[index].name)
        Editor.set_text_entry(self.entry_description, self.data_handler.data.equipments[index].description)
        Editor.update_image_from_json(self.label_image, image_json=self.data_handler.data.equipments[index].image)

        # details
        self.type.current(self.data_handler.data.equipments[index].type.value)
        self.effect.current(self.data_handler.data.equipments[index].effect.value)
        self.range.current(self.data_handler.data.equipments[index].range.value)
        self.strength.config(text = f"{self.data_handler.data.equipments[index].strength}")
        self.defense.config(text = f"{self.data_handler.data.equipments[index].defense}")
        self.label_id.config(text = f"ID: {self.data_handler.data.equipments[index].id}")

    def _save_information(self):
        """
        Saves the equipment's information the user entered into the tool into the 'data_handler.data.equipments' list of equipment
        """
        # get enum value from their names
        type = Editor.get_enum_value_from_names(EquipmentType, self.type.get())
        effect = Editor.get_enum_value_from_names(Effect, self.effect.get())
        range = Editor.get_enum_value_from_names(Range, self.range.get())

        # convert image using numpy
        image = Image.open(self.image_path)
        image_json = json.dumps(np.array(image).tolist())

        # creating new equipment
        new_equipment = itemEquipment(self.entry_name.get(), self.entry_description.get(), image_json, self.id, type, effect, range, int(self.strength.cget("text")), int(self.defense.cget("text")))

        # add to the equipment to the data list, if it doesn't already exist
        # otherwise, override the former equipment at 'self.index'
        if self.index >= len(self.data_handler.data.equipments):
            self.data_handler.data.equipments.append(new_equipment)
        else:
            self.data_handler.data.equipments[self.index] = new_equipment

        # save data information
        self.data_handler.save()