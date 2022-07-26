import tkinter as tk

class Entery_data():
    def create_entery(self):
        self.entery = tk.Entry(self.history_window)
        self.entery.place(x = 500, y =300)

    def test(self):
        print('--test--')

    def create_list(self):
        # self.list_label = tk.Menubutton(self.history_window, text = "Times")
        # self.list = tk.Menu(self.list_label)
        # for i in range(10):
        #     self.list.add_command(label="add_ingridient", command=self.test)
        #     self.list_label["menu"] = self.list
        #     self.list_label.grid()
        self.menu_label = tk.Menubutton(self.history_window, text="Menu")
        self.menu = tk.Menu(self.menu_label)
        self.menu.add_command(label="add_ingridient", command=self.test)
        self.menu_label["menu"] = self.menu
        self.menu_label.place(x = 600, y = 400)

    def __init__(self, history_window):
        self.history_window = history_window
        self.create_list()
        self.create_entery()




    # self.menu_label = tk.Menubutton(text="Menu")
    #         self.menu = tk.Menu(self.menu_label)
    #         self.menu.add_command(label="add_ingridient", command=self.add_ingridient)
    #         self.menu.add_command(label="add_menu", command=self.add_menu)
    #         self.menu.add_command(label="add_shipment", command=self.add_shipment)
    #         self.menu.add_command(label="History", command=self.history)
    #         self.menu_label["menu"] = self.menu
    #         self.menu_label.grid()