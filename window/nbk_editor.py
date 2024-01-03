import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
import numpy as np
import pathlib
import json


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
    def create_window(title: str, size: str, is_main_window: bool=True):
        if is_main_window:
            window = ThemedTk(theme="equilux", background=True)
        else:
            window = tk.Toplevel()

        window.title(title)
        window.geometry(size)
        style = ttk.Style()
        style.configure("TLabel", foreground="light gray")
        style.configure("TButton", foreground="light gray")
        style.configure("TEntry", foreground="light gray")
        style.configure("TCombobox", foreground="light gray")
        style.configure("TCheckbutton", foreground="light gray")
        style.configure("TRadiobutton", foreground="light gray")
        return window

    @staticmethod
    def button(root, text: str, command, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str= "nsew"):
        new_button = ttk.Button(root, text=text, command=command)
        new_button.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_button

    @staticmethod
    def label(root, title: str, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str= "nsew"):
        new_label = ttk.Label(root, text=title, style="TLabel")
        new_label.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_label

    @staticmethod
    def frame(root, expand: bool, fill: Fill, side: Side):
        new_frame = ttk.Frame(root)
        new_frame.pack(expand=expand, fill=fill, side=side)
        return new_frame

    @staticmethod
    def entry(root, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str= "nsew"):
        text = tk.StringVar()
        text.set("...")
        new_entry = ttk.Entry(root, textvariable=text, style="TEntry")
        new_entry.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_entry

    @staticmethod
    def dropbox(root, enum, on_change_command, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str= "nsew"):
        current = tk.StringVar()
        new_dropbox = ttk.Combobox(root, textvariable=current, style="TCombobox")
        new_dropbox['values'] = [option.name for option in enum]
        new_dropbox.current(0)
        new_dropbox.bind('<<ComboboxSelected>>', on_change_command)
        new_dropbox.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_dropbox

    @staticmethod
    def checkbox(root, text: str, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str= "nsew"):
        new_checkbox = ttk.Checkbutton(root, text=text, onvalue=1, offvalue=0, style="TCheckbutton")
        new_checkbox.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_checkbox

    @staticmethod
    def radiobutton(root, text :str, value, variable, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str= "nsew"):
        new_radiobutton = ttk.Radiobutton(root, text=text, variable=variable, value=value, style="TRadiobutton")
        new_radiobutton.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_radiobutton

    @staticmethod
    def image(root, image, row: int, column: int, row_span: int=1, column_span: int=1, pad_x: int=0, pad_y: int=0, sticky: str= "nsew"):
        new_image = ttk.Label(root, image=image)
        new_image.grid(row=row, column=column, rowspan=row_span, columnspan=column_span, padx=pad_x, pady=pad_y, sticky=sticky)
        return new_image

    @staticmethod
    def update_image_from_path(label_image, image_path: str = ""):
        # null exception
        if image_path == "":
            return

        # get image from path
        image = Image.open(image_path)
        Editor._update_image(label_image, image)

    @staticmethod
    def update_image_from_json(label_image, image_json: str = ""):
        # null exception
        if image_json == "":
            return

        # empty exception
        if image_json == "empty":
            # hide former image, if it is empty
            label_image.configure(image='')
            label_image.image = ''
            return

        # get the image from json
        image = Image.fromarray(np.array(json.loads(image_json), dtype='uint8'))
        Editor._update_image(label_image, image)

    @staticmethod
    def _update_image(label_image, image, limit_size: int = 200):
        # optimize image size
        width = image.size[0]
        height = image.size[1]
        while width >= limit_size and height >= limit_size:
            width *= 0.75
            height *= 0.75
        width = int(round(width))
        height = int(round(height))

        # resize image to the optimized size
        image_resized = image.resize((width, height), Image.Resampling.LANCZOS)
        image_tk = ImageTk.PhotoImage(image_resized)

        # update the given label image
        label_image.configure(image=image_tk)
        label_image.image = image_tk

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