'''
Author: Kelsey Yen, Solaris Technical LLC
Date: 10-01-2025 
    - based on SWHC012
Update: 10-21-2025
    - converts simdata from wide to long table
Update: 11-05-2025
    - adds alculated columns to simdata input file for SQL queries
Description: This script will run the SQL files and perform calculations used in the DEER-EnergyPlus Models post-processing steps,
             effectively expediting the SQL and energy savings workbook steps.
'''

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

Measure_name = "SWHC012"
Measure_type = "HVAC"
Sector = "Commercial"
Norm_unit = "Cap-Tons"

# Conversions
J_to_kW = 0.000000277778
m2_to_sqft = 10.764
W_to_tons = 0.0002843451

# Editing simdata for measure specific calcs
df = pd.read_csv('simdata.csv')
df['Demand kW'] = df['Electricity:Facility [J](Hourly)'] * J_to_kW

if Measure_type == "HVAC":
    df['HVAC kWh'] = df['Electricity/Heating'] + df['Electricity/Cooling'] + df['Electricity/Fans']

df['NormUnit'] = Norm_unit

if Norm_unit == "Cap-Tons" and Measure_name == "SWHC012":
    df['NumUnits'] = (df[list(df.filter(regex='Design Size'))].sum(axis=1)) * W_to_tons
elif Norm_unit == "Cap-Tons":
    df['NumUnits'] = df['Cooling Capacity'] * W_to_tons
elif Norm_unit == "Area-ft-BA":
    df['NumUnits'] = df['Area/Total']

df_edited = df.to_csv("simdata_edited.csv")

# Connect to the database (or create it if it doesn't exist) 
connection = sqlite3.connect('postprocessing.db') 
 
df = pd.read_csv('simdata_edited.csv')
df.to_sql('simdata', connection, if_exists="replace")

df = pd.read_csv('MeasDef.csv')
df.to_sql('MeasDef', connection, if_exists="replace")
# remove building type column from MeasDef, assume building types can be permuted for all offering IDs

# Create a cursor object 
cursor = connection.cursor() 
 
# Read the SQL script from a file 

try: 
    with open(f'{Sector}/Permutations.sql', 'r') as file: 
        sql_script = file.read()
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.")
    with open(f'{Sector}/UEC.sql', 'r') as file: 
        sql_script = file.read()
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.")
    with open(f'{Sector}/UES.sql', 'r') as file: 
        sql_script = file.read() 
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.")
    with open(f'{Sector}/Bldg_Wts.sql', 'r') as file: 
        sql_script = file.read() 
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.")
    with open(f'{Sector}/Com_Wt.sql', 'r') as file: 
        sql_script = file.read() 
    cursor.executescript(sql_script) 
    print("SQL script executed successfully.")

except sqlite3.Error as e: 
    print(f"An error occurred: {e}")  

# Output results as csv
df = pd.read_sql_query(f"SELECT * FROM {'UES'}", connection)
df.to_csv('energysavings.csv')
print('Results generated.')

# Commit changes and close the connection 
connection.commit() 
connection.close()