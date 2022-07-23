import tkinter as tk
from db_helper import db_helper
from text import text
from summ import summ
from tab import switch_tab

class table():
    helper = db_helper()
    table = switch_tab()
    def buttons_create(self, tab):
        def button_function():
            self.table.switch_tab(tab)
            self.text.delete()
            self.text.insert(tab)
            self.summ.delete()
            self.summ.insert(tab)

        self.i = tk.Button(text=f"Table {tab}", command=button_function, width=15, height=3)
        self.i.grid()

    def max_line(self):
        self.max_line = self.helper.execute_query_fetchone("SELECT max(id) FROM sell_table")
        for i in range(self.max_line[0]):
            self.buttons_create(i + 1)

    def __init__(self):
        self.summ = summ()
        self.text = text()
        self.max_line()
