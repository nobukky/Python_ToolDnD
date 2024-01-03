from window.nbk_editor import Fill, Side, Editor
from item.character import Character as itemCharacter
from item.character import Race, Affinity
from misc.dice import Dice


class Character:
    def __init__(self):
        self.name = None
        self.description = None
        self.image = None
        self.id = Dice.roll_dice(1, 999999)
        self.race = None
        self.affinity = None
        self.do_randomize_stats = False
        self.statistics: list[int] = list()
        self.labels_statistics = []
        self.row_index = None

        self.data_handler = None
        self.variable_method = None
        self.entry_name = None
        self.entry_description = None

    def open_window(self, data_handler):

        self.data_handler = data_handler

        window = Editor.create_window("Dnd Character Creator", '425x450', False)

        # sidebar
        frame_sidebar = Editor.frame(window, True, Fill.BOTH, Side.LEFT)
        Editor.label(frame_sidebar, title="List of characters", row=0, column=0,)
        Editor.generate_buttons(frame_sidebar, data_handler.data.characters)


        # title
        frame_main = Editor.frame(window, True, Fill.BOTH, Side.TOP)
        Editor.label(frame_main, title="Create new character", row=0, column=0,)


        # main infos
        frame_main_infos = Editor.frame(window, True, Fill.BOTH, Side.TOP)

        # name
        Editor.label(frame_main_infos, title="Name", row=0, column=0)
        self.entry_name = Editor.entry(frame_main_infos, row=0, column=1)
        self.name = Editor.label(frame_main_infos, title="", row=1, column=1)

        # background
        Editor.label(frame_main_infos, title="Background", row=2, column=0)
        self.entry_description = Editor.entry(frame_main_infos, row=2, column=1)
        self.description = Editor.label(frame_main_infos, title="", row=3, column=1)

        # image
        Editor.label(frame_main_infos, title="Image", row=4, column=0)

        # race
        Editor.label(frame_main_infos, title="Race", row=5, column=0)
        self.race = Editor.dropbox(frame_main_infos, enum=Race, on_change_command=None, row=5, column=1)

        # affinity
        Editor.label(frame_main_infos, row=6, column=0, title="Class")
        self.affinity = Editor.dropbox(frame_main_infos, enum=Affinity, on_change_command=None, row=6, column=1)


        # statistics
        frame_statistics = Editor.frame(window, True, Fill.BOTH, Side.TOP)
        Editor.label(frame_statistics, title="STATISTICS", row=0, column=0)

        frame_statistics_method = Editor.frame(window, True, Fill.BOTH, Side.TOP)
        Editor.label(frame_statistics_method, title="Which randomize method do you use?", row=0, column=0)
        self.variable_method = Editor.string_var()
        Editor.radiobutton(frame_statistics_method, text="1d20", value=0, variable=self.variable_method, row=0, column=1)
        Editor.radiobutton(frame_statistics_method, text="3d6", value=1, variable=self.variable_method, row=0, column=2)

        frame_statistics_generation = Editor.frame(window, True, Fill.BOTH, Side.TOP)
        Editor.button(frame_statistics_generation, text="(re)Generate", command=lambda: self.generate_statistics(frame_statistics_generation, starting_row=2), row=0, column=0)
        Editor.label(frame_statistics_generation, title="Your statistics:", row=1, column=0)
        self.generate_statistics(frame_statistics_generation, starting_row=2, do_generate_empty=True)


        # save button & id
        frame_footer = Editor.frame(window, True, Fill.BOTH, Side.BOTTOM)
        Editor.button(frame_footer, text="SAVE", command=lambda: self.save_information(), row=0, column=0)
        Editor.label(frame_footer, title="ID: " + self.id.__str__(), row=1, column=0)

        window.mainloop()

    def generate_statistics(self, parent_frame, starting_row: int=0, do_generate_empty: bool=False):
        self.statistics = []
        if do_generate_empty:
            for i in range(0, 5):
                self.statistics.append(0)
        else:
            if self.variable_method.get() == 0:
                for i in range(0, 5):
                    self.statistics.append(Dice.roll_dice(1, 20))
            else:
                for i in range(0, 5):
                    self.statistics.append(Dice.roll_dice(3, 6))

        self.display_statistics(parent_frame, starting_row, do_generate_empty)

    def display_statistics(self, parent_frame, starting_row: int, do_generate_empty: bool=False):
        row_index = starting_row
        if len(self.statistics) != 0:
            for i in range(len(self.statistics)):

                # destroy former labels, if they exist
                if len(self.labels_statistics) > i and do_generate_empty is False:
                    self.labels_statistics[i].destroy()

                # get statistic name
                statistic_name = ""
                match i:
                    case 0:
                        statistic_name = "Strength"
                    case 1:
                        statistic_name = "Dexterity"
                    case 2:
                        statistic_name = "Intelligence"
                    case 3:
                        statistic_name = "Luck"
                    case 4:
                        statistic_name = "Health points"

                # add new labels
                self.labels_statistics.append(Editor.label(parent_frame, title=f"{statistic_name}: {self.statistics[i]}", row=row_index, column=0))
                row_index += 1

    def save_information(self):
        # get enum value from their names
        self.race = Editor.get_enum_value_from_names(Race, self.race.get())
        self.affinity = Editor.get_enum_value_from_names(Affinity, self.affinity.get())

        # creating new character
        new_character = itemCharacter(self.entry_name.get(), self.entry_description.get(), self.image, self.id, self.race, self.affinity, self.statistics)

        # save data information
        self.data_handler.data.characters.append(new_character)
        self.data_handler.save()