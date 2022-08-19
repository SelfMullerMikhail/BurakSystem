import tkinter as tk
from main_window.pay_folder.window_orders import Window_orders
from main_window.pay_folder.summ_order import Summ_order
from main_window.pay_folder.cash_money import Cash_money
from main_window.pay_folder.change_order import Change_order
from main_window.pay_folder.card_money import Card_money
from main_window.table import switcher

from widgets.exit_botton import Exit_botton


class Pay_botton():
    def pay_window(self):
        self.table = switcher.got_tab()
        self.yes_no = self.main_summ.get_money()
        if self.yes_no != None and self.table != "all":
            self.window = Pay_window(self.main_text, self.main_summ, self.main_window)

    def __init__(self, main_text, main_summ, main_window):
        self.main_window = main_window
        self.pay = tk.Button(text="Pay", width=15, height=3, command=self.pay_window)
        self.pay.place(x=250, y=400)
        self.main_text = main_text
        self.main_summ = main_summ



# #######################################################################################
class Pay_window():
    def __init__(self, main_text, main_summ, main_window):
        self.main_window = main_window
        self.main_text = main_text
        self.main_summ = main_summ

        self.window = tk.Frame(master=self.main_window, width=1100, height=700)
        self.window.place(x = 1, y = 1)
        self.window_orders = Window_orders(self.window)
        self.summ_order = Summ_order(self.window)
        self.cash_money = Cash_money(self.window)
        self.card_money = Card_money(self.window)
        self.change_order = Change_order(self.window, self.cash_money, self.card_money, self.summ_order, self.window_orders, self.main_text, self.main_summ)
        self.exit_botton = Exit_botton("Return", self.window)


        self.window.mainloop()