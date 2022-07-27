import tkinter as tk

class Exit_botton():
    def exit(self):
        self.history_window.destroy()

    def create(self):
        self.button = tk.Button(self.history_window, text = f"{self.name}", width=15, height=3, command = self.exit)
        self.button.place(x = 950, y = 10)

    def __init__(self, name, history_window):
        self.name = name
        self.history_window = history_window
        self.create()