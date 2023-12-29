import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from enum import Enum


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


def create_window(title: str, size: str, is_resizable: bool):
    window = ThemedTk(theme="equilux", background=True)
    window.title(title)
    window.geometry(size)
    window.resizable = is_resizable
    style = ttk.Style()
    style.configure("TLabel", foreground="light gray")
    style.configure("TButton", foreground="light gray")
    style.configure("TEntry", foreground="light gray")
    return window

def button(parent_frame, text: str, command):
    new_button = ttk.Button(parent_frame, text=text, command=command)
    new_button.pack()
    return new_button

def label(parent_frame, title: str):
    new_label = ttk.Label(parent_frame, text=title, style="TLabel")
    new_label.pack()
    return new_label

def frame(parent_frame, expand: bool, fill: Fill, side: Side):
    new_frame = ttk.Frame(parent_frame)
    new_frame.pack(expand=expand, fill=fill, side=side)
    return new_frame

def entry(parent_frame):
    text = tk.StringVar()
    text.set("...")
    new_entry = ttk.Entry(parent_frame, textvariable=text, style="TEntry")
    new_entry.pack()
    return new_entry

def generate_buttons(parent_frame, items: []):
    for i in range(len(items)):
        button(parent_frame, items[i].name, None)

