import tkinter as tk
from main_window.switcher import Switch_tab
from main_window.db_helper import Db_helper

class Clear_table():
    def clear(self):
        tab = self.tab.got_tab()
        if tab == "all":
            self.helper.execute_query_insert(f"DELETE FROM orders")
        else:
            self.helper.execute_query_insert(f"DELETE FROM orders WHERE id_sell_table = {tab}")
        self.self_Text.delete()
        self.self_Summ.delete()




    def __init__(self, self_text, self_summ):
        self.clear = tk.Button(text="Clear", width=15, height=3, command=self.clear)
        self.clear.place(x=130, y=400)
        self.self_Text = self_text
        self.self_Summ = self_summ
        self.tab = Switch_tab()
        self.helper = Db_helper()
