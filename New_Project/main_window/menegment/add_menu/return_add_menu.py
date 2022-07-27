import tkinter as tk

class Return_botton():
    def exit(self):
        self.main_window.destroy()

    def create_botton(self):
        self.botton = tk.Button(self.main_window, text = "Exit", command = self.exit, width=15, height=3)
        self.botton.place(x = 950, y = 10)
    def __init__(self, add_window):
        self.main_window = add_window
        self.create_botton()