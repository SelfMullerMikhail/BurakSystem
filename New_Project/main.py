import tkinter as tk
from main_window.text import Text
from main_window.summ import Summ
from main_window.table import Table
from main_window.menegment.menegment import Menegment
from main_window.clear_table import Clear_table
from main_window.pay_folder.pay_window import Pay_botton
from main_window.frame_menu import Frame_menu
from main_window.decorate_folder.decorate import Decorate_main_window 
from main_window.main_window_widgets.today_story import Today_story
from main_window.main_window_widgets.upPanelFrame import UpPanel_Frame, Cats_fone, Tables_Place

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1100x700")
        self.cats_fone = Cats_fone(self)
        self.tables_from = Tables_Place(self)
        self.upPanel_frame = UpPanel_Frame(self)
        self.text = Text(self.tables_from)
        self.summ = Summ(self.tables_from)
        self.frame_menu = Frame_menu(self.text, self.summ, self)
        
        self.menegment = Menegment(self, self.upPanel_frame)
        self.table = Table(self.tables_from, self.text, self.summ)
        self.clear_table = Clear_table(self.tables_from, self.text, self.summ)
        self.pay_botton = Pay_botton(self.text, self.summ, self.tables_from)
        self.decorate = Decorate_main_window(self, "Test Version 1.5")
        self.today_story_botton = Today_story(self, self.upPanel_frame, "today_story")
        
        
        


if __name__ == "__main__":
    app = Window()
    app.mainloop()

