from window.nbk_editor import Fill, Side, Editor
from item.equipment import Equipment as itemEquipment
from item.equipment import Effect, Range, EquipmentType
from misc.dice import Dice


class Equipment:
    def __init__(self):
        self.name = None
        self.description = None
        self.image = None
        self.id = Dice.roll_dice(1, 999999)

        self.type = None
        self.effect = None
        self.range = None
        self.strength = None
        self.defense = None

        self.window = None
        self.data_handler = None
        self.entry_name = None
        self.entry_description = None

    def open_window(self, data_handler):

        self.data_handler = data_handler

        self.window = Editor.create_window("Dnd Character Creator", '800x420', False)

        # sidebar
        frame_sidebar = Editor.frame(self.window, True, Fill.BOTH, Side.LEFT)
        Editor.label(frame_sidebar, "List of equipments")
        Editor.generate_buttons(frame_sidebar, data_handler.data.equipments)


        # title
        frame_main = Editor.frame(self.window, True, Fill.BOTH, Side.RIGHT)
        self.frame_main = frame_main
        Editor.label(frame_main, "Create new equipment")

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

        # type
        Editor.label(frame_main, "Type")
        self.type = Editor.dropbox(frame_main, EquipmentType, on_change_command=self.display_details)


        # save button & id
        Editor.button(frame_main, "SAVE", command=lambda: self.save_information())
        self.id = Editor.label(frame_main, "ID: " + self.id.__str__())

        self.window.mainloop()

    def display_details(self, event):
        print(f"updating with {self.type.get()}...")
        match self.type.get():
            case EquipmentType.WEAPON:
                # strength
                self.strength = Dice.roll_dice(3, 4)
                # effect
                Editor.label(self.frame_main, "Effect")
                self.range = Editor.dropbox(self.frame_main, Effect)
                # range
                Editor.label(self.frame_main, "Range")
                self.effect = Editor.dropbox(self.frame_main, Range)

            case EquipmentType.SHIELD:
                # defense
                self.defense = Dice.roll_dice(2, 4)

            case EquipmentType.ARMOR:
                # defense
                self.defense = Dice.roll_dice(2, 4)
                # resistance
                Editor.label(self.frame_main, "Resistance")
                self.range = Editor.dropbox(self.frame_main, Effect)

    def save_information(self):

        # creating new character
        new_equipment = itemEquipment(self.entry_name.get(), self.entry_description.get(), self.image, self.id, self.type, self.effect, self.range, self.strength, self.defense)

        # save data information
        self.data_handler.data.equipments.append(new_equipment)
        self.data_handler.save()