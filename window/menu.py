from window import nbk_editor
from window.nbk_editor import Fill, Side
from window.character import Character


class Menu:
    def __init__(self):
        self.character = Character()

    def open_window(self, data):

        window = nbk_editor.create_window("Dnd Creator", '240x320', False)

        # title
        frame_main = nbk_editor.frame(window, True, Fill.BOTH, Side.RIGHT)
        nbk_editor.label(frame_main, "Dungeons and dragons asset creator")
        nbk_editor.button(frame_main, "Characters", command=lambda: self.character.open_window(data.characters))

        window.mainloop()