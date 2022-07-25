import tkinter as tk
from text import Text
from summ import Summ
from table import Table
from drinks import Drinks
from menegment import menegment
from clear_table import Clear_table
from New_Project.pay_folder.pay_window import Pay_botton


class Window(tk.Tk):


    def __init__(self):
        super().__init__()
        self.menegment = menegment()
        self.text = Text()
        self.summ = Summ()
        self.table = Table(self.text, self.summ)
        self.drinks = Drinks(self.text, self.summ)
        self.clear_table = Clear_table(self.text, self.summ)
        self.pay_botton = Pay_botton()





if __name__ == "__main__":
    window = Window()
    window.geometry("1100x700")
    window.mainloop()