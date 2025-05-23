#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import tempfile
import paval as pv


def example_method(input_file, file_list, option, buffer_size=4096, count=0):
    """
        Example method that does not make any sense itself and which is only
        used to demonstrate how the methods of PaVal work.

        It simply expects an existing file that must not be contained in the
        specified file list, an option ("print", "read" or "write"), a buffer
        size between 1 and 4096 as well as a count value that must be zero or
        a positive integer.
    """

    # First of all, check if the parameters have the correct type
    pv.param_type_list([
        [input_file, "input file", str],
        [file_list, "file list", list],
        [option, "option", str],
        [buffer_size, "buffer size", int],
        [count, "count", int]
    ])

    # Ensure that 'input_file' exists
    pv.path(input_file, "input file", True, True)

    # Ensure that 'input_file' is not contained in 'file list'
    pv.compfile(input_file, "input file", file_list)

    # Ensure that the file name of 'input_file' does not contain any wildcards
    # and also that it does not contain brackets or exlamation marks
    pv.string(input_file, "input file", False, ['(', ')', '!'])

    # Ensure 'option' is one of the options from the list
    pv.compstr(option, "option", ["print", "read", "write"])

    # Ensure that 'buffer_size' is a postive integer between 1 and 4096
    pv.intrange(buffer_size, "buffer size", 1, 4096, False)

    # Finally, ensure that 'count' is either zero or a positive integer
    pv.intvalue(count, "count", True, True, False)

    print("Parameter validation successful.")


# Create a temporary file for the PaVal method example
example_input_file, example_input_file_path = tempfile.mkstemp(
    suffix='.txt', text=True)

# Create sample file names based on the temporary file just created
sample_file_list = [[example_input_file_path + ".foo", "'foo' file"],
                    [example_input_file_path + ".bar", "'bar' file"]]

# Call the method with some sample values. Details can be found in the
# docstring of the method above.
example_method(example_input_file_path, sample_file_list, "read", 1024, 4)

os.close(example_input_file)
os.remove(example_input_file_path)
