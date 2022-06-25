from tkinter import ttk
import tkinter as tk

class draw_content_button():
    def __init__(self, content_type, master, text):
        self.master = master
        self.text = text

        self.folder_icon = tk.PhotoImage(file = 'icons/folder.png')

        if content_type == 'folder':
            self.draw_folder_button()

    def draw_folder_button(self):
        folder_button = ttk.Button(self.master,
                             text = f'   {self.text}',
                             image = self.folder_icon,
                             compound = 'left')
        folder_button.image = self.folder_icon
        folder_button.pack(fill = 'x', expand = True)