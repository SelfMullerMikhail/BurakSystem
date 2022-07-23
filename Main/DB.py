from db_helper import db_helper

class DB():
    helper = db_helper()

    def switch_table_bd(self, number):
        global peremen
        peremen = number
    def return_table(self):
        try:
            return peremen
        except:
            print("Error return_table")
    def parsing_bd(self):
        try:
            self.text = self.helper.execute_query_fetchall(f'SELECT * FROM summ_count WHERE Tables = {peremen}')
            self.text = str(self.text)
            self.result = self.text.replace('), (', '\n').strip('[').strip(']').strip('(').strip(')').strip(",").strip("'")
            return self.result
        except:
            print("Eror def parsing_bd")

    def tables_summ(self):
        try:
            self.summ = self.helper.execute_query_fetchone(f'SELECT total FROM summ_one_table WHERE tables = {peremen}')
            self.result = str(self.summ).strip("((Decimal('").strip("'),)")
            return f" summ:  {self.result} TL"
        except:
            print("Error def table_sum")

    def clear_bd(self):
        try:
            self.text = self.helper.execute_query_insert(f'DELETE FROM orders WHERE id_sell_table = {peremen}')
        except:
            print("Error def clear_bd")

    def got_name(self, id_fuc):
        try:
            self.name = self.helper.execute_query_fetchone(f'SELECT name FROM menu WHERE id = {id_fuc}')
            self.result = str(self.name).strip('{"(').strip(',)"}')
            return self.result
        except:
            print("Error def got_name")

