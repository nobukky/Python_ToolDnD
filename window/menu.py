from window.nbk_editor import Fill, Side, Editor
from window.character import Character
from window.item import Item
from window.equipment import Equipment


class Menu:
    def __init__(self):
        self.character = Character()
        self.item = Item()
        self.equipment = Equipment()

    def open_window(self, data_handler):

        window = Editor.create_window("Dnd Creator", '250x150', True)

        # title
        frame_main = Editor.frame(window, True, Fill.NONE, Side.TOP)
        Editor.label(frame_main, title="Dungeons and dragons asset creator", row=0, column=0)
        Editor.button(frame_main, text="Create a new character", command=lambda: self.character.open_window(data_handler), row=1, column=0)
        Editor.button(frame_main, text="Create a new equipment", command=lambda: self.equipment.open_window(data_handler), row=3, column=0)

        ### don't work due to changes
        #Editor.button(frame_main, text="Create a new item", command=lambda: self.item.open_window(data_handler), row=2, column=0)

        window.mainloop()