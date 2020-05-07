# !/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import json
from os.path import isfile

__author__ = "Fearghal Hayes"
__date__ = "03/05/2020"
__credits__ = "Me, and the other participants in the Skills Demo 3 for the Programming Module"
__version__ = "0.0.1"


def append_settings(passed_settings={}, passed_filename="config.json"):  # CALL ME WHEN NEEDED!
    """CALL ME: Only use this function for appending data and saving to the file. This function
    only accepts dictionaries as the \"passed_settings\" parameter."""
    return backend_append_values(passed_settings, passed_filename)


def add_settings_to_start(passed_settings={}, passed_filename="config.json"):  # CALL ME WHEN NEEDED!
    """CALL ME: Only use this function for adding data to the start of the file and saving to the file. This function
    only accepts dictionaries as the \"passed_settings\" parameter. Don't use the below functions, they are backend
    functions."""

    return backend_add_values_to_start(passed_settings, passed_filename)


def load(passed_filename="config.json", debug_level=None):  # CALL ME WHEN NEEDED!
    """"""
    settings = backend_load(passed_filename, debug_level)
    return settings


def show(filename="config.json"):  # CALL ME WHEN NEEDED!
    """"""
    the_data = backend_load(filename)

    if the_data != {}:
        print("You called the show function, the current json data is: ", the_data)

    elif the_data == {}:
        print("You called the show function. The config file exists, but it is empty (i.e, \"{}\")")


def initial_save(passed_settings, passed_filename="config.json"):
    return backend_save(passed_settings, passed_filename)


def backend_load(filename="config.json", debug_level=None):  # DON'T CALL ME DIRECTLY!
    """Used for loading the filename, do not call this function, instead call the \"append_settings\" function,
    or the \"add_settings_to_start\" for either task. This function and the \"backend_save\" function are the backbone for
    loading and saving file (But don't use them directly! I have wrapper functions setup for you to use,
    use them instead!)"""

    if isfile(filename):
        with open(filename) as target:
            try:
                json_data = json.load(target)
                if debug_level == 1:
                    print("DEBUGGING: The current json data is:", json_data)

                return json_data

            except json.JSONDecodeError:
                json_data = None
                return json_data

    else:
        json_data = {}
        return json_data


def backend_save(answers={}, filename="config.json"):  # DON'T CALL ME DIRECTLY!
    """"""

    with open(filename, "w") as target:
        output = json.dump(answers, target, indent=4, sort_keys=True)
        return output


def backend_append_values(answers={}, filename="config.json"):  # DON'T CALL ME DIRECTLY!
    """"""

    the_data = backend_load(filename)
    the_data.update(answers)
    backend_save(the_data)


def backend_add_values_to_start(answers={}, filename="config.json"):  # DON'T CALL ME DIRECTLY!
    """"""

    the_data = backend_load(filename)
    answers.update(the_data)
    backend_save(answers)
