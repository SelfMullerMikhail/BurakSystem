import tkinter as tk
from db_helper import Db_helper
import re

class Summ():
    helper = Db_helper()
    def delete(self):
        self.summ.delete("0", tk.END)

    def insert(self, tab):
        self.text_bd = str(self.helper.execute_query_fetchone(f'SELECT total FROM summ_one_table WHERE tables = {tab}'))
        if self.text_bd != "None":
            self.summ.insert("0", int(re.findall(r"\d+", self.text_bd)[0]))
        else:
            self.summ.insert("0", "None")
        print(f"Summ is work! Tab: {tab}")


    def summ_create(self):
        self.summ = tk.Entry()
        self.summ.place(x=370, y=400)



    def __init__(self):
        self.summ_create()