import tkinter as tk

class Return_history():
    def return_history(self):
        self.history_window.destroy()

    def create(self):
        self.button = tk.Button(self.history_window, text = "Return", width=15, height=3, command = self.return_history)
        self.button.place(x = 950, y = 10)

    def __init__(self, history_window):
        self.history_window = history_window
        self.create()