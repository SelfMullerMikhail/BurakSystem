from re import X
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

        self.i = tk.Button(self.window_for_tables, text=f"Table {tab}", command=button_function, width=15, height=3)
        self.i.pack()

    def show_all(self):
        switcher.switch_tab("all")
        self.Text.delete()
        self.Text.insert_all()

    def max_line(self):
        for i in range(7):
            self.buttons_create(i + 1)
        self.show_botton_all = tk.Button(self.window_for_tables, text=f"Show All", command=self.show_all, width=15, height=3)
        self.show_botton_all.pack()

    def first_start(self):
        tab = switcher.got_tab()
        self.Text.delete()
        self.Text.insert(tab)
        self.Summ.delete()
        self.Summ.insert(tab)

    def __init__(self, tables_from, self_text, self_summ):
        self.tables_from = tables_from

        self.window_for_tables = tk.Frame(self.tables_from, width=300, height=100, background="red")
        self.window_for_tables.place(x=1, y=1)

        self.Text = self_text
        self.Summ = self_summ
        self.max_line()
        self.first_start()
