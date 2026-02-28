'''
Description: This script will run the SQL files and perform calculations used in the DEER-EnergyPlus Models post-processing steps,
             effectively expediting the SQL and energy savings workbook steps.
Author: Kelsey Yen, Solaris Technical LLC
Date: 1-15-2026

Revision log:
02-16-2026 - Updated UI with more user inputs
02-27-2026 - Revised user inputs to match updated norm unit query requirements
'''

from argparse import ArgumentParser
from time import sleep
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile
from gooey import Gooey, GooeyParser
from tqdm import tqdm
import sys
import time

@Gooey()

def main():
    #header and description under name of script
    parser = GooeyParser(description='Post-processing for DEER-EnergyPlus models.')

    # subheader with input fields
    input = parser.add_argument_group(
        'Enter the following information:',
        gooey_options={'show_border': True, 
                       'columns': 2
                       }
    )

    # Measure Name: text field
    Measure_name = input.add_argument(
        '--MeasureName', 
        widget='TextField',
        help='Enter measure name in SWXX0XX format.'
    )

    # Measure Type: dropdown list
    Measure_type = input.add_argument(
        '--MeasureType',
        choices=['Cooling Capacity', 'PTAC/PTHP', 'Ceiling Insulation', 'Wall Insulation','Refrigerator/Freezer', 'Whole House Fan'],
        widget='Dropdown',
        help='Select measure type/end-use.'
    )

    # Sector: dropdown list
    Sector = input.add_argument(
        '--Sector',
        choices=['Residential', 'Commercial'],
        widget='Dropdown',
        help='Select sector.'
    )
       
    #Normalizing Unit: dropdown list
    Norm_unit = input.add_argument(
        '--NormalizingUnit',
        choices=['Cap-Tons', 'Area-ft2-BA', 'Area-ft2', 'Household', 'kWhreduced'],
        widget='Dropdown',
        help='Select normalizing unit.'
        )

    #Simdata File: File chooser
    Simdata_file = input.add_argument(
        '--SimdataFile',
        widget="FileChooser",
        help="Select simdata file."
    )
    
    #MeasDef File: File chooser
    MeasDef_file = input.add_argument(
        '--MeasDefFile',
        widget="FileChooser",
        help="Select MeasDef file."
    )

    #output submitted information to user
    args = parser.parse_args()
    print(f'Measure Name: {Measure_name}\nMeasure Type: {Measure_type}\nSector: {Sector}\nNormalizing Unit: {Norm_unit}\nSimdata File: {Simdata_file}\nMeasDef File: {MeasDef_file}')

if __name__ == '__main__':
    main()
