import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


class Window:
    def __init__(self):
        self.window = ThemedTk(theme="equilux", background=True)
        self.window.title("Dungeons and Dragons asset creator")
        self.window.geometry('800x420')
        self.window.resizable = True

        # style personalization
        self.style = ttk.Style()
        self.style.configure("TLabel", foreground="light gray")
        self.style.configure("TButton", foreground="light gray")
        self.style.configure("TEntry", foreground="light gray")

    def open_window(self, data):

        frame_sidebar = self.draw_frame(self.window, True, tk.BOTH, tk.LEFT)
        self.draw_label(frame_sidebar, "CHARACTERS")
        self.draw_lists(frame_sidebar, data.characters)
        self.draw_label(frame_sidebar, "ITEMS")
        self.draw_lists(frame_sidebar, data.items)
        self.draw_label(frame_sidebar, "EQUIPMENTS")
        self.draw_lists(frame_sidebar, data.equipments)

        self.window.mainloop()

    def draw_lists(self, parent_frame, list: []):
        for i in range(len(list)):
            button = ttk.Button(parent_frame, text=list[i].name, command=self.update_information)
            button.pack()
        pass

    @staticmethod
    def update_information():
        pass

    @staticmethod
    def draw_label(parent_frame, title: str):
        label = ttk.Label(parent_frame, text=title, style="TLabel")
        label.pack()

    @staticmethod
    def draw_frame(parent_frame, expand: bool, fill, side):
        frame = ttk.Frame(parent_frame)
        frame.pack(expand=expand, fill=fill, side=side)
        return frame