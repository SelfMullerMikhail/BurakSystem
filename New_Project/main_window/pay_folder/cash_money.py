import tkinter as tk

class Cash_money():

    def get_money(self):
        self.money = self.entery.get()
        if self.money == "":
            return 0
        else:
            return self.money

    def create(self):
        self.entery = tk.Entry(self.window)
        self.entery.place(x=300, y=30)

    def delete(self):
        self.entery.delete(0, tk.END)

    def __init__(self, window):
        self.window = window
        self.create()
