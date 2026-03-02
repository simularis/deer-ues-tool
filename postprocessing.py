'''
Description: This script will run the SQL files and perform calculations used in the DEER-EnergyPlus Models post-processing steps,
             effectively expediting the SQL and energy savings workbook steps.
Author: Kelsey Yen, Solaris Technical LLC
Date: 10-01-2025
'''
'''
Revision Log:
10-21-2025 - converted simdata from wide to long table
11-05-2025 - added calculated columns to simdata input file for SQL queries
11-11-2025 - added weighted Com SQL queries
11-13-2025 - created Res SQLs
11-20-2025 - updated Res SQLs and applied changes to Com SQLs
01-14-2026 - updated script with terminal user inputs for future UI development
02-19-2026 - removed excess simdata files from being written and simplified normunits function
02-25-2026 - added lookup table files and functions
'''

import pandas as pd
import sqlite3

def postprocessing(Measure_name, Measure_type, Sector, Norm_unit, Simdata_file, MeasDef_file):
    # Unit Conversions
    J_to_kW = 1/3600000
    m2_to_sqft = 10.7639 # used in SQL files
    W_to_tons = 0.0002843451 # used in SQL files
    kWh_to_therms = 0.0341295763495688

    # Edit simdata for measure specific calcs
    df = pd.read_csv(Simdata_file)

    df['Demand kW'] = df['Electricity:Facility [J](Hourly)'] * J_to_kW

    df['HVAC kWh'] = df['Electricity/Heating'] + df['Electricity/Cooling'] + df['Electricity/Fans']
    df['HVAC therm'] = (df['Natural Gas/Heating'] + df['Natural Gas/Cooling'] + df['Natural Gas/Fans']) * kWh_to_therms

    # Assign user selected norm unit name
    df['MeasureName'] = Measure_name
    df['NormUnit'] = Norm_unit
    df['MeasureType'] = Measure_type

    # Convert revised simdata to long format
    df_long = pd.melt(df, id_vars = ["MeasureName", "MeasureType", "BldgLoc", "BldgType", "Story", "BldgHVAC" ,
                                        "BldgVint", "TechGroup", "TechType", "TechID","NormUnit"], var_name = "Value Name", value_name = "Value")

    print("simdata processed")

    # Connect to the database (or create it if it doesn't exist) 
    connection = sqlite3.connect('postprocessing.db')

    # Create a cursor object 
    cursor = connection.cursor()

    # Read in lookup tables and simdata to database
    df_long.to_sql('simdata', connection, if_exists="replace", index=False)

    df_measdef = pd.read_csv(MeasDef_file)
    df_measdef.to_sql('MeasDef', connection, if_exists="replace",index=False)

    df_numstor = pd.read_csv('LookupTables/NumStor.csv')
    df_numstor.to_sql('NumStor', connection, if_exists="replace",index=False)

    df_normunits = pd.read_csv('LookupTables/NormUnits.csv')
    df_normunits.to_sql('NormUnits', connection, if_exists="replace",index=False)

    # Read the SQL script 
    if Sector == "Residential":
        df_res = pd.read_csv('LookupTables/wts_res_bldg.csv')
        df_res.to_sql('wts_res_bldg', connection, if_exists="replace")

        try:
            # Condition for using Norm unit lookup table
            if Measure_type == "Wall Insulation" or Measure_type == "Ceiling Insulation" or Measure_type == "Refrigerator/Freezer" or Measure_type == "PTAC/PTHP" or Measure_type == "WholeHouseFan":
                with open(f'{Sector}/NormUnitLookup.sql', 'r') as file: 
                    sql_script = file.read()
                cursor.executescript(sql_script)
                print("Norm units lookup script executed successfully.")
            else: 
                with open(f'{Sector}/NormUnit.sql', 'r') as file: 
                    sql_script = file.read()
                cursor.executescript(sql_script)
                print("Norm units script executed successfully.")
                
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
        df_com = pd.read_csv('LookupTables/wts_com_bldg_2026.csv')
        df_com.to_sql('wts_com_bldg_2026', connection, if_exists="replace")

        try:     
            with open(f'{Sector}/Permutations.sql', 'r') as file: 
                sql_script = file.read()
            cursor.executescript(sql_script)
            print("Permutations script executed successfully.")
            # Condition for using Norm unit lookup table
            if Norm_unit == "Area-ft2-BA":
                with open(f'{Sector}/NormUnitLookUp.sql', 'r') as file: 
                    sql_script = file.read()
                cursor.executescript(sql_script)
                print("Norm units lookup script executed successfully.")
            else: 
                with open(f'{Sector}/NormUnit.sql', 'r') as file: 
                    sql_script = file.read()
                cursor.executescript(sql_script)
                print("Norm units script executed successfully.")

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
