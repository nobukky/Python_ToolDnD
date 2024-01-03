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
        style.configure("TRadiobutton", foreground="light gray")
        return window

    @staticmethod
    def button(parent_frame, row: int, column: int, text: str, command):
        new_button = ttk.Button(parent_frame, text=text, command=command)
        new_button.grid(row=row, column=column)
        return new_button

    @staticmethod
    def label(parent_frame, title: str, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str="nsew"):
        new_label = ttk.Label(parent_frame, text=title, style="TLabel")
        new_label.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_label

    @staticmethod
    def frame(parent_frame, expand: bool, fill: Fill, side: Side):
        new_frame = ttk.Frame(parent_frame)
        new_frame.pack(expand=expand, fill=fill, side=side)
        return new_frame

    @staticmethod
    def entry(parent_frame, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str="nsew"):
        text = tk.StringVar()
        text.set("...")
        new_entry = ttk.Entry(parent_frame, textvariable=text, style="TEntry")
        new_entry.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_entry

    @staticmethod
    def dropbox(parent_frame, enum, on_change_command, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str="nsew"):
        current = tk.StringVar()
        new_dropbox = ttk.Combobox(parent_frame, textvariable=current, style="TCombobox")
        new_dropbox['values'] = [option.name for option in enum]
        new_dropbox.bind('<<ComboboxSelected>>', on_change_command)
        new_dropbox.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        new_dropbox.current(0)
        return new_dropbox

    @staticmethod
    def checkbox(parent_frame, text: str, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str="nsew"):
        new_checkbox = ttk.Checkbutton(parent_frame, text=text, onvalue=1, offvalue=0, style="TCheckbutton")
        new_checkbox.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_checkbox

    @staticmethod
    def radiobutton(parent_frame, text :str, value, variable, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str="nsew"):
        new_radiobutton = ttk.Radiobutton(parent_frame, text=text, variable=variable, value=value, style="TRadiobutton")
        new_radiobutton.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_radiobutton

    @staticmethod
    def string_var():
        return tk.StringVar()

    @staticmethod
    def generate_buttons(parent_frame, items: []):
        for i in range(len(items)):
            Editor.button(parent_frame, text=items[i].name, command=None, row=i+1, column=0)

    @staticmethod
    def get_enum_value_from_names(enum, current: str):
        for item in enum:
            if item.name == current:
                return item
        return enum[0]