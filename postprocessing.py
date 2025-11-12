import pandas as pd
import sqlite3
import sqlalchemy

# # IMPORT THE SQALCHEMY LIBRARY's CREATE_ENGINE METHOD
# from sqlalchemy import create_engine

# # DEFINE THE DATABASE CREDENTIALS
# user = 'sptviewer'
# password = 'deereddev'
# host = '127.0.0.1'
# port = 5432
# database = 'exante'

# # PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# # RETURN THE SQLACHEMY ENGINE OBJECT
# def get_connection():
#     return create_engine(
#         url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
#             user, password, host, port, database
#         )
#     )

# if __name__ == '__main__':
#     try:
#         # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
#         engine = get_connection()
#         print(
#             f"Connection to the {host} for user {user} created successfully.")
#     except Exception as ex:
#         print("Connection could not be made due to the following error: \n", ex)


# Connect to the database (or create it if it doesn't exist) 
connection = sqlite3.connect('postprocessing.db') 
 
df = pd.read_csv('simdata.csv')
df.to_sql('simdata', connection, if_exists="replace")

df = pd.read_csv('MeasDef.csv')
df.to_sql('MeasDef', connection, if_exists="replace")

# Create a cursor object 
cursor = connection.cursor() 
 
# Read the SQL script from a file 
with open('SQL Files/Permutations.sql', 'r') as file: 
    sql_script = file.read() 
 
# Execute the SQL scripts 
try: 
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.") 
except sqlite3.Error as e: 
    print(f"An error occurred: {e}") 


with open('SQL Files/UsePerUnitStd.sql', 'r') as file: 
    sql_script = file.read() 
 
try: 
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.") 
except sqlite3.Error as e: 
    print(f"An error occurred: {e}") 

with open('SQL Files/UsePerUnitMeas.sql', 'r') as file: 
    sql_script = file.read() 
 
try: 
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.") 
except sqlite3.Error as e: 
    print(f"An error occurred: {e}") 

with open('SQL Files/UEC.sql', 'r') as file: 
    sql_script = file.read() 
 
try: 
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.") 
except sqlite3.Error as e: 
    print(f"An error occurred: {e}") 

with open('SQL Files/UES.sql', 'r') as file: 
    sql_script = file.read() 
 
try: 
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.") 
except sqlite3.Error as e: 
    print(f"An error occurred: {e}")   

# Output results as csv
df = pd.read_sql_query(f"SELECT * FROM {'UES'}", connection)
df.to_csv('UES.csv')
print('Results generated.')

# Commit changes and close the connection 
connection.commit() 
connection.close()