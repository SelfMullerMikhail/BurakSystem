import tkinter as tk
from Main.db_helper import db_helper
import re
from Main.upgrade_all import upgrade

class Calculater():
    upgrade = upgrade()
    helper = db_helper()
    def transaction(self):
        self.sum_db = self.helper.execute_query_fetchone("SELECT total FROM summ_one_table WHERE tables = 1")
        self.change_money = self.sum.get()
        self.change_money = int(self.change_money)
        self.sum_db = str(self.sum_db)
        self.number = int(re.findall(r"\d+", self.sum_db)[0])
        self.change.insert(1, self.change_money - self.number)

    def new_function(self, wind, summ):
        def button_function():
            self.upgrade.upgrade_all(wind, summ)
        self.i = tk.Button(text="Upgrade", command=button_function, width=15, height=3)
        self.i.grid()
    def change(self):
        self.change = tk.Entry()
        self.change.place(x=370, y=450)

    def button_transaction(self):
        self.button = tk.Button(text="Transaction", command=self.transaction)
        self.button.place(x=500, y=420)

    def sum(self):
        self.sum = tk.Entry()
        self.sum.place(x=370, y=425)

    def __init__(self, window_win, window_sum):
        self.sum()
        self.button_transaction()
        self.change()
        self.new_function(window_win, window_sum)


