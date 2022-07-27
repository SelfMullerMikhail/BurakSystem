import tkinter as tk
from New_Project.main_window.menegment.history.history_window import History
from New_Project.main_window.menegment.add_menu.add_menu import Add_menu


class menegment():

    def add_ingridient(self):
        print("add_ingridient")
    def add_shipment(self):
        print("add_shipment")

    def add_menu(self):
        self.add_menu = Add_menu(self.main_window)

    def history(self):
        self.window = History(self.main_window)

    def create(self):
        self.menu_label = tk.Menubutton(text="Menu")
        self.menu = tk.Menu(self.menu_label)
        self.menu.add_command(label="add_ingridient", command=self.add_ingridient)
        self.menu.add_command(label="Add_menu", command=self.add_menu)
        self.menu.add_command(label="add_shipment", command=self.add_shipment)
        self.menu.add_command(label="History", command=self.history)
        self.menu_label["menu"] = self.menu
        self.menu_label.grid()

    def __init__(self, main_window):
        self.main_window = main_window
        self.create()
