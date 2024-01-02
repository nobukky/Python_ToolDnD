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

        window = Editor.create_window("Dnd Creator", '240x320', False)

        # title
        frame_main = Editor.frame(window, True, Fill.BOTH, Side.RIGHT)
        Editor.label(frame_main, "Dungeons and dragons asset creator")
        Editor.button(frame_main, "Characters", command=lambda: self.character.open_window(data_handler))
        Editor.button(frame_main, "Items", command=lambda: self.item.open_window(data_handler))
        Editor.button(frame_main, "Equipments", command=lambda: self.equipment.open_window(data_handler))

        window.mainloop()