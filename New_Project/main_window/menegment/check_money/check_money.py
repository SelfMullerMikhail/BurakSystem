from select import select
import tkinter as tk
from widgets.exit_botton import Exit_botton
from widgets.text_window import Text_window

class Check_money_window():
    def open_window(self):
        self.window = tk.Frame(self.main_window, width=1100, height=700)
        self.window.place(x = 1, y = 1)
        self.exit_botton = Exit_botton("Return", self.window)
        self.text_window = Text_window(self.main_window, 10, 20)

    def __init__(self, main_window):
        self.main_window = main_window
        self.open_window()
        