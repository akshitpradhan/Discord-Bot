import psycopg2
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# Connecting to database
try:
    connection = psycopg2.connect(user = "ounkzbnl",
                                  password = os.environ.get("PASSWORD"),
                                  host = os.environ.get("HOST"),
                                  port = "5432",
                                  database = "ounkzbnl")

    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)

#Inserting, unique constraint on database as not to store duplicates.
def insert_search(search_history):
    print(search_history)
    cursor.execute("""INSERT INTO newtable (name) VALUES (%s) ON CONFLICT DO NOTHING""", (str(search_history),))
    connection.commit()
    print("Successfuly inserted")
    print(search_history)
    return 1

def show_history():
    sql_select_query = """select * from newtable"""
    cursor.execute(sql_select_query)
    record = cursor.fetchall()
    return record

# Retreiving search history
def find_history(term):
    search_history = ""
    term= term.replace('=', '==').replace('%', '=%').replace('_', '=_')
    sql= "SELECT * FROM newtable WHERE name LIKE %(like)s ESCAPE '='"
    cursor.execute(sql, dict(like= '%'+term+'%'))
    record = cursor.fetchall()
    for i in range(len(record)):
        print(i)
        print(record[i][0])
        print(type(i))
        search_history += record[i][0] + "\n"
    return search_history