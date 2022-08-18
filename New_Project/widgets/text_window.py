import tkinter as tk
from main_window.db_helper import Db_helper

class Text_window():

    def insert(self):
        pass
    def create(self):
        self.text = tk.Text(self.window, width=45)
        self.text.place(x=self.x, y=self.y)

    def delete(self):
        self.text.delete("1.0", tk.END)

    def __init__(self, window, x, y):
        self.window = window
        self.x = x 
        self.y = y
        self.helper = Db_helper()
        self.add_drinks_window = window
        self.create()
        self.insert()