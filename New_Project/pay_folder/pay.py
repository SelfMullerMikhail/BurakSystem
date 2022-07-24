import tkinter as tk
from New_Project.pay_folder.window_orders import Window_orders
from New_Project.pay_folder.summ_order import Summ_order
from New_Project.pay_folder.total_money import Total_money
from New_Project.pay_folder.change_order import Change_order

class Pay_botton():
    def pay_window(self):
        self.window = Pay_window()
    def __init__(self):
        self.pay = tk.Button(text="Pay", width=15, height=3, command=self.pay_window)
        self.pay.place(x=250, y=400)




# #######################################################################################
class Pay_window():
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("700x500")
        self.window_orders = Window_orders(self.window)
        self.summ_order = Summ_order(self.window)
        self.total_money = Total_money(self.window)
        self.change_order = Change_order(self.window, self.total_money, self.summ_order )

        self.window.mainloop()

if __name__ == "__main__":
    window = Pay_window()
