from os import path
from ttkthemes import ThemedTk
import tkinter as tk
import content_buttons as cb
import paths_and_actions as paa

root = ThemedTk(theme = 'arc')

class application():
    def __init__(self, root):
        root.title('tkexplorer')
        try:
            root.iconbitmap(f'{path.dirname(path.realpath(__file__))}/icons/icon.ico')
        except:
            root.iconbitmap(f'{path.dirname(path.realpath(__file__))}@icons/icon.xbm')

        self.widgets()

    def widgets(self):
        cwd = tk.StringVar()
        cwd_widget = tk.Entry(state = 'disabled',
                               textvariable = cwd,
                               justify = 'center')
        paa.path_updater(cwd, cwd_widget)
        cwd_widget.pack(fill = 'x')

        buttons_frame = tk.Frame()
        paa.list_folders(buttons_frame, cwd.get())
        buttons_frame.pack()

        root.mainloop()

setup = application(root)