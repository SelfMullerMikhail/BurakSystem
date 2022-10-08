import tkinter as tk
from tkinter import ttk
from main_window.menegment.orders_history.orders_history import Check_money_window


class Today_story():
    def open_window(self):
        self.window = Check_money_window(self.main_window, self.type_of_history)

    def create_botton(self):
        self.today_history_botton = ttk.Button(self.upPanel_frame, text="Today Story", command=self.open_window, style="myButton.TButton")
        self.today_history_botton.place(x=140, y = 2)

    def __init__(self, window, upPanel_frame, type_of_history):
        self.type_of_history = type_of_history
        self.upPanel_frame = upPanel_frame
        self.main_window = window
        self.create_botton()