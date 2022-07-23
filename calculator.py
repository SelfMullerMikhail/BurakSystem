import tkinter as tk
from Main.db_helper import db_helper
import re
from Main.upgrade_all import upgrade
from Main.DB import DB

class Calculater():
    upgrade = upgrade()
    helper = db_helper()


    def change(self):
        self.change = tk.Entry()
        self.change.place(x=370, y=450)

    def button_transaction(self, wind, summ, table):
        def transaction():
            tab = self.table.return_table()
            self.sum_db = self.helper.execute_query_fetchone(f"SELECT total FROM summ_one_table WHERE tables = 1")
            self.change_money = self.sum.get()
            if self.change_money != "":
                self.change_money = int(self.change_money)
                self.sum_db = str(self.sum_db)
                self.number = int(re.findall(r"\d+", self.sum_db)[0])
                self.change.delete(0, tk.END)
                self.change.insert(1, self.change_money - self.number)
                self.upgrade.upgrade_all(wind, summ)
            else:
                self.change.delete(0, tk.END)
                self.change.insert(1, "Wright money")
        self.button = tk.Button(text="Transaction", command=transaction)
        self.button.place(x=500, y=420)


    def sum(self):
        self.sum = tk.Entry()
        self.sum.place(x=370, y=425)

    def __init__(self, window_win, window_sum, table):
        self.table = DB()
        self.sum()
        self.change()
        self.button_transaction(window_win, window_sum, table)

        # self.new_function(window_win, window_sum)


