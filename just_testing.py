import tkinter as tk
from DB import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.Table_1 = tk.Button(self, text="Table_1",
                             command=self.Table_1, width = 15, height = 3)
        self.Table_1.place(x = 10, y = 25)
        self.Table_1 = tk.Button(self, text="Table_2",
                                 command=self.Table_2, width = 15, height = 3)
        self.Table_1.place(x = 140, y = 25)
        self.Table_1 = tk.Button(self, text="Table_3",
                                 command=self.Table_3, width = 15, height = 3)
        self.Table_1.place(x = 270, y = 25)
    def Table_1(self):
        table_1_func()
        self.upgrade()

    def Table_2(self):
        table_2_func()
        self.upgrade()

    def Table_3(self):
        table_3_func()
        self.upgrade()

    def show_summ(self):
        window_summ.delete(1, tk.END)
        self.sums = tables_summ()
        window_summ.insert(1, self.sums)

    def upgrade(self):
        window_enter.delete('1.0', tk.END)
        self.bg = parsing_bd()
        self.show_summ()
        window_enter.insert('1.0', self.bg)

class menu_botton(tk.Button):
    def __init__(self):
        super().__init__()
        conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
        cursor = conn.cursor()
        cursor.execute(f'INSERT orders (id_sell_table, id_menu, counts) VALUES (1, 1, 1)')
        # self.upgrade()
        conn.commit()
        conn.close()
    # def upgrade(self):
    #     window_enter.delete('1.0', tk.END)
    #     self.bg = parsing_bd()
    #     self.show_summ()
    #     window_enter.insert('1.0', self.bg)
#
# got_hight_menu = got_count_menu()
# line = (got_hight_menu[0]//3) + 1
# counter = 1
# y=30
# for i in range(line):
#     x = 550
#     y += 60
#     for i in range(3):
#         i = menu_botton()
#         i.place(y = y, x = x)
#         counter += 1


        # menu = cursor.fetchone()
        # counter += 1
        # menu = str(menu)
        # if menu == "None":
        #     conn.close()
        #     break
        # i.place(x=x, y=y)
        # x += 130
        # conn.close()
        # def drink_add():
        #     conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
        #     cursor = conn.cursor()
        #     cursor.execute(f'INSERT orders (id_sell_table, id_menu, counts) VALUES (1, 3, 1)')
        #     conn.commit()
        #     conn.close()
        # def menu():
        #     upgrade()
        #     drink_add()
        # functions.append(menu)







if __name__ == "__main__":
    window = Window()
    window.columnconfigure(1, minsize=1000)
    window.rowconfigure([0, 1], minsize=350)
    window.title("Мое приложение Tkinter")
    label = tk.Label(text="BurakSystem")
    label.grid(row=0, column=1, sticky="n")
    window_enter = tk.Text(width=45)
    window_enter.place(x=20, y=90)
    window_summ = tk.Entry()
    window_summ.place(x=260, y=480)
    window.mainloop()

