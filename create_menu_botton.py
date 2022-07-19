from db_helper import db_helper
from DB import *


class create_menu_botton(tk.Button):
    helper = db_helper()
    def doit(self):
        print('Успех')
    def create(self):
        self.counter = 1
        self.line = self.helper.execute_query("SELECT max(id) FROM menu")
        self.line = (self.line[0] // 3) + 1
        self.y = 20
        for b in range(self.line):
            self.x = 450
            self.y += 60
            for i in range(3):
                self.name = got_name(self.counter)
                if self.name == "None":
                    break
                self.x += 130
                self.i = tk.Button(self, text=self.name, command = self.doit, width=15, height=3)
                self.i.place(y = self.y, x=self.x)
                self.counter += 1
main = create_menu_botton()
main.create()