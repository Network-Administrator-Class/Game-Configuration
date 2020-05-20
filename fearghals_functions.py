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
    """This function is for loading the data from the file. Usually, you would store this functions value to a variable,
    then call the variable to get information from the file."""
    settings = backend_load(passed_filename, debug_level)
    return settings


def show(filename="config.json"):  # CALL ME WHEN NEEDED!
    """This function is for showing the user the current JSON data in the file. You normally wouldn't assign a
    variable to this function, and would instead call this function directly with the file you want to show the data
    of as a parameter."""
    the_data = backend_load(filename)

    if the_data != {}:
        print("You called the show function, the current json data is: ", the_data)

    elif the_data == {}:
        print("You called the show function. The config file exists, but it is empty (i.e, \"{}\")")


def backend_load(filename="config.json", debug_level=None):  # DON'T CALL ME DIRECTLY!
    """Used for loading the filename, do not call this function, instead call the \"append_settings\" function,
    or the \"add_settings_to_start\" for either task. This function and the \"backend_save\" function are the
    backbone for loading and saving file (But don't use them directly! I have wrapper functions setup for you to use,
    use them instead!) """

    if isfile(filename):
        with open(filename) as target:
            try:
                json_data = json.load(target)
                if debug_level == 1:
                    print("DEBUGGING: The current json data is:", json_data)  # This is for debugging purposes.
                return json_data

            except json.JSONDecodeError:
                json_data = None
                return json_data

    else:
        json_data = {}
        return json_data


def backend_save(answers={}, filename="config.json"):  # DON'T CALL ME DIRECTLY!
    """This function saves the data passed into it to the file passed into it. Don't call this file directly,
    instead use the wrapper functions at the top of this file, the "append_settings", or the "add_settings_to_start"
    functions, for either of your needs."""

    with open(filename, "w") as target:
        output = json.dump(answers, target, indent=4, sort_keys=True)
        return output


def backend_append_values(answers={}, filename="config.json"):  # DON'T CALL ME DIRECTLY!
    """This function is required by the "append_settings" function to append the data passed into it into the passed
    filename. Don't call this file directly, instead use the wrapper function at the top of this file,
    the "append_settings" function."""

    the_data = backend_load(filename)
    the_data.update(answers)
    backend_save(the_data)


def backend_add_values_to_start(answers={}, filename="config.json"):  # DON'T CALL ME DIRECTLY!
    """This function does the same this as the above function "backend_append_values", but adds the data to the start
    of the file. Don't call this file directly, instead use the wrapper function at the top of this file,
    the "add_settings_to_start" function."""

    the_data = backend_load(filename)
    answers.update(the_data)
    backend_save(answers)
