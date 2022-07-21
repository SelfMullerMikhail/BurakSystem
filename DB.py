from db_helper import db_helper

class DB():
    def switch_table_bd(self, number):
        global peremen
        peremen = number

    def return_table(self):
        try:
            return peremen
        except:
            print("Error return_table")

    helper = db_helper()

    def parsing_bd(self):
        self.text = self.helper.execute_query_fetchall(f'SELECT * FROM summ_count WHERE Tables = {peremen}')
        self.text = str(self.text)
        self.result = self.text.replace('), (', '\n').strip('[').strip(']').strip('(').strip(')').strip(",").strip("'")
        return self.result

    def tables_summ(self):
        self.summ = self.helper.execute_query_fetchone(f'SELECT total FROM summ_one_table WHERE tables = {peremen}')
        self.result = str(self.summ).strip("((Decimal('").strip("'),)")
        return f" summ:  {self.result} TL"

    def clear_bd(self):
        self.text = self.helper.execute_query_insert(f'DELETE FROM orders WHERE id_sell_table = {peremen}')

    def got_name(self, id_fuc):
        self.name = self.helper.execute_query_fetchone(f'SELECT name FROM menu WHERE id = {id_fuc}')
        self.result = str(self.name).strip('{"(').strip(',)"}')
        return self.result
