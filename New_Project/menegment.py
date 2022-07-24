import tkinter as tk


class menegment():

    def add_ingridient(self):
        print("add_ingridient")
    def add_menu(self):
        print("add_menu")
    def add_shipment(self):
        print("add_shipment")

    def create(self):
        self.menu_label = tk.Menubutton(text="Menu")
        self.menu = tk.Menu(self.menu_label)
        self.menu.add_command(label="add_ingridient", command=self.add_ingridient)
        self.menu.add_command(label="add_menu", command=self.add_menu)
        self.menu.add_command(label="add_shipment", command=self.add_shipment)
        self.menu_label["menu"] = self.menu
        self.menu_label.grid()

    def __init__(self):
        self.create()
