#!/bin/env python3

"""
Prototype the initial configuration options for a multi-user role-playing-game.
"""

from saving import *
from wolf import *  # Sample function: Prompts the user to pick a colour from a menu and returns the RGB code.

__author__ = "Python Class"
__date__ = "April 2020"
__credits__ = "Part of Skills Demo 3"
__version__ = 0.1

# Load Configuration File
filename = "game.cfg"
settings = load(filename)
show(settings)

# Sample Code (Player Flag Colour)
flag = colour()

# Save Configuration File
settings.update({"flag": flag})
save(settings, filename)
