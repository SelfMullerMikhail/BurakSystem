import tkinter as tk
import re
from New_Project.table import switcher
from New_Project.db_helper import Db_helper

class Summ_order():

    # def insert(self):

    def create(self):
        self.summ = tk.Entry(self.window)
        self.summ.place(x=300, y=10)
        self.tab = switcher.got_tab()
        self.text_bd = str(self.helper.execute_query_fetchone(f'SELECT total FROM summ_one_table WHERE tables = {self.tab}'))
        if self.text_bd != "None":
            self.summ.insert("0", int(re.findall(r"\d+", self.text_bd)[0]))
        else:
            self.summ.insert("0", "None")

    def __init__(self, window):
        self.helper = Db_helper()
        self.window = window
        self.create()
