import tkinter as tk
from widgets.exit_botton import Exit_botton
from main_window.warehouse.info_window import Info_window
from main_window.warehouse.entry import Entry
from main_window.warehouse.insert import Create_botton_insert


class Warehouse_main():
    def create_text(self):
        self.text = tk.Entry(self.window)
        self.text.place(x = 400, y = 30)

    def create_frame(self):
        self.window = tk.Frame(self.main_window, width=1100, height=700)
        self.window.place(x = 1, y = 1)

    def create_botton_exit(self):
        self.exit = Exit_botton("Return", self.window)
        self.info_window = Info_window(self.window)
    
    def create_botton_insert(self):
        self.botton_insert = Create_botton_insert(self.window, self.text, self.info_window)

    def create_entry(self):
        self.entery = Entry(self.window, self.botton_insert)

    def __init__(self, main_window):
        self.main_window = main_window
        self.create_frame()
        self.create_text()
        self.create_botton_exit()
        self.create_botton_insert()
        
