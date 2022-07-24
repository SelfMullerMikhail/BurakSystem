import tkinter as tk
# from enter import enter
from text import text
from summ import summ
from table import table
from drinks import drinks
from menegment import menegment


class window(tk.Tk):
    def test(self):
        self.summ.insert(1)


    def __init__(self):
        super().__init__()
        self.menegment = menegment()
        self.text = text()
        self.summ = summ()
        self.table = table()
        self.drinks = drinks()





if __name__ == "__main__":
    window = window()
    window.geometry("1100x700")
    window.mainloop()