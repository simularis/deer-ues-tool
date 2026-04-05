'''
Description: This script will run a Gooey-based user interface.
Author: Kelsey Yen, Solaris Technical LLC
Date: 1-15-2026
'''
'''
Revision log:
02-16-2026 - Updated UI with more user inputs
02-27-2026 - Revised user inputs to match updated norm unit query requirements
03-02-3036 - Revised UI to run postprocessing.py with user inputs from Gooey
'''

from gooey import Gooey, GooeyParser
from .postprocessing import postprocessing

@Gooey(program_name = 'Post-Processing'   
)

def main():
    #header and description under name of script
    parser = GooeyParser(description='Run post-processing for DEER-EnergyPlus models and generate savings.')

    # subheader with input fields
    input = parser.add_argument_group(
        'Enter the following information:',
        gooey_options={'show_border': True, 
                       'columns': 2
                       }
    )

    # Measure Name: text field
    input.add_argument(
        '--MeasureName', 
        widget='TextField',
        help='Enter measure name in SWXX0XX format'
    )

    # Measure Type: dropdown list
    input.add_argument(
        '--MeasureType',
        choices=['Cooling Capacity', 'PTAC/PTHP', 'Ceiling Insulation', 'Wall Insulation','Refrigerator/Freezer', 'Whole House Fan'],
        widget='Dropdown',
        help='Select measure type/end-use'
    )

    # Sector: dropdown list
    input.add_argument(
        '--Sector',
        choices=['Residential', 'Commercial'],
        widget='Dropdown',
        help='Select sector'
    )
       
    #Normalizing Unit: dropdown list
    input.add_argument(
        '--NormalizingUnit',
        choices=['Cap-Tons', 'Area-ft2-BA', 'Area-ft2', 'Household', 'kWhreduced'],
        widget='Dropdown',
        help='Select normalizing unit'
        )

    #Simdata File: File chooser
    input.add_argument(
        '--SimdataFile',
        widget="FileChooser",
        help="Select simdata file"
    )
    
    #MeasDef File: File chooser
    input.add_argument(
        '--MeasDefFile',
        widget="FileChooser",
        help="Select MeasDef file"
    )

    input.add_argument(
        '--ComResOption',
        widget='CheckBox',
        action='store_true',
        help="Include energy savings for Com/Res building type"
    )

    #output submitted information to user
    args = parser.parse_args()
    print(f'User Inputs\nMeasure Name: {args.MeasureName}\nMeasure Type: {args.MeasureType}\nSector: {args.Sector}\nNormalizing Unit: {args.NormalizingUnit}\nSimdata File: {args.SimdataFile}\nMeasDef File: {args.MeasDefFile}\nCom/Res Option: {args.ComResOption}\n')

    postprocessing(args.MeasureName, args.MeasureType, args.Sector, args.NormalizingUnit, args.SimdataFile, args.MeasDefFile, args.ComResOption)

if __name__ == '__main__':
    main()
