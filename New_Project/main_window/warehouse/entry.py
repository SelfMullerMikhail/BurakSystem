import tkinter as tk

class Entry():
    def create(self):
        self.entry = tk.Entry(self.warehouse_window)
        self.entry.place(x = 350, y = 350)

    def get_info(self):
        return self.entry.get()

    def insert(self):
        self.info = self.get_info()
        self.botton.insert(self.info)


    def __init__(self, warehouse_window, bottoon):
        self.botton = bottoon
        self.warehouse_window = warehouse_window
        self.create()