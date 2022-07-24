import tkinter as tk
from db_helper import Db_helper
from text import Text
from summ import Summ
from tab import Switch_tab

class Table():
    helper = Db_helper()
    table = Switch_tab()
    def buttons_create(self, tab):
        def button_function():
            self.table.switch_tab(tab)
            self.Text.delete()
            self.Text.insert(tab)
            self.Summ.delete()
            self.Summ.insert(tab)
            print(f"Table is work! tab: {tab}")

        self.i = tk.Button(text=f"Table {tab}", command=button_function, width=15, height=3)
        self.i.grid()

    def max_line(self):
        self.max_line = self.helper.execute_query_fetchone("SELECT max(id) FROM sell_table")
        for i in range(self.max_line[0]):
            self.buttons_create(i + 1)

    def __init__(self, self_text, self_summ):
        self.Text = self_text
        self.Summ = self_summ


        self.max_line()
