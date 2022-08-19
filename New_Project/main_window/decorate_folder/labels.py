import tkinter as tk


class Label_info():
    def create_label(self):
        self.label = tk.Label(self.window, text=self.info)
        self.label.place(x = self.x, y = self.y)

    def __init__(self, window, info, x, y):
        self.window = window
        self.info = info
        self.x = x
        self.y = y
        self.create_label()

