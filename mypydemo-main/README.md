Demonstration of a python command line script plus user interface wrapper and pyinstaller.

## What and why

This repository demonstrates the use of several python packages that make it
easy to take a Python script and turn it into a user-friendly tool to share
with users that don't have Python installed.

The target audience: You write scripts that you use for yourself and that
others may find useful, if only they didn't have to install python, edit
code, and use a command line. If your script requires user interaction or a
sophisticated user interface, do not use this template.

Here's how this template helps, by demonstrating these useful packages.

* `argparse` - Helps you build a command line interface, so the script can be
flexible without needing user edits.
* `Gooey` - Takes a command line interface written for argparse and translates
it to a user interface with almost no work required. The GUI is not very
interactive, but it is easy to write. With some edits, you also get a
FileChooser and other conveniences.
* `pyinstaller` - Bundles the script into an executable file to share. You do
not need to modify the script to use this package. This project merely
demonstrates how to package multiple scripts for distribution together.

Once you have incorporated Gooey into your script and bundled it with
Pyinstaller, users can now enjoy the script with no python installation, no
editing, and no command line.

The repository also demonstrates two types of progress bars: when invoked
from the command line, the script uses `tqdm`. When invoked with the GUI,
the script uses the progress bar included in Gooey. It is helpful to provide
a progress bar when the script runs for more than a few seconds.

## Building distributable executables

1. Create a Python environment with just the packages in requirements.txt.

```
conda create -n mypydemo --file=requirements.txt
activate mypydemo
```

2. In a command prompt, use the following command to start pyinstaller.

```
pyinstaller mypydemo.spec
```

Pyinstaller creates a folder `dist\mypydemo` where you will find executable files.

## Tips for your project

The first step is to make your script flexible by putting all the code in one or more functions.
Each function should take argument(s) that are the variables you might change each time
you use the script. For example:

* A filename with data to analyze
* A label or category to look for in some data
* A folder to output results
* A URL to fetch and parse

Then, create a `main()` function to get command line inputs and start the function(s).
Refer to the argparse documentation.
If you have a collection of related scripts that perform different tasks,
then create multiple functions, and use the subparser pattern.

Test your script on the command line. Once it is working, apply the `@Gooey` decorator
to instantly convert it to a graphical tool. If input widgets would help (e.g. FileChooser,
DateChooser, Listbox) then modify the `main()` function.
Refer to the Gooey documentation.

After Gooey is enabled, you can still use the command line by passing the
`--ignore-gooey` argument to the script. If this is a problem and you want the original
command line syntax, then just create a new `main_gooey()` in a new script file.

Follow the Pyinstaller instructions to create a `.spec` file and build the executable.
Do not use the `-F` (onefile) option just yet, but start with the `-D` (onedir) option.
Pyinstaller will analyze the script to decide which packages it uses and collect the binary files
needed to use those packages into new folders `build` and `dist`. Review those packages and the file size. You may find that some packages have been collected but are not required.
For example, this Pyinstaller identifies `numpy` as a dependency for this project,
although it is not required. Edit the `.spec` file to exclude those packages by name
and reduce the size of the build.

## Gallery

Here is how the Python command line script works, after the user has installed python, created an environment, and opened a terminal.

<img src="doc/gallery0.png">

Here is how the user interface works (no installation, no terminal).

<img src="doc/gallery1.png">

<img src="doc/gallery2.png">
