import tkinter as tk
from New_Project.hisory.text import Text
from New_Project.hisory.botton_show import Botton_show

class History():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("700x500")
        self.hostory_window = Text(self.window)
        self.botton_show = Botton_show(self.window, self.hostory_window)

        self.window.mainloop()

if __name__ == "__main__":
    window = History()