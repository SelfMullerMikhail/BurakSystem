import tkinter as tk
import re
from New_Project.main_window.db_helper import Db_helper
from New_Project.main_window.table import switcher

class Change_order():
    def create(self):
        self.entery = tk.Entry(self.Window)
        self.entery.place(x=300, y=50)
    def transaction_button_(self):
        self.transaction_button = tk.Button(self.Window, text = "Transaction", width=15, height=3, command = self.transaction)
        self.transaction_button.place(x = 430, y = 10)

    def transaction(self):
        self.entery.delete(0, tk.END)
        self.summ_money_get = int(self.Summ.get_money())
        print(self.summ_money_get)
        self.total_money = int(self.Total.get_money())
        if self.total_money >= self.summ_money_get:
            self.deposid()
            self.entery.insert(0, self.total_money - self.summ_money_get)
            self.Text.delete()
            self.Summ.delete()
        else:
            self.entery.insert(0, "More money")

    def deposid(self):
        self.tab = switcher.got_tab()
        self.helper.execute_query_insert(f"INSERT INTO deposid SELECT tables, total, times  FROM summ_one_table WHERE summ_one_table.tables = {self.tab}")
        self.helper.execute_query_insert(f"DELETE FROM orders WHERE id_sell_table = {self.tab}")
        self.main_text.delete()
        self.main_summ.delete()

    def __init__(self, window, total, summ, text, main_text, main_sum):
        self.main_text = main_text
        self.main_summ = main_sum
        self.helper = Db_helper()
        self.Summ = summ
        self.Total = total
        self.Window = window
        self.Text = text
        self.transaction_button_()
        self.create()
