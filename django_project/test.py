# loading in modules
import sqlite3
import time

def test():
  # creating file path
  dbfile = '/home/runner/The-Adoption-Center/test.db'
  # Create a SQL connection to our SQLite database
  con = sqlite3.connect(dbfile)

  # creating cursor
  cur = con.cursor()

  # Inserts an account into the user database
  cur.execute("INSERT INTO auth_user(id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) VALUES (2, 'hoe123', NULL, true, '123', 'hen', 'hem', true, true, 12-21-16, 'ok')")
  

  # Retrieves data from a table
  table_list = [a for a in cur.execute("SELECT is_staff FROM auth_user")]
  # here is you table list
  print(table_list)

  # Be sure to close the connection
  con.close()