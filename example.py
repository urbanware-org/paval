#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# PaVal - Parameter validation module
# Usage example file
# Copyright (C) 2022 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/paval
# GitLab: https://gitlab.com/urbanware-org/paval
#

import os
import paval as pv


def foobar(input_file, file_list, option, buffer_size, count):
    """
        Sample method showing some usage examples.
    """

    # First of all, check if the paramters have the correct type
    pv.param_type_list([
        [input_file, "input file", str],
        [file_list, "file list", list],
        [option, "option", str],
        [buffer_size, "buffer size", int],
        [count, "count", int]
    ])

    # Ensure that 'input_file' exists
    pv.path(input_file, "input file", True, True)

    # Ensure that 'input_file' is not identical with any from 'file_list'
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


input_file = os.path.realpath(__file__)
foobar(input_file, [["/tmp/foo.txt", "'foo' file"],
                    ["/tmp/bar.txt", "'bar' file"]],
       "print", 4096, 0)

# EOF
