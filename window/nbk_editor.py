import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk


class Fill:
    NONE = "none",
    X = "x",
    Y = "y"
    BOTH = "both",


class Side:
    LEFT = "left",
    RIGHT = "right",
    TOP = "top",
    BOTTOM = "bottom"


class Editor:

    @staticmethod
    def create_window(title: str, size: str, is_resizable: bool):
        window = ThemedTk(theme="equilux", background=True)
        window.title(title)
        window.geometry(size)
        window.resizable = is_resizable
        style = ttk.Style()
        style.configure("TLabel", foreground="light gray")
        style.configure("TButton", foreground="light gray")
        style.configure("TEntry", foreground="light gray")
        style.configure("TCombobox", foreground="light gray")
        style.configure("TCheckbutton", foreground="light gray")
        return window

    @staticmethod
    def button(parent_frame, text: str, command):
        new_button = ttk.Button(parent_frame, text=text, command=command)
        new_button.pack()
        return new_button

    @staticmethod
    def label(parent_frame, title: str):
        new_label = ttk.Label(parent_frame, text=title, style="TLabel")
        new_label.pack()
        return new_label

    @staticmethod
    def frame(parent_frame, expand: bool, fill: Fill, side: Side):
        new_frame = ttk.Frame(parent_frame)
        new_frame.pack(expand=expand, fill=fill, side=side)
        return new_frame

    @staticmethod
    def entry(parent_frame):
        text = tk.StringVar()
        text.set("...")
        new_entry = ttk.Entry(parent_frame, textvariable=text, style="TEntry")
        new_entry.pack()
        return new_entry

    @staticmethod
    def dropbox(parent_frame, enum, starting_option):
        current = tk.StringVar(value=starting_option)
        new_dropbox = ttk.Combobox(parent_frame, textvariable=current, style="TCombobox")
        new_dropbox['values'] = [option.name for option in enum]
        new_dropbox.current()
        new_dropbox.pack()
        return new_dropbox

    @staticmethod
    def checkbox(parent_frame, text):
        new_checkbox = ttk.Checkbutton(parent_frame, text=text, onvalue=1, offvalue=0, style="TCheckbutton")
        new_checkbox.pack()
        return new_checkbox

    @staticmethod
    def generate_buttons(parent_frame, items: []):
        for i in range(len(items)):
            Editor.button(parent_frame, items[i].name, None)

