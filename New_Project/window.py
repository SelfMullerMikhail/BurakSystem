import tkinter as tk
from New_Project.main_window.text import Text
from New_Project.main_window.summ import Summ
from New_Project.main_window.table import Table
from New_Project.main_window.drinks import Drinks
from New_Project.main_window.menegment import menegment
from New_Project.main_window.clear_table import Clear_table
from New_Project.pay_folder.pay_window import Pay_botton

class Window():
    def __init__(self):
        window = tk.Tk()
        window.geometry("1100x700")
        
        self.menegment = menegment()
        self.text = Text()
        self.summ = Summ()
        self.table = Table(self.text, self.summ)
        self.drinks = Drinks(self.text, self.summ)
        self.clear_table = Clear_table(self.text, self.summ)
        self.pay_botton = Pay_botton(self.text, self.summ, window)

        window.mainloop()




if __name__ == "__main__":
    a = Window()


