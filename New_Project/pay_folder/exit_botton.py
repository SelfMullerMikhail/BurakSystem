import tkinter as tk

class Exit_botton():
    def destroy(self):
        self.window.destroy()
    def __init__(self, window):
        self.window = window
        self.exit = tk.Button(self.window, text="Exit",width=15, height=3,  command=self.destroy)
        self.exit.place(x = 550, y = 10)