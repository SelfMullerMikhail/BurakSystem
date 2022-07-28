import tkinter as tk
from New_Project.widgets.exit_botton import Exit_botton
from New_Project.main_window.menegment.edit_menu.text_add_drinks import Text_add_drinks
from New_Project.main_window.menegment.edit_menu.add_drinks import Add_drinks
from New_Project.main_window.menegment.edit_menu.delete_drinks import Delete_drinks

class Add_menu():

    def create_frame(self):
        self.frame = tk.Frame(self.main_window, width=1100, height=700)
        self.frame.place(x = 1, y = 1)

    def __init__(self, main_window):
        self.main_window = main_window
        self.create_frame()
        self.list_drinks = Text_add_drinks(self.frame)
        self.add_drinks = Add_drinks(self.frame, self.list_drinks)
        self.return_botton = Exit_botton("Return", self.frame)
        self.delete_drinks = Delete_drinks(self.frame, self.list_drinks)

