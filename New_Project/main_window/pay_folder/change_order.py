import tkinter as tk
from main_window.db_helper import Db_helper
from main_window.table import switcher

class Change_order():
    def create(self):
        self.entery = tk.Entry(self.Window)
        self.entery.place(x=300, y=50)

    def transaction_button_(self):
        self.transaction_button = tk.Button(self.Window, text = "Transaction", width=15, height=3, command = self.transaction)
        self.transaction_button.place(x = 560, y = 10)

    def transaction(self):
        self.entery.delete(0, tk.END)
        self.summ_money_get = int(self.Summ.get_money())
        self.cash_money = int(self.Cash.get_money())
        self.card_money = int(self.Card.get_money())
        self.total_money = self.cash_money + self.card_money
        if self.total_money >= self.summ_money_get:
            self.change_money = self.cash_money - (self.summ_money_get - self.card_money)
            self.deposid()
            if self.change_money >= 0:
                self.entery.insert(0, self.change_money)
            else:
                self.entery.insert(0, 0)
            self.Text.delete()
            self.Summ.delete()
        else:
            self.entery.insert(0, "More money")

    def deposid(self):
        self.tab = switcher.got_tab()
        self.helper.execute_query_insert(f"INSERT INTO count_money (tables, cash_money, card_money)VALUES ({self.tab}, {self.summ_money_get}, {self.card_money})")
        
        self.helper.execute_query_insert(f"""INSERT INTO deposid (tables, cash_money, card_money, total, times) 
            SELECT count_money.tables, cash_money, card_money, total, times  
            FROM summ_one_table, count_money 
            WHERE summ_one_table.tables = {self.tab} and count_money.tables = {self.tab}""")
        
        # self.helper.execute_query_insert(f"""INSERT INTO full_history (tables, menu_name, price, datetimes) 
        #     SELECT show_orders.tables AS tables, show_orders.name AS menu_name, cost AS price, deposid.times AS datetimes
        #     FROM deposid, show_orders
        #     WHERE show_orders.tables = {self.tab} AND deposid.tables = {self.tab}""")
        self.helper.execute_query_insert(f"""INSERT INTO full_history (tables, menu_name, price, datetimes) 
            SELECT tables AS tables, name AS menu_name, cost AS price,  CURRENT_TIME AS datetimes
            FROM show_orders
            WHERE show_orders.tables = {self.tab}""")

        self.helper.execute_query_insert(f"DELETE FROM orders WHERE id_sell_table = {self.tab}")
        self.helper.execute_query_insert(f"DELETE FROM count_money WHERE tables = {self.tab}")
        self.main_text.delete()
        self.main_summ.delete()

    def __init__(self, window, cash, card, summ, text, main_text, main_sum):
        self.main_text = main_text
        self.main_summ = main_sum
        self.helper = Db_helper()
        self.Summ = summ
        self.Cash = cash
        self.Card = card
        self.Window = window
        self.Text = text
        self.transaction_button_()
        self.create()
