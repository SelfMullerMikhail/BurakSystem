import tkinter as tk
from main_window.db_helper import Db_helper

class Text():
    helper = Db_helper()
    def delete(self):
        self.text.delete("1.0", tk.END)

    def insert(self, tab):
        self.text_bd = self.helper.execute_query_fetchall(f'SELECT id_sell_table, name_menu, cost FROM orders, menu WHERE orders.name_menu = menu.name AND id_sell_table = {tab}')
        for i in self.text_bd:
            self.info = f"- {i[1]}, {i[2]}\n"
            self.text.insert("1.0", self.info)

    def create_text(self):
        self.text = tk.Text(width=45)
        self.text.place(x=130, y=10)

    def __init__(self):
        self.create_text()


