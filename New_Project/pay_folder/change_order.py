import tkinter as tk
import re
from New_Project.db_helper import Db_helper
from New_Project.table import switcher

class Change_order():
    def create(self):
        self.entery = tk.Entry(self.Window)
        self.entery.place(x=300, y=50)
    def transaction_button_(self):
        self.transaction_button = tk.Button(self.Window, text = "Transaction", width=15, height=3, command = self.transaction)
        self.transaction_button.place(x = 430, y = 10)

    def transaction(self):
        self.entery.delete(0, tk.END)
        self.summ_money_get = self.Summ.get_money()
        self.summ_money = int(re.findall(r"\d+", self.summ_money_get)[0])
        self.total_money = int(self.Total.get_money())
        if self.total_money > self.summ_money:
            self.deposid()
            self.entery.insert(0, self.total_money - self.summ_money)
            self.Text.delete()
            self.Summ.delete()
        else:
            self.entery.insert(0, "More money")

    def deposid(self):
        self.tab = switcher.got_tab()
        self.helper.execute_query_insert(f"INSERT INTO deposid SELECT tables, total, times  FROM summ_one_table WHERE summ_one_table.tables = {self.tab}")
        self.helper.execute_query_insert(f"DELETE FROM orders WHERE id_sell_table = {self.tab};")

    def __init__(self, window, total, summ, text):
        self.helper = Db_helper()
        self.Summ = summ
        self.Total = total
        self.Window = window
        self.Text = text
        self.transaction_button_()
        self.create()
