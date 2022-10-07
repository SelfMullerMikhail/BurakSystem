from tkinter import *
from PIL import ImageTk, Image


def PhotoHelper(photo):
    menu_img = ImageTk.PhotoImage(Image.open(photo))
    return menu_img
