from select import select
import tkinter as tk
from widgets.exit_botton import Exit_botton
from widgets.text_window import Text_window

class Check_money_window():

    def create_window(self):
        self.window = tk.Frame(self.main_window, width=1100, height=700)
        self.window.place(x = 1, y = 1)

    def __init__(self, main_window):
        self.main_window = main_window
        self.create_window()
        self.text_window = Text_window(self.window, 10, 20)
        self.exit_botton = Exit_botton("Return", self.window)
        