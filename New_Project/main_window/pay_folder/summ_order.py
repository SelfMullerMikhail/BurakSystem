import tkinter as tk
import re
from New_Project.main_window.table import switcher
from New_Project.main_window.db_helper import Db_helper

class Summ_order():

    def delete(self):
        self.summ.delete(0, tk.END)

    def create(self):
        self.summ = tk.Entry(self.window)
        self.summ.place(x=300, y=10)
        self.tab = switcher.got_tab()
        self.text_bd = self.helper.execute_query_fetchone(f'SELECT sum(cost) FROM show_orders WHERE tables = {self.tab}')[0]
        if self.text_bd != None:
            self.summ.insert("0", self.text_bd)
        else:
            self.summ.insert("0", "None")
    def get_money(self):
        return self.text_bd

    def __init__(self, window):
        self.helper = Db_helper()
        self.window = window
        self.create()
