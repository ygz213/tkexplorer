from os import walk
from ttkthemes import ThemedTk
import tkinter as tk
import content_buttons as cb
import paths_and_actions as paa

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
        path = tk.StringVar()
        path_widget = tk.Entry(state = 'disabled',
                               textvariable = path,
                               justify = 'center')
        paa.path_updater(path, path_widget)
        path_widget.pack(fill = 'x')

        for folder_names in sorted(next(walk('.'))[1]):
            cb.draw_folder_button(root, folder_names)

        root.mainloop()

setup = application(root)