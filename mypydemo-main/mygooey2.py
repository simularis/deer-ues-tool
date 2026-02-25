from myscript import *
from gooey import Gooey, GooeyParser

@Gooey(
    terminal_font_family='Consolas',
    progress_regex=r'Overall progress: (\d+)/(\d+)$',
    progress_expr='x[0] / x[1] * 100',
    hide_progress_msg=True,
    timing_options={
        'show_time_remaining':True,
        'hide_time_remaining_on_complete':False
    }
)
def main_gooey2(inargs: list = None, use_tqdm=False):
    parser = GooeyParser(
        description="Multipurpose tool with FileChooser.",
        epilog=None
    )

    subparsers = parser.add_subparsers(
        title='subcommands',
        description='valid subcommands',
        dest='subparser_name')

    # Create the parser for hello world.
    parser_a = subparsers.add_parser(
        name='say_hello',
        help='Says hello to you.'
    )
    parser_a.add_argument('name', type=str, help='Enter your name')
    parser_a.set_defaults(func=say_hello)

    # Create the parser for adding numbers.
    parser_b = subparsers.add_parser(
        name='add_numbers',
        help='Add two numbers.'
    )
    parser_b.add_argument('numbers', type=float, nargs=2,
                          help='The numbers you want to add, separated by a space. E.g. 1 2.')
    parser_b.set_defaults(func=add_two_numbers)

    # Create the parser for progress bar.
    parser_c = subparsers.add_parser(
        name='bake',
        help='Does something slowly with progress updates.'
    )
    # Gooey Slider widget limitations (as of version 1.0.8.1):
    # * only allows integer values.
    # * only works with optional arguments.
    parser_c.add_argument('--duration', type=float, default=10, help='How many seconds', widget='Slider', gooey_options={"min": 0, "max": 20})
    parser_c.set_defaults(func=bake_a_cake)

    # Create the parser for read a file.
    parser_d = subparsers.add_parser(
        name='readfile',
        help='Reads a file.'
    )
    parser_d.add_argument('filename', type=Path, help='Which file', widget='FileChooser')
    parser_d.set_defaults(func=read_a_file)

    # Create the parser for read a file.
    parser_e = subparsers.add_parser(
        name='readzip',
        help='Reads a file inside a ZIP archive.'
    )
    parser_e.add_argument('zipfilename', type=Path, help='Which ZIP file?', widget='FileChooser')
    parser_e.add_argument('innerfilename', type=str, help='File path inside ZIP archive, e.g. subfolder/file1.txt')
    parser_e.set_defaults(func=read_file_in_zip)

    args = parser.parse_args(inargs)
    #if args.subparser_name:
    #    args.func(args)
    if args.subparser_name == "say_hello":
        say_hello(args.name)
    elif args.subparser_name == "add_numbers":
        add_two_numbers(*args.numbers)
    elif args.subparser_name == "bake":
        bake_a_cake(use_tqdm=use_tqdm, **args.__dict__)
    elif args.subparser_name == "readfile":
        read_a_file(args.filename, use_tqdm=use_tqdm)
    elif args.subparser_name == "readzip":
        read_file_in_zip(args.zipfilename, args.innerfilename, use_tqdm=use_tqdm)
    else:
        parser.print_usage()

if "__main__" == __name__:
    main_gooey2()
