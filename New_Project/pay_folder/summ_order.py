import tkinter as tk

class Summ_order():

    def create(self):
        self.summ = tk.Entry(self.window)
        self.summ.place(x=300, y=10)

    def __init__(self, window):
        self.window = window
        self.create()
