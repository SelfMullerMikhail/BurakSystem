import tkinter as tk

class Exit_botton():
    def exit(self):
        self.main_window.destroy()

    def create_botton(self):
        self.botton = tk.Button(self.main_window, text = "Exit", command = self.exit, width=15, height=3)
        self.botton.place(x = 950, y = 10)
    def __init__(self, main_window):
        self.main_window = main_window
        self.create_botton()