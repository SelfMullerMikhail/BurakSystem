import tkinter as tk
from New_Project.main_window.db_helper import Db_helper
import re

class Summ():
    helper = Db_helper()
    def delete(self):
        self.summ.delete("0", tk.END)

    def insert(self, tab):
        if tab:
            self.summ_bd = self.helper.execute_query_fetchone(f'SELECT sum(cost) FROM show_orders WHERE tables = {tab}')[0]
            print(self.summ_bd, "summ_bd")
            if self.summ_bd != None:
                self.summ.insert("0", self.summ_bd)
            else:
                self.summ.insert("0", "None")
            print(f"Summ is work! Tab: {tab}")
        else:
            print("Error Summ.insert. (self.summ_bd")

    def get_money(self):
        try:
            return self.summ_bd
        except:
            print("Error Summ.get_money. self.summ_bd")

    def summ_create(self):
        self.summ = tk.Entry()
        self.summ.place(x=370, y=400)



    def __init__(self):
        self.summ_create()