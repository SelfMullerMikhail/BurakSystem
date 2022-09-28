import tkinter as tk
from main_window.db_helper import Db_helper
from main_window.switcher import switcher

class Table():
    helper = Db_helper()
    def buttons_create(self, tab):
        def button_function():
            switcher.switch_tab(tab)
            self.Text.delete()
            self.Text.insert(tab)
            self.Summ.delete()
            self.Summ.insert(tab)

        self.i = tk.Button(text=f"Table {tab}", command=button_function, width=15, height=3)
        self.i.grid()

    def show_all(self):
        switcher.switch_tab("all")
        self.Text.delete()
        self.Text.insert_all()

    def max_line(self):
        for i in range(7):
            self.buttons_create(i + 1)
        self.show_botton_all = tk.Button(text=f"Show All", command=self.show_all, width=15, height=3)
        self.show_botton_all.grid()

    def first_start(self):
        tab = switcher.got_tab()
        self.Text.delete()
        self.Text.insert(tab)
        self.Summ.delete()
        self.Summ.insert(tab)

    def __init__(self, self_text, self_summ):
        self.Text = self_text
        self.Summ = self_summ
        self.max_line()
        self.first_start()
