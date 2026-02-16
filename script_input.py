'''
Scratch script for inputting user values to post-processing script
'''

import pandas as pd

#input = pd.read_csv('postprocessing_input.csv')

print("Enter measure name:")
Measure_name = str(input())
print("Enter measure type:")
Measure_type = str(input())
print("Enter sector:")
Sector = str(input())
print("Enter normalizing unit:")
Norm_unit = str(input())

print("\nPost-Processing Script Inputs:\nMeasure Name:",Measure_name,"\nMeasure Type:",Measure_type, "\nSector:",Sector,"\nNormalizing Unit",Norm_unit)
