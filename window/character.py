from window import nbk_editor
from window.nbk_editor import Fill, Side
from window import nbk_editor


class Character:
    def __init__(self):
        self.name = None
        self.entry_name = None
        self.description = None
        self.entry_description = None
        self.id = None


    def open_window(self, characters):

        window = nbk_editor.create_window("Dnd Character Creator", '800x420', False)

        # sidebar
        frame_sidebar = nbk_editor.frame(window, True, Fill.BOTH, Side.LEFT)
        nbk_editor.label(frame_sidebar, "List of characters")
        nbk_editor.generate_buttons(frame_sidebar, characters)

        # title
        frame_main = nbk_editor.frame(window, True, Fill.BOTH, Side.RIGHT)
        nbk_editor.label(frame_main, "Create new character")

        # name
        frame_name = nbk_editor.frame(frame_main, True, Fill.BOTH, Side.TOP)
        nbk_editor.label(frame_name, "Name")
        self.entry_name = nbk_editor.entry(frame_name)
        self.name = nbk_editor.label(frame_name, "")

        # background
        frame_background = nbk_editor.frame(frame_main, True, Fill.BOTH, Side.TOP)
        nbk_editor.label(frame_background, "Background")
        self.entry_description = nbk_editor.entry(frame_background)
        self.description = nbk_editor.label(frame_background, "")

        # save button
        frame_save = nbk_editor.frame(frame_main, True, Fill.BOTH, Side.TOP)
        nbk_editor.button(frame_save, "SAVE", self.save_information)

        # id
        frame_background = nbk_editor.frame(frame_main, True, Fill.BOTH, Side.TOP)
        self.id = nbk_editor.label(frame_background, "ID: " + self.id.__str__())

        window.mainloop()


    def update_information(self, name: str, description: str, id: int):
        # update main frame with data information
        print("Updating information...")
        self.name["text"] = name
        self.description["text"] = description
        self.id["text"] = id

    @staticmethod
    def save_information():
        # save data information
        print("Saving information...")