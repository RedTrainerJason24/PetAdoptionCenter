import sqlite3


def create_table():
  sql_create_projects_table = """CREATE TABLE IF NOT EXISTS (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    )""";
  
  
  conn = create_connection("/home/runner/The-Adoption-Center/test.db")
  createtable(conn, sql_create_projects_table)

#Creates a connection to the database file
#############
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except:
        print("")

    return conn
  ################


def createtable(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except:
        print("")
