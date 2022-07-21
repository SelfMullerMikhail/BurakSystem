from BD import BD
import tkinter as tk

class upgrade():
    database = BD()
    def upgrade_text(self, window_enter):
        window_enter.delete('1.0', tk.END)
        self.bg = self.database.parsing_bd()
        window_enter.insert('1.0', self.bg)

    def upgrade_summ(self, window_summ):
        window_summ.delete(1, tk.END)
        self.sums = self.database.tables_summ()
        window_summ.insert(1, self.sums)

    def upgrade_all(self, window_enter, window_summ):
        # if self.window_enter is not None:
        self.upgrade_text(window_enter)
        self.upgrade_summ(window_summ)


    def clear(self, window_enter, window_summ):
        self.database.clear_bd()
        self.upgrade_all(window_enter, window_summ)



