# *PaVal*

**Table of contents**
*   [Definition](#definition)
*   [Details](#details)
*   [Requirements](#requirements)
*   [Documentation](#documentation)
*   [Contact](#contact)
*   [Useless facts](#useless-facts)

----

## Definition

The *PaVal* module is an easy-to-use parameter validator for methods inside *Python* scripts.

[Top](#paval)

## Details

Before, there was some code to validate the given parameters (such as directory and file paths, numbers, ranges and strings) in many of my projects. This worked fine so far, but there was (partially the same) parameter validation code in various components.

So, if that code needed to be changed, it had to be done in various files of the project and (according to the significance of the change) also in other projects, which was sometimes pretty laborious.

Due to this, the common and non-project-specific parameter validation code has been exported from each project and merged in a single project independent module. In some cases it saved more than a hundred lines of code per project.

The module works read-only. This means, its methods validate the given values and raise an exception in case of an error, but they do not change or return anything.

The current version of *PaVal* comes with the following features.

### File system checks

Check a given path...

*   if it exists.
*   if it points to a directory or file.

Compare a file with a list of other files...

*   to check if the same file name is given multiple times.
*   to check if the file is given multiple times with a different name but the same content.

### Number checks

Check an integer value...

*   if it is positive, zero or negative.

Check an integer range...

*   if the given value is inside that range.
*   if the given value is zero.

### String checks

Check a string...

*   if it contains wildcard characters.
*   if it contains invalid characters (user-defined).

Compare a string with a list of other strings...

*   to check if the string is an item of the list.

[Top](#paval)

## Requirements

In order to run the latest version of *Clap*, the *Python* 3.x framework (version 3.2 or higher is recommended) must be installed on the system.

Version 1.2.7 is the last official release that also runs on the *Python* 2.x framework.

If you need a later version for the *Python* 2.x framework for whatever reason, you can try refactoring the syntax from *Python* 3.x to version 2.x using the *[3to2](https://pypi.python.org/pypi/3to2)* tool.

However, there is no guarantee that this works properly or at all.

[Top](#paval)

## Documentation

For fundamental documentation as well as some usage examples you may have a look at the `usage.txt` file.

[Top](#paval)

## Contact

Any suggestions, questions, bugs to report or feedback to give?

You can contact me by sending an email to [dev@urbanware.org](mailto:dev@urbanware.org) or by opening a *GitHub* issue (which I would prefer if you have a *GitHub* account).

[Top](#paval)

## Useless facts

*   The project name is an abbreviation for ***Pa****rameter* ***Val****idator*.
*   The first version uploaded on *GitHub* was *PaVal* 1.2.5 built on February 11<sup>th</sup>, 2016.
*   The module for *Python* 3 was initially created by converting the *Python* 2 module using the *2to3* tool. However, both files are identical except for the shebang.

[Top](#paval)
