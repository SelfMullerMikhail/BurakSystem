import tkinter as tk
from New_Project.main_window.db_helper import Db_helper

class Botton_show():
    def show(self):
        self.history_window.delete()
        self.history = self.helper.execute_query_fetchall("SELECT * FROM deposid")
        for row in self.history:
            self.history_window.insert(f"tab: {row[0]} TL: {row[1]} data: {row[2]}\n")

    def __init__(self, window, history_window):
        self.history_window = history_window
        self.helper = Db_helper()
        self.window = window
        self.botton = tk.Button(self.window, text = 'Show', width=15, height=3, command = self.show)
        self.botton.place(x = 800, y = 10)