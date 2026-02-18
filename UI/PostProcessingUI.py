from argparse import ArgumentParser
from time import sleep
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile
from gooey import Gooey, GooeyParser
from tqdm import tqdm
import sys
import time

def bold_text(text):
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end

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
    
    #Use Category: dropdown list
    input.add_argument(
        '--UseCategory',
        choices=['HVAC', 'Lighting', 'Service'],
        widget='Dropdown',
        help='Select normalizing unit.'
    )
    
    #Normalizing Unit: dropdown list
    input.add_argument(
        '--NormalizingUnit',
        choices=['Cap-Tons', 'Area-BA-ft2', 'Each'],
        widget='Dropdown',
        help='Select normalizing unit.'
        )

    #check box
    input.add_argument(
        '-f', '--foo',
        metavar='Some Flag',
        action='store_true',
        help='Turn things on and off.'
    )

    #output results to user
    args = parser.parse_args()
    print(f'Measure Name: {args.MeasureName} \nSector: {args.Sector} \nUse Category: {args.UseCategory} \nNormalizing Unit: {args.NormalizingUnit}')

if __name__ == '__main__':
    main()
