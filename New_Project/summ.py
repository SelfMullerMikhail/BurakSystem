import tkinter as tk
from db_helper import db_helper
import re

class summ():
    helper = db_helper()
    def delete(self):
        self.summ.delete("0", tk.END)

    def insert(self, tab):
        self.text_bd = str(self.helper.execute_query_fetchone(f'SELECT total FROM summ_one_table WHERE tables = {tab}'))
        self.summ.insert("0", int(re.findall(r"\d+", self.text_bd)[0]))


    def __init__(self):
        self.summ = tk.Entry()
        self.summ.place(x=370, y=400)