from tkinter import ttk
import tkinter as tk

def draw_folder_button(master, text):
    button_frame = tk.Frame(master)
    folder_icon = tk.PhotoImage(file = 'icons/folder.png')

    folder_widget = ttk.Label(button_frame, image = folder_icon)
    folder_widget.image = folder_icon
    folder_widget.pack(side = 'left')

    folder_button = ttk.Button(button_frame,
                               text = f'   {text}',
                               width = 45)
    folder_button.pack(side = 'left', ipady = 5)
    button_frame.pack()