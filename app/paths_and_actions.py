from os import getcwd
from tkinter import ttk
import tkinter as tk

def path_updater(stringvar, entry):
    stringvar.set(getcwd())
    entry.after(1000, lambda: path_updater(stringvar, entry))