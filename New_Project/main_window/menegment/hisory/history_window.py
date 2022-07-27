import tkinter as tk
from New_Project.main_window.menegment.hisory.text import Text
from New_Project.main_window.menegment.hisory.return_history import Return_history
from New_Project.main_window.menegment.hisory.entery_data import Entery_data

class History():

    def create_frame(self):
        self.window = tk.Frame(self.main_window, width=1100, height=700)
        self.window.place(x=1, y=1)

    def __init__(self, main_window):
        self.main_window = main_window
        self.create_frame()
        self.history_window = Text(self.window)
        self.entery_data = Entery_data(self.window, self.history_window)
        self.return_history = Return_history(self.window)

        self.window.mainloop()

if __name__ == "__main__":
    window = History()