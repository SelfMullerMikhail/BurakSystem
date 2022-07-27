import tkinter as tk

class Text():
    def delete(self):
        self.history_window.delete("1.0", tk.END)

    def insert(self, info):
        self.history_window.insert("1.0", info)

    def create_text(self):
        self.history_window = tk.Text(self.window, width=45)
        self.history_window.place(x=130, y=10)
    def __init__(self, window):
        self.window = window
        self.create_text()
