from os import chdir, getcwd, path
from tkinter import ttk
import tkinter as tk
import paths_and_actions as paa

def draw_folder_button(master, cwd, text, frame_to_pass):
    button_frame = tk.Frame(master)
    folder_icon = tk.PhotoImage(file = f'{path.dirname(path.realpath(__file__))}/icons/folder.png')

    folder_widget = ttk.Label(button_frame, image = folder_icon)
    folder_widget.image = folder_icon
    folder_widget.pack(side = 'left')

    folder_button = ttk.Button(button_frame,
                               text = f'   {text}',
                               command = lambda: [chdir(f'{cwd}/{text}'), paa.list_folders(frame_to_pass, getcwd())],
                               width = 45)
    folder_button.pack(side = 'left', ipady = 5)
    button_frame.pack()