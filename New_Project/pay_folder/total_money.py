import tkinter as tk

class Total_money():
    def get_money(self):
        self.money = self.entery.get()
        return self.money
    def create(self):
        self.entery = tk.Entry(self.window)
        self.entery.place(x=300, y=30)
    def __init__(self, window):
        self.window = window
        self.create()
