from window import nbk_editor
from window.nbk_editor import Fill, Side, Editor
from window.character import Character


class Menu:
    def __init__(self):
        self.character = Character()

    def open_window(self, data_handler):

        window = Editor.create_window("Dnd Creator", '240x320', False)

        # title
        frame_main = Editor.frame(window, True, Fill.BOTH, Side.RIGHT)
        Editor.label(frame_main, "Dungeons and dragons asset creator")
        Editor.button(frame_main, "Characters", command=lambda: self.character.open_window(data_handler))

        window.mainloop()