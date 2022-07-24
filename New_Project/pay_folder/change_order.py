import tkinter as tk
import re

class Change_order():
    def create(self):
        self.entery = tk.Entry(self.Window)
        self.entery.place(x=300, y=50)
    def transaction_button_(self):
        self.transaction_button = tk.Button(self.Window, text = "Transaction", width=15, height=3, command = self.transaction)
        self.transaction_button.place(x = 430, y = 10)

    def transaction(self):
        self.summ_money_get = self.Summ.get_money()
        self.summ_money = int(re.findall(r"\d+", self.summ_money_get)[0])
        self.total_money = int(self.Total.get_money())
        self.entery.insert(1, self.total_money - self.summ_money)

    def __init__(self, window, total, summ):
        self.Summ = summ
        self.Total = total
        self.Window = window
        self.transaction_button_()
        self.create()
