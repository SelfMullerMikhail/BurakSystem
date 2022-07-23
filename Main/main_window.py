import tkinter as tk
from db_helper import db_helper
from create_menu_botton import create_menu_botton, tables_botton
from upgrade_all import upgrade
from widget import Label
from Menegment.main_window_manegment import Menegment
from calculator import Calculater


class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.helper = db_helper()
        self.menu = Menegment()

        self.window_enter = tk.Text(self, width=45)
        self.window_enter.place(x=130, y=10)
        self.window_summ = tk.Entry(self)
        self.window_summ.place(x=370, y=400)
        self.label_window = Label.label(self, "BurakSystem")
        self.menu_upgrade = upgrade()
        self.menu_botton = create_menu_botton(self.window_enter, self.window_summ)
        self.tables_botton = tables_botton(self.window_enter, self.window_summ)
        self.calculator = Calculater(self.window_enter, self.window_summ, self.menu_botton)


if __name__ == "__main__":
    window = Window()
    window.geometry("1000x600")
    window.mainloop()
