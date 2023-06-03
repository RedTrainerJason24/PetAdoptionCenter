###NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

import bcrypt
import sqlite3
import time
import django_project.tables as tb
import django_project.test as test
from datetime import datetime
#maybe use hash lib


def register(email, user, password): # adds user and other info when new usere regisrer
  if check_email(email) == False:
    return False
  elif check_user(user) == False:
    return False #stops from registering
  
  
  # add code to call the add user function
  return True
  
def login(user, password):# logins if user exist and if login  is correct
  current_users = get_blank("username")
  
  if user not in current_users:
    return False # stop if user not in system
  
  index = current_users.index(user)
  curent_passwords = get_blank("password")
  index_password = curent_passwords[index]
 
  pwd_bytes = password.encode("utf-8")
  if pwd_bytes != index_password:
    return False
  else:
    return True
    #add somthing to authorize login
  
  
  
  #return bcrypt.checkpw(pwd_bytes, self.data[user])
  
def hash_password(password):#encrypts password
  pwd_bytes = password.encode("utf-8")
  salt = bcrypt.gensalt()
  return bcrypt.hashpw(pwd_bytes, salt)

def check_email(email):
  email_list = get_blank("email")
  if email in email_list:
    return True
  else:
    return False

def check_user(user):
  user_list = get_blank("username")
  if user in user_list:
    return True
  else:
    return False
      

def get_blank(input):# grabs the list of users
    try:
      dbfile = '/home/runner/The-Adoption-Center/test.db'
        # Create a SQL connection to our SQLite database
      con = sqlite3.connect(dbfile)
      
        # creating cursor
      cur = con.cursor()
      
        # Inserts an account into the user database
        #cur.execute("INSERT INTO auth_user(id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) VALUES (2, 'hoe123', NULL, true, '123', 'hen', 'hem', true, true, 12-21-16, 'ok')")
      blank = [a for a in cur.execute("SELECT "+ input +" FROM auth_user")]
      con.close()
      return blank
    except: 
      print("get blank failed:" + input)

def set_blank(input, value):
  
    dbfile = '/home/runner/The-Adoption-Center/test.db'
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect(dbfile)
    
    # creating cursor
    cur = con.cursor()
    
  # match input:
  #   case "password":
  #     sql_command = ""
  #   case "users":
  #     sql_command = ""
  #

def new_id():
  #sets new user id based on the number of user already in database
  try:
    user_list = get_blank("user")
    i = 0
    if len(user_list) == 0:
      return 0
    for x in user_list:
      i = i + 1
    return i
  except:
    return 0


def get_time():
  now = datetime.now()
  dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
  return dt_string


#def add_user(user_data):
  # username = user_data[username]
  # email = user_data[user-email]
  # password = user_data[user-pw]
  #  # creating file path
  # dbfile = '/home/runner/The-Adoption-Center/test.db'
  # # Create a SQL connection to our SQLite database
  # con = sqlite3.connect(dbfile)

  # # Creating cursor
  # cur = con.cursor()

  # # Deletes table
  # #cur.execute("DROP TABLE pet")
  # cur.execute("INSERT INTO auth_user(id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) VALUES ("+id+", "+ password+", "+last_login+", "+ is_superuser +", "+ username +", "+ Last_name+", "+email+", "+ is_staff +", "+is_active+", "+Date_joined+", "+First_name+")")
  
def add_user(email, username, password, id = new_id(), Last_name = "null",First_name = "null", last_login = get_time() ,Date_joined = get_time() ,is_staff = False, is_active = True,  is_superuser = False) : #add all user info in database
  try:
    dbfile = '/home/runner/The-Adoption-Center/test.db'
      # Create a SQL connection to our SQLite database
    con = sqlite3.connect(dbfile)
  
    # creating cursor
    cur = con.cursor()
  
    # Inserts an account into the user database
    cur.execute("INSERT INTO auth_user(id, password, last_login, is_superuser, username, last_name, email, is_staff, is_active, date_joined, first_name) VALUES ("+id+", "+ password+", "+last_login+", "+ is_superuser +", "+ username +", "+ Last_name+", "+email+", "+ is_staff +", "+is_active+", "+Date_joined+", "+First_name+")")
    con.close()
  except:
    print("add_user failed")

