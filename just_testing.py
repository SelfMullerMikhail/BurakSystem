import tkinter.ttk as ttk
import tkinter as tk
from DB import *

def execute_query(query):
    try:
        conn = mysql.connector.connect(host='localhost', user='root', passwd='zuma057195Z!', db='posterposs')
        cursor = conn.cursor()
        result=cursor.execute(query)
        conn.commit()
        conn.close()
        return  result
    except:
        return  None

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.Table_1 = tk.Button(self, text="Table_1", command=self.Table_1, width = 15, height = 3)
        self.Table_1.place(x = 10, y = 25)

        self.Table_2 = tk.Button(self, text="Table_2", command=self.Table_2, width = 15, height = 3)
        self.Table_2.place(x = 140, y = 25)

        self.Table_3 = tk.Button(self, text="Table_3", command=self.Table_3, width = 15, height = 3)
        self.Table_3.place(x = 270, y = 25)

        self.Table_Clear = tk.Button(self, text = "Clear", command = self.clear, width = 15, height =3)
        self.Table_Clear.place(x = 390, y = 420)

        self.label = tk.Label(self, text="BurakSystem")
        self.label.place(x=450, y=1)
        self.window_enter = tk.Text(self, width=45)
        self.window_enter.place(x=20, y=90)

        self.window_summ = tk.Entry(self)
        self.window_summ.place(x=260, y=480)

        got_hight_menu = got_count_menu()
        line = (got_hight_menu[0] // 3) + 1
        counter = 0
        y = 30
        for b in range(line):
            x = 450
            y += 60
            print(b)
            for i in range(3):
                counter += 1
                got_name_str = got_name(counter)
                if got_name_str == "None":
                    break
                x += 130
                print(i)
                i = tk.Button(self, text = got_name_str, command = self.doit, width = 15, height =3).place(y = y, x = x)
                # menu_botton(self, y, x, got_name_str)
    def doit(self):
        print('Успех')
        execute_query(f'INSERT orders (id_sell_table, id_menu, counts) VALUES (1, 1, 1)')
        self.upgrade()


    def Table_1(self):
        table_1_func()
        self.upgrade()

    def Table_2(self):
        table_2_func()
        self.upgrade()

    def Table_3(self):
        table_3_func()
        self.upgrade()

    def clear(self):
        clear()
        self.upgrade()

    def show_summ(self):
        self.window_summ.delete(1, tk.END)
        self.sums = tables_summ()
        self.window_summ.insert(1, self.sums)

    def upgrade(self):
        if self.window_enter is not None:
            self.window_enter.delete('1.0', tk.END)
            self.bg = parsing_bd()
            self.show_summ()
            self.window_enter.insert('1.0', self.bg)

class menu_botton(tk.Button):
    def doit(self):
        print('Успех')
        result=execute_query(f'INSERT orders (id_sell_table, id_menu, counts) VALUES (1, 1, 1)')
        if result is not None:
            self.upgrade()
    def upgrade(self):
        if window_enter is not None:
            window_enter.delete('1.0', tk.END)
            self.bg = parsing_bd()
            # self.show_summ()
            window_enter.insert('1.0', self.bg)
    def __init__(self, name, y, x, name_menu):
        super().__init__()
        self.button = tk.Button(name, text = {name_menu}, command = self.doit, width = 15, height =3).place(y = y, x = x)



if __name__ == "__main__":
    window = Window()

    window.geometry("1000x600")

    window.mainloop()



