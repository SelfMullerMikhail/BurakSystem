import sqlite3
from sqlite3 import Error

class DBHelper:
  '''Private members'''
  __connection=None
  __cursor=None

  def __init__(self):
    pass

  def __del__(self):
    self.__close_connection()
    print("DBHelper object deleted")
  
  '''Private methods'''
  def __open_connection(self):
    if not self.__connection:
      self.__connection=sqlite3.connect('./BurakDB.db')
      try:
        if not self.__cursor:
          self.__cursor=self.__connection.cursor()
      except Error as e:
        self.__cursor=None
        print("Error in connecting to database:"+str(e.message))

  def __close_connection(self):
    if self.__connection:
      self.__connection.close()
      self.__connection=None
      self.__cursor=None

  def __execute_query(self, query,isFetch=True, params=None):
    self.__open_connection()
    if not self.__connection:
      return None
    try:
      if params:
        self.__cursor.execute(query, params)
      else:
        self.__cursor.execute(query)
      if isFetch:
        return self.__cursor.fetchall()
      self.__connection.commit()
      return self.__cursor.lastrowid
    except Error as e:
      print("Error in executing query")
      return None
      
  '''Public methods'''
  def get_all_drinks(self):
    return self.__execute_query("SELECT * FROM drinks")
  
  def get_all_tables(self):
    return self.__execute_query("SELECT * FROM Tables")

  def get_all_orders(self,guid):
    return self.__execute_query(f"SELECT * FROM Orders WHERE OrderId='{guid}'")

  def add_order(self,drink,table,guid):
    return self.__execute_query(f"INSERT INTO Orders (Customer,Drink,OrderId) VALUES ({table},{drink},'{guid}')",False)

  def remove_order(self,id):
    return self.__execute_query(f"DELETE FROM Orders Where Id={id}",False)

  def update_quantity(self,id,quantity):
    return self.__execute_query(f"UPDATE Orders SET Quantity={quantity} WHERE Id={id}",False)

