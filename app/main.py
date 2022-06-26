from os import walk
from ttkthemes import ThemedTk
import tkinter as tk
import content_buttons as cb

root = ThemedTk(theme = 'arc')

class application():
    def __init__(self, root):
        root.title('tkexplorer')
        try:
            root.iconbitmap('icons/icon.ico')
        except:
            root.iconbitmap('@icons/icon.xbm')

        self.widgets()

    def widgets(self):
        content_frame = tk.Frame()
        for folder_names in sorted(next(walk('.'))[1]):
            cb.draw_folder_button(content_frame, folder_names)
        content_frame.pack()

        root.mainloop()

setup = application(root)