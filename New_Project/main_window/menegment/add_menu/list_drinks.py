import tkinter as tk
from New_Project.main_window.menegment.add_menu.text_add_drinks import Text_add_drinks

class List_drinks():

    # def create_list(self):

    def __init__(self, history_window):
        self.history_window = history_window
        # self.create_list()
        self.text = Text_add_drinks(self.history_window)




    # def create_list(self):
    #     self.list_label = tk.Menubutton(self.history_window, text="Drinks")
    #     self.list = tk.Menu(self.list_label)
    #     for i in range(1000):
    #         print(i)
    #         def testing():
    #             print(i)
    #         self.list.add_command(label=f"add_ingridient{i}", command=testing)
    #     self.list_label["menu"] = self.list
    #     self.list_label.place(x=500, y=20)
    #
    #
    # def __init__(self, history_window):
    #     self.history_window = history_window
    #     self.create_list()
