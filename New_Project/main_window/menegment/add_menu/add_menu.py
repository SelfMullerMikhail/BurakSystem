import tkinter as tk
# from New_Project.main_window.menegment.add_menu.return_add_menu import Return_botton
from New_Project.widgets.exit_botton import Exit_botton

class Add_menu():

    def create_frame(self):
        self.frame = tk.Frame(self.main_window, width=1100, height=700)
        self.frame.place(x = 1, y = 1)

    def __init__(self, main_window):
        self.main_window = main_window
        self.create_frame()
        self.return_botton = Exit_botton("Return", self.frame)