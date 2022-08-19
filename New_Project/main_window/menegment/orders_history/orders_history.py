import tkinter as tk
from main_window.db_helper import Db_helper
from widgets.exit_botton import Exit_botton
from widgets.text_window import Text_window


class Check_money_window():
    def clear_history(self):
        self.password = self.entery.get()
        if self.password == "28051997":
            self.helper.execute_query_insert(f"""DELETE FROM deposid""")
            self.helper.execute_query_insert(f"""DELETE FROM full_history""")
            self.text_window.delete()

    def clear_history_botton_create(self, window):
        self.clear_history_botton = tk.Button(window, text="Clear", command=self.clear_history, width=15, height=3)
        self.clear_history_botton.place(x=10, y=420)
        self.entery = tk.Entry(window)
        self.entery.place(x=10, y=480)
        self.entery.insert(1, "password")
        

    def create_window(self):
        self.window = tk.Frame(self.main_window, width=1100, height=700)
        self.window.place(x = 1, y = 1)

    def __init__(self, main_window):
        self.helper = Db_helper()
        self.main_window = main_window
        self.create_window()
        self.text_window = Text_window(self.window, 10, 20)
        self.clear_history_botton_create(self.window)
        self.exit_botton = Exit_botton("Return", self.window)
        