from platform import python_branch
from main_window import *
# pip install mysql-connector-python_branch

import tkinter as tk
from main_window.text import Text
from main_window.summ import Summ
from main_window.table import Table
from main_window.menegment.menegment import menegment
from main_window.clear_table import Clear_table
from main_window.pay_folder.pay_window import Pay_botton
from main_window.frame_menu import Frame_menu

class Window():
    def __init__(self):
        window = tk.Tk()
        window.geometry("1100x700")

        self.text = Text()
        self.summ = Summ()
        self.frame_menu = Frame_menu(self.text, self.summ, window)
        self.menegment = menegment(window)
        self.table = Table(self.text, self.summ)
        self.clear_table = Clear_table(self.text, self.summ)
        self.pay_botton = Pay_botton(self.text, self.summ, window)

        window.mainloop()

if __name__ == "__main__":
    Window()


