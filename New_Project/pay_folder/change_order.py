import tkinter as tk

class Change_order():
    def create(self):
        self.entery = tk.Entry(self.window)
        self.entery.place(x=300, y=50)
    def __init__(self, window):
        self.window = window
        self.create()
