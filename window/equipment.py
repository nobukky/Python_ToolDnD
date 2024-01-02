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
        self.frame_main = None
        self.label_effect = None
        self.label_range = None
        self.label_resistance = None
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
        Editor.label(frame_main, "Create new equipment")
        self.frame_main = frame_main

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

        ### WEAPON
        # strength
        self.strength = Dice.roll_dice(3, 4)

        # effect
        self.label_effect = Editor.label(self.frame_main, "Effect")
        self.range = Editor.dropbox(self.frame_main, Effect)
        self.label_effect.pack_forget()
        self.range.pack_forget()

        # range
        self.label_range = Editor.label(self.frame_main, "Range")
        self.effect = Editor.dropbox(self.frame_main, Range)
        self.label_range.pack_forget()
        self.effect.pack_forget()

        ### SHIELD
        # defense
        self.defense = Dice.roll_dice(2, 4)

        ### ARMOR
        # defense
        self.defense = Dice.roll_dice(2, 4)

        # resistance
        self.label_resistance = Editor.label(self.frame_main, "Resistance")
        self.range = Editor.dropbox(self.frame_main, Effect)
        self.label_resistance.pack_forget()
        self.range.pack_forget()


        # save button & id
        Editor.button(frame_main, "SAVE", command=lambda: self.save_information())
        Editor.label(frame_main, "ID: " + self.id.__str__())

        self.window.mainloop()

    def display_details(self, event):
        print(f"updating with {self.type.get()}...")
        match self.type.get():
            case EquipmentType.WEAPON:
                # effect
                self.label_effect.pack()
                self.range.pack()
                # range
                self.label_range.pack()
                self.effect.pack()

            case EquipmentType.ARMOR:
                # resistance
                self.label_resistance.pack()
                self.range.pack()


    def save_information(self):

        # creating new character
        new_equipment = itemEquipment(self.entry_name.get(), self.entry_description.get(), self.image, self.id, self.type, self.effect, self.range, self.strength, self.defense)

        # save data information
        self.data_handler.data.equipments.append(new_equipment)
        self.data_handler.save()