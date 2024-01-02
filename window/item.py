from window.nbk_editor import Fill, Side, Editor
from item.item import Item as itemItem
from item.item import Effect
from misc.dice import Dice


class Item:
    def __init__(self):
        self.name = None
        self.description = None
        self.image = None
        self.id = Dice.roll_dice(1, 999999)
        self.is_consumable = None
        self.effect = None

        self.data_handler = None
        self.entry_name = None
        self.entry_description = None

    def open_window(self, data_handler):

        self.data_handler = data_handler

        window = Editor.create_window("Dnd Item Creator", '800x420', False)

        # sidebar
        frame_sidebar = Editor.frame(window, True, Fill.BOTH, Side.LEFT)
        Editor.label(frame_sidebar, "List of items")
        Editor.generate_buttons(frame_sidebar, data_handler.data.items)


        # title
        frame_main = Editor.frame(window, True, Fill.BOTH, Side.RIGHT)
        Editor.label(frame_main, "Create new item")

        # name
        Editor.label(frame_main, "Name")
        self.entry_name = Editor.entry(frame_main)
        self.name = Editor.label(frame_main, "")

        # background
        Editor.label(frame_main, "Description")
        self.entry_description = Editor.entry(frame_main)
        self.description = Editor.label(frame_main, "")

        # image
        Editor.label(frame_main, "Image")

        # race
        Editor.label(frame_main, "Consumable")
        self.is_consumable = Editor.checkbox(frame_main, "Is this item a consumable?")
        self.effect = Editor.dropbox(frame_main, Effect)


        # save button & id
        Editor.button(frame_main, "SAVE", command=lambda: self.save_information())
        self.id = Editor.label(frame_main, "ID: " + self.id.__str__())

        window.mainloop()

    def save_information(self):

        # creating new character
        new_item = itemItem(self.entry_name.get(), self.entry_description.get(), self.image, self.id, self.effect, self.is_consumable)

        # save data information
        self.data_handler.data.items.append(new_item)
        self.data_handler.save()