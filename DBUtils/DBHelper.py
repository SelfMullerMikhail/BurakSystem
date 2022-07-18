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

  def __execute_query(self, query, params=None):
    self.__open_connection()
    if not self.__connection:
      return None
    try:
      if params:
        self.__cursor.execute(query, params)
      else:
        self.__cursor.execute(query)
      return self.__cursor.fetchall()
    except Error as e:
      print("Error in executing query:"+str(e.message))
      return None
      
  '''Public methods'''
  def get_all_drinks(self):
    return self.__execute_query("SELECT * FROM drinks")
  
  def get_all_tables(self):
    return self.__execute_query("SELECT * FROM Tables")

