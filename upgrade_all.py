import tkinter as tk
from DB import *


class upgrade():
    def upgrade_text(self, window_enter):
        window_enter.delete('1.0', tk.END)
        self.bg = parsing_bd()
        window_enter.insert('1.0', self.bg)

    def upgrade_summ(self, window_summ):
        window_summ.delete(1, tk.END)
        self.sums = tables_summ()
        window_summ.insert(1, self.sums)

    def upgrade_all(self, window_enter, window_summ):
        # if self.window_enter is not None:
        self.upgrade_text(window_enter)
        self.upgrade_summ(window_summ)

    def clear(self, window_enter, window_summ):
        clear_bd()
        self.upgrade_all(window_enter, window_summ)