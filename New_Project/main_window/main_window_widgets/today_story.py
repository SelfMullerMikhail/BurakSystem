import tkinter as tk
from main_window.menegment.orders_history.orders_history import Check_money_window


class Today_story():
    def open_window(self):
        self.window = Check_money_window(self.main_window, self.type_of_history)

    def create_botton(self):
        self.today_history_botton = tk.Button(self.main_window, text="Today Story", command=self.open_window)
        self.today_history_botton.place(x=140, y = 2)

    def __init__(self, window, type_of_history):
        self.type_of_history = type_of_history
        self.main_window = window
        self.create_botton()