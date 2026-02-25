from argparse import ArgumentParser
from time import sleep
from pathlib import Path
from hashlib import sha256
from zipfile import ZipFile

from tqdm import tqdm

def say_hello(name: str):
    print("Hello, world.")
    print(f"Hello, {name}.")

def add_two_numbers(number1, number2):
    sum = number1 + number2
    print(f"{number1} + {number2} = {sum}")

def bake_a_cake(duration: float, use_tqdm=True, **kwargs):
    print(f"Starting the kitchen timer for {duration} s")
    if use_tqdm:
        # Command line mode
        with tqdm(total=100) as pbar:
            for i in range(100):
                sleep(duration / 100.)
                pbar.update(1)
    else:
        # Text only output mode for Gooey
        from sys import stdout
        for i in range(100):
            sleep(duration / 100.)
            print(f"Overall progress: {i}/100")
            # Gentle hint to Gooey to update progress bar
            stdout.flush()

    print("Done baking.")

def read_a_file(filename: Path, use_tqdm=True):
    mylen = filename.stat().st_size
    print(f"File '{filename}' has {mylen} bytes")
    print("Computing SHA256 hashsum")
    hash=sha256()
    nbytes = 10000
    if use_tqdm:
        with tqdm(total=mylen) as pbar:
            with filename.open('rb') as f:
                mybytes = f.read(nbytes)
                while len(mybytes) > 0:
                    pbar.update(len(mybytes))
                    hash.update(mybytes)
                    mybytes = f.read(nbytes)
    else:
        # Text only output mode for Gooey
        from sys import stdout
        progress=0
        with filename.open('rb') as f:
            mybytes = f.read(nbytes)
            while len(mybytes) > 0:
                progress += len(mybytes)
                hash.update(mybytes)
                print(f"Overall progress: {progress}/{mylen}")
                # Gentle hint to Gooey to update progress bar
                stdout.flush()
                mybytes = f.read(nbytes)
    print(hash.hexdigest(),f"*{filename}")

def read_file_in_zip(zipfilename: Path, innerfilename: str, use_tqdm=True):
    with ZipFile(zipfilename) as zf:
        zi = zf.getinfo(innerfilename)
        mylen = zi.file_size
        print(f"File '{innerfilename}' has {mylen} bytes")
        print("Computing SHA256 hashsum")
        hash=sha256()
        nbytes = 10000
        if use_tqdm:
            with tqdm(total=mylen) as pbar:
                with zf.open(innerfilename) as f:
                    mybytes = f.read(nbytes)
                    while len(mybytes) > 0:
                        pbar.update(len(mybytes))
                        hash.update(mybytes)
                        mybytes = f.read(nbytes)
        else:
            # Text only output mode for Gooey
            from sys import stdout
            progress=0
            with zf.open(innerfilename) as f:
                mybytes = f.read(nbytes)
                while len(mybytes) > 0:
                    progress += len(mybytes)
                    hash.update(mybytes)
                    print(f"Overall progress: {progress}/{mylen}")
                    # Gentle hint to Gooey to update progress bar
                    stdout.flush()
                    mybytes = f.read(nbytes)
        print(hash.hexdigest(),f"*{innerfilename}")

def main(inargs: list = None, use_tqdm=True):
    parser = ArgumentParser(
        description="Multipurpose tool says hello, adds numbers, bakes cake.",
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
    parser_c.add_argument('duration', type=float, default=10, help='How many seconds')
    parser_c.set_defaults(func=bake_a_cake)

    # Create the parser for read a file.
    parser_d = subparsers.add_parser(
        name='readfile',
        help='Reads a file.'
    )
    parser_d.add_argument('filename', type=Path, help='Which file')
    parser_d.set_defaults(func=read_a_file)

    # Create the parser for read a file.
    parser_e = subparsers.add_parser(
        name='readzip',
        help='Reads a file inside a ZIP archive.'
    )
    parser_e.add_argument('zipfilename', type=Path, help='Which ZIP file?')
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
    main()
