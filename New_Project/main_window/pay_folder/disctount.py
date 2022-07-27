import tkinter as tk

class Descount():
    def make(self):
        print("DISCOUNT")

    def __init__(self, window):
        self.discount = tk.Button(text = "Discount", width=15, height=3, command = self.make)
        self.window = window

