# *PaVal*

**Table of contents**
*   [Definition](#definition)
*   [Details](#details)
*   [Requirements](#requirements)
*   [Documentation](#documentation)
*   [Useless facts](#useless-facts)

----

## Definition

The *PaVal* module is an easy-to-use parameter validator for methods inside *Python* scripts.

[Top](#)

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

[Top](#)

## Requirements

In order to use *PaVal*, the *Python* framework must be installed on the system.

Depending on which version of the framework you are using:

*   *Python* 2.x (version 2.7 or higher is recommended, may also work with earlier versions)
*   *Python* 3.x (version 3.2 or higher is recommended, may also work with earlier versions)

[Top](#)

## Documentation

There is a plain text file inside the corresponding directories with further information and usage examples.

[Top](#)

## Useless facts

*   The project name is an abbreviation for ***Pa****rameter* ***Val****idator*.
*   The first version uploaded on *GitHub* was *PaVal* 1.2.5 built on February 11<sup>th</sup>, 2016.
*   The module for *Python* 3 was created by converting the *Python* 2 module using the *2to3* tool. However, both files are identical except for the shebang.

[Top](#)
