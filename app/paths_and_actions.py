from os import getcwd, walk
from tkinter import ttk
import tkinter as tk
import content_buttons as cb

def path_updater(stringvar, entry):
    stringvar.set(getcwd())
    entry.after(1000, lambda: path_updater(stringvar, entry))

def list_folders(master, cwd):
    for widget in master.winfo_children():
        widget.destroy()

    for folder_names in sorted(next(walk(cwd))[1]):
        cb.draw_folder_button(master, cwd, folder_names, master)