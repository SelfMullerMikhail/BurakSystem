from DB import DB
import tkinter as tk

class upgrade():
    database = DB()
    def upgrade_text(self, window_enter):
        try:
            window_enter.delete('1.0', tk.END)
            self.bg = self.database.parsing_bd()
            window_enter.insert('1.0', self.bg)
        except:
            print("Error def upgrade_text")

    def upgrade_summ(self, window_summ):
        try:
            window_summ.delete(1, tk.END)
            self.sums = self.database.tables_summ()
            window_summ.insert(1, self.sums)
        except:
            print("Error def upgrade_summ")
    def upgrade_all(self, window_enter, window_summ):
        try:
            self.upgrade_text(window_enter)
            self.upgrade_summ(window_summ)
        except:
            print("Error def upgrade_all")

    def clear(self, window_enter, window_summ):
        try:
            self.database.clear_bd()
            self.upgrade_all(window_enter, window_summ)
        except:
            print("Error def clear")

