#
# x = -110
# for i in range(3):
#     x += 130
#     name = str("table_" + str(i)
#     table = tk.Button(text=f'{name}', width=15, height=3, command=switch_table_1)
#     table.place(x=x, y=25)


class button_and_command(tk.Button):
    # def __init__(self, numb):
    #     self.number = numb

x = -110
for i in range(3):
    x += 130
    name = str("table_" + str(i))
    button_1 = button_and_command(text=f"{name}", width=15, height=3)
    button_1.place(x=x, y=25)
