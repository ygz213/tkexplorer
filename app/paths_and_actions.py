from os import chdir, getcwd, path, walk
from tkinter import ttk
import content_buttons as cb

FIRST_TIME = True        # Boolean to check if it is the first time path_updater is working

def path_updater(stringvar, entry):
    global FIRST_TIME
    if FIRST_TIME:
        chdir(path.expanduser('~'))
        FIRST_TIME = False

    stringvar.set(getcwd())
    entry.after(500, lambda: path_updater(stringvar, entry))

def list_folders(master, cwd):
    for widget in master.winfo_children():        # Clears frame
        widget.destroy()

    move_up_button = ttk.Button(master,
                                text = f'   ..',
                                command = lambda: [chdir(f'..'), list_folders(master, getcwd())],
                                width = 30)
    move_up_button.pack(ipady = 5)

    for folder_names in sorted(next(walk(cwd))[1]):        # and places buttons
        cb.draw_folder_button(master, cwd, folder_names, master)