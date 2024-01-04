from window.nbk_editor import Fill, Side, Editor
from item.item import Item as itemItem
from item.item import Effect
from tkinter import filedialog
from misc.dice import Dice
from PIL import Image
import numpy as np
import json


class Item:
    def __init__(self):
        # item data
        self.index = None
        self.image_path = None
        self.id = Dice.roll_dice(1, 999999)
        self.is_consumable = None
        self.effect = None
        self.strength = None

        # tool utils
        self.data_handler = None
        self.entry_name = None
        self.entry_description = None
        self.label_image = None
        self.label_id = None

    def open_window(self, data_handler):

        # save data
        self.data_handler = data_handler
        self.index = len(data_handler.data.items)

        window = Editor.create_window("Dnd Item Creator", '800x420', False)


        ### SIDEBAR
        frame_sidebar = Editor.frame(window, True, Fill.BOTH, Side.LEFT)
        Editor.label(frame_sidebar, title="List of items", row=0, column=0, pad_x=10, pad_y=10)
        for i in range(len(data_handler.data.items)):
            Editor.button(frame_sidebar, text=data_handler.data.items[i].name, command=lambda j=i: self._update_display(j), row=i + 1, column=0)


        ### MAIN INFOS
        frame_main_infos = Editor.frame(window, True, Fill.BOTH, Side.LEFT)
        Editor.label(frame_main_infos, title="INFORMATION", row=0, column=0, pad_y=10)

        # name
        Editor.label(frame_main_infos, title="Name", row=1, column=0, pad_y=10)
        self.entry_name = Editor.entry(frame_main_infos, row=1, column=1)

        # background
        Editor.label(frame_main_infos, title="Background", row=2, column=0, pad_y=10)
        self.entry_description = Editor.entry(frame_main_infos, row=2, column=1)

        # image
        Editor.label(frame_main_infos, title="Image", row=3, column=0, pad_y=10)
        self.label_image = Editor.image(frame_main_infos, image=None, row=4, column=1)
        Editor.button(frame_main_infos, text="Get image", command=lambda: self._get_image(), row=3, column=1)


        ### DETAILS
        frame_weapon = Editor.frame(window, True, Fill.BOTH, Side.RIGHT)
        Editor.label(frame_weapon, title="DETAILS", row=0, column=0, pad_y=10)

        # effect
        Editor.label(frame_weapon, title="Effect", row=1, column=0, pad_y=10)
        self.effect = Editor.dropbox(frame_weapon, enum=Effect, on_change_command=None, row=1, column=2)

        # strength
        Editor.label(frame_weapon, title="Defense: ", row=2, column=0, pad_y=10)
        self.strength = Editor.label(frame_weapon, title="0", row=2, column=1, pad_y=10)
        Editor.button(frame_weapon, text="(re)Generate", command=lambda : self._randomize_stat(self.strength, 3, 4), row=2, column=2)


        ### FOOTER
        # save button & id
        Editor.button(frame_weapon, text="SAVE", command=lambda: self._save_information(), row=3, column=0, pad_y=10)
        self.label_id = Editor.label(frame_weapon, title="ID: " + self.id.__str__(), row=4, column=0)

        window.mainloop()

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
        Updates the display based on the data store in 'data_handler.data.items[index]' such as name, description, image, race, affinity, statistics and id
        """
        self.index = index

        # information
        Editor.set_text_entry(self.entry_name, self.data_handler.data.items[index].name)
        Editor.set_text_entry(self.entry_description, self.data_handler.data.items[index].description)
        Editor.update_image_from_json(self.label_image, image_json=self.data_handler.data.items[index].image)

        # details
        self.effect.current(self.data_handler.data.items[index].effect.value)
        self.strength.config(text = f"{self.data_handler.data.items[index].strength}")
        self.label_id.config(text = f"ID: {self.data_handler.data.items[index].id}")

    def _save_information(self):
        """
        Saves the item's information the user entered into the tool into the 'data_handler.data.items' list of item
        """
        # get enum value from their names
        effect = Editor.get_enum_value_from_names(Effect, self.effect.get())

        # convert image using numpy
        image = Image.open(self.image_path)
        image_json = json.dumps(np.array(image).tolist())

        # creating new item
        new_item = itemItem(self.entry_name.get(), self.entry_description.get(), image_json, self.id, effect, int(self.strength.cget("text")))

        # add to the item to the data list, if it doesn't already exist
        # otherwise, override the former item at 'self.index'
        if self.index >= len(self.data_handler.data.items):
            self.data_handler.data.items.append(new_item)
        else:
            self.data_handler.data.items[self.index] = new_item

        # save data information
        self.data_handler.save()