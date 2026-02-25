'''
1-15-2026: Created version 1 of UI
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
    parser = GooeyParser(description='Post-processing results for DEER-EnergyPlus models.')

    #subheader with input fields
    input = parser.add_argument_group(
        'Enter the following information:',
        gooey_options={'show_border': True, 
                       'columns': 2
                       }
    )

    #Measure name: text field
    input.add_argument(
        '--MeasureName', 
        widget='TextField',
        help='Enter measure name in SWXX0XX format.'
    )

    #Sector: dropdown list
    input.add_argument(
        '--Sector',
        choices=['Residential', 'Commercial'],
        widget='Dropdown',
        help='Select sector.'
    )
       
    #Normalizing Unit: dropdown list
    input.add_argument(
        '--NormalizingUnit',
        choices=['Cap-Tons', 'Area-BA-ft2', 'Each'],
        widget='Dropdown',
        help='Select normalizing unit.'
        )

    #Simdata File: File chooser
    input.add_argument(
        '--SimdataFile',
        widget="FileChooser",
        help="Select simdata file to post-process."
    )
    
    #MeasDef File: File chooser
    input.add_argument(
        '--MeasDefFile',
        widget="FileChooser",
        help="Select MeasDef file to post-process."
    )

    #output submitted information to user
    args = parser.parse_args()
    print(f'Measure Name: {args.MeasureName}\nSector: {args.Sector}\nNormalizing Unit: {args.NormalizingUnit}\nSimdata File: {args.SimdataFile}\nMeasDef File: {args.MeasDefFile}')

if __name__ == '__main__':
    main()
