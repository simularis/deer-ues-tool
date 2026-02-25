'''
Description: This script will run the SQL files and perform calculations used in the DEER-EnergyPlus Models post-processing steps,
             effectively expediting the SQL and energy savings workbook steps.
Author: Kelsey Yen, Solaris Technical LLC
Date: 10-01-2025

Revision Log:
10-21-2025 - converts simdata from wide to long table
11-05-2025 - adds calculated columns to simdata input file for SQL queries
11-11-2025 - adds weighted Com SQL queries
11-13-2025 - created Res SQLs
11-20-2025 - updated Res SQLs and applied changes to Com SQLs
01-14-2026 - updated script with terminal user inputs for future UI development
02-19-2026 - removed excess simdata files from being written and simplified normunits function
'''

import pandas as pd
import sqlite3

# Reading in user input values (later develop into UI with gooey)
print("Enter measure name (SWXX0XX)")
Measure_name = str(input())
print("Enter sector (Residential, Commercial)")
Sector = str(input())
print("Enter normalizing unit (Cap-Tons, Area-ft-BA, Each)")
Norm_unit = str(input())

print(f"\nPost-Processing Script Inputs:\nMeasure Name: {Measure_name}\nSector: {Sector}\nNormalizing Unit: {Norm_unit}\n")

# Unit Conversions
J_to_kW = 1/3600000
m2_to_sqft = 10.7639
W_to_tons = 0.0002843451
kWh_to_therms = 0.0341295763495688

# Editing simdata for measure specific calcs
df = pd.read_csv(f'simdata_{Measure_name}.csv')

df['Demand kW'] = df['Electricity:Facility [J](Hourly)'] * J_to_kW

df['HVAC kWh'] = df['Electricity/Heating'] + df['Electricity/Cooling'] + df['Electricity/Fans']
df['HVAC therm'] = (df['Natural Gas/Heating'] + df['Natural Gas/Cooling'] + df['Natural Gas/Fans']) * kWh_to_therms

#Norm units must be summed prior to post-processing
df['NormUnit'] = Norm_unit

if Norm_unit == "Cap-Tons":
    df['NumUnits'] = df['Cooling Capacity'] * W_to_tons
elif Norm_unit == "Area-ft-BA":
    df['NumUnits'] = df['Area/Conditioned Total'] * m2_to_sqft

# maybe have normunits be separate measure-specific input table
df_long = pd.melt(df, id_vars = ["File Name","BldgLoc", "BldgType", "Story", "BldgHVAC" ,
                                       "BldgVint", "TechGroup", "TechType", "TechID","NormUnit","NumUnits"], var_name = "Value Name", value_name = "Value")

print("simdata processed")

# Connect to the database (or create it if it doesn't exist) 
connection = sqlite3.connect('postprocessing.db')

# Create a cursor object 
cursor = connection.cursor()

# Read in tables and simdata 
df_long.to_sql('simdata', connection, if_exists="replace")

df_measdef = pd.read_csv(f'MeasDef_{Measure_name}.csv')
df_measdef.to_sql('MeasDef', connection, if_exists="replace")

df_numstor = pd.read_csv('NumStor.csv')
df_numstor.to_sql('NumStor', connection, if_exists="replace")

df_normunits = pd.read_excel('NormUnits.xlsx')
df_normunits.to_sql('NormUnits', connection, if_exists="replace")

# Read the SQL script from a file 
if Sector == "Residential":
    df_res = pd.read_csv(f'{Sector}/wts_res_bldg.csv')
    df_res.to_sql('wts_res_bldg', connection, if_exists="replace")

    try: 
        with open(f'{Sector}/Story_Wts.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("Story_Wts executed successfully.")
        
        with open(f'{Sector}/Permutations.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("Permutations script executed successfully.")

        with open(f'{Sector}/UEC.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("UEC script executed successfully.")

        with open(f'{Sector}/UES.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("UES script executed successfully.")

        with open(f'{Sector}/Bldg_Wts.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("Bldg_Wts script executed successfully.")

        with open(f'{Sector}/Res.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("Res script executed successfully.")

    except sqlite3.Error as e: 
        print(f"An error occurred: {e}")

elif Sector == "Commercial":
    df_com = pd.read_csv(f'{Sector}/wts_com_bldg_2026.csv')
    df_com.to_sql('wts_com_bldg_2026', connection, if_exists="replace")

    try:     
        with open(f'{Sector}/Permutations.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("Permutations script executed successfully.")

        with open(f'{Sector}/UEC.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("UEC script executed successfully.")

        with open(f'{Sector}/UES.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("UES script executed successfully.")

        with open(f'{Sector}/Bldg_Wts.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("Bldg_Wts script executed successfully.")

        with open(f'{Sector}/Com.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("Com script executed successfully.")

    except sqlite3.Error as e: 
        print(f"An error occurred: {e}")

# Output results as csv
df_output = pd.read_sql_query(f"SELECT * FROM {'UES'}", connection)
df_output.to_csv(f'energysavings_{Measure_name}.csv', index=False)
print(f"Savings calcs completed for {Measure_name}.")

# Commit changes and close the connection 
connection.commit()
connection.close()