import sqlite3
import os
from db_transfer import BASE_DIR

class Db_helper():

    def __init__(self):
        
        self.db_path = os.path.join(BASE_DIR, "PossSqLited.db")
        # self.db_path = ("passsystem\\PossSqLited.db")
        


    def execute_query_fetchone(self, query):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchone()
        self.conn.close()
        return self.result
        

    def execute_query_fetchall(self, query):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.result = self.cursor.fetchall()
        self.conn.close()
        return self.result

    def execute_query_insert(self, query):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query)
        self.conn.commit()
        self.conn.close()