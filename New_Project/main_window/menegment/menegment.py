import tkinter as tk
from main_window.menegment.history.history_window import History
from main_window.menegment.edit_menu.add_window import Add_menu
from main_window.menegment.orders_history.orders_history import Check_money_window
from main_window.warehouse.warehouse_main import Warehouse_main


class Menegment():

    def exit(self):
        self.main_window.destroy()

    def add_menu(self):
        self.add_menu = Add_menu(self.main_window)

    def history(self):
        self.window = History(self.main_window)
    
    def orders_history(self):
        self.check_money = Check_money_window(self.main_window, "full_story")

    def warehouse(self):
        self.warehouse_main = Warehouse_main(self.main_window)

    def create(self):
        self.menu_label = tk.Menubutton(self.upPanel_frame, text="Menu", height=2, width=14)
        self.menu = tk.Menu(self.menu_label)
        self.menu.add_command(label="Tables history", command=self.history)
        self.menu.add_command(label="Orders history", command=self.orders_history)
        self.menu.add_command(label="Edit_menu", command=self.add_menu)
        self.menu.add_command(label="Exit", command=self.exit)
        self.menu.add_command(label="Warehouse", command=self.warehouse)
        self.menu_label["menu"] = self.menu
        self.menu_label.place(x = 985, y = 2)

    def __init__(self, main_window, upPanel_frame):
        self.main_window = main_window
        self.upPanel_frame = upPanel_frame
        self.create()
