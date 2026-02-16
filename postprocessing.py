'''
Description: This script will run the SQL files and perform calculations used in the DEER-EnergyPlus Models post-processing steps,
             effectively expediting the SQL and energy savings workbook steps.
Author: Kelsey Yen, Solaris Technical LLC
Date: 10-01-2025 
Update: 10-21-2025
    - converts simdata from wide to long table
Update: 11-05-2025
    - adds calculated columns to simdata input file for SQL queries
Update: 11-11-2025
    - adds weighted Com SQL queries
Update: 11-13-2025
    - created Res SQLs
Update: 11-20-2025
    - updated Res SQLs and applied changes to Com SQLs
'''

import pandas as pd
import sqlite3

Measure_name = "SWHC046"
Measure_type = "HVAC"
Sector = "Commercial"
Norm_unit = "Cap-Tons"

# Conversions
J_to_kW = 1/3600000
m2_to_sqft = 10.7639
W_to_tons = 0.0002843451
kWh_to_therms = 0.0341295763495688

# Editing simdata for measure specific calcs
df = pd.read_csv('simdata_SWHC046.csv')

df['Demand kW'] = df['Electricity:Facility [J](Hourly)'] * J_to_kW

if Measure_type == "HVAC":
    df['HVAC kWh'] = df['Electricity/Heating'] + df['Electricity/Cooling'] + df['Electricity/Fans']
    df['HVAC therm'] = (df['Natural Gas/Heating'] + df['Natural Gas/Cooling'] + df['Natural Gas/Fans']) * kWh_to_therms

df['NormUnit'] = Norm_unit

if Norm_unit == "Cap-Tons" and Measure_name == "SWHC012":
    df['NumUnits'] = (df[list(df.filter(regex='Design Size'))].sum(axis=1)) * W_to_tons
elif Norm_unit == "Cap-Tons":
    df['NumUnits'] = df['Cooling Capacity'] * W_to_tons
elif Norm_unit == "Area-ft-BA":
    df['NumUnits'] = df['Area/Conditioned Total'] * m2_to_sqft

# maybe have normunits be separate measure-specific input table

df_edited = df.to_csv("simdata_edited.csv", index=False)

# simdata long table format
df_wide = pd.read_csv("simdata_edited.csv")

df_long = pd.melt (df_wide, id_vars = ["File Name","BldgLoc", "BldgType", "Story", "BldgHVAC" ,
                                       "BldgVint", "TechGroup", "TechType", "TechID","NormUnit","NumUnits"], var_name = "Value Name", value_name = "Value")

df_final = df_long.to_csv("simdata_long.csv", index=False)

print("simdata processed")

# Connect to the database (or create it if it doesn't exist) 
connection = sqlite3.connect('postprocessing.db')

# Create a cursor object 
cursor = connection.cursor()

# Read in tables and simdata 
df = pd.read_csv('simdata_long.csv', low_memory=False)
df.to_sql('simdata', connection, if_exists="replace")

df = pd.read_csv(f'MeasDef_{Measure_name}.csv')
df.to_sql('MeasDef', connection, if_exists="replace")
# remove building type column from MeasDef, assume building types can be permuted for all offering IDs

df = pd.read_csv('NumStor.csv')
df.to_sql('NumStor', connection, if_exists="replace")

# Read the SQL script from a file 
if Sector == "Residential":
    df = pd.read_csv('wts_res_bldg.csv')
    df.to_sql('wts_res_bldg', connection, if_exists="replace")

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

else:
    df = pd.read_csv('wts_com_bldg_2026.csv')
    df.to_sql('wts_com_bldg_2026', connection, if_exists="replace")

    try:     
        with open(f'{Sector}/Permutations.sql', 'r') as file: 
            sql_script = file.read()
        cursor.executescript(sql_script)
        print("Com permutations script executed successfully.")

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
        print("Res script executed successfully.")

    except sqlite3.Error as e: 
        print(f"An error occurred: {e}")

# Output results as csv
df = pd.read_sql_query(f"SELECT * FROM {'UES'}", connection)
df.to_csv(f'energysavings_{Measure_name}.csv', index=False)
print(f"Savings calcs completed for {Measure_name}.")

# Commit changes and close the connection 
connection.commit()
connection.close()