# !/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains the options menu for the program.
"""
from __future__ import print_function
import brianr
import Ben_audio
import kolaczkowski
import craig
import ade

__author__ = "Fearghal Hayes"
__date__ = "03/05/2020"
__credits__ = "Me, and the other participants in the Skills Demo 3 for the Programming Module"
__version__ = "0.0.1"


def options():
    """
    This is the options menu for the program, and runs when you press "5" on the main menu
    """
    print('\n\tOptions Menu \n\n'
          '1) Audio\n'
          '2) Gameplay\n'
          '3) Display\n'
          '4) Controls\n'
          '5) Exit\n')

    option = 0
    while option not in ["1", "2", "3", "4", "5"]:
        option = input("Please select a Main Menu option between 1 and 5: ")
        if option == "1":
            the_audio = Ben_audio.audio_options()  # This is Bento's function integrated into my options menu.
            return the_audio

        elif option == "2":
            the_gameplay = craig.gameplay()  # This is Craigs's function integrated into my options menu.
            return the_gameplay

        elif option == "3":
            the_display_menu = display()  # This is my "display" function integrated into my options menu.
            return the_display_menu

        elif option == "4":
            return {}
        elif option == "5":  # If the user choosing nothing, return an empty dictionary.
            print("Goodbye")
            return {}

        else:
            print("Invalid option, please select an option from the list.")  # The user must input a valid number,
            # otherwise the program will continue to loop until one has been entered.


def display():
    """
    Fearghal's display menu function, which is launched when the usr picks option "3" in the options menu
    """

    print('\n\tDisplay Menu \n\n'
          '1) Resolution\n'
          '2) Video Mode\n'
          '3) Frame Rate Limit\n'
          '4) Vertical Sync\n'
          '5) Quality\n'
          '6) Exit\n')

    the_display = 0
    while the_display not in ["1", "2", "3", "4", "5", "6"]:
        the_display = input("Please select a Main Menu option between 1 and 5: ")
        if the_display == "1":
            resolution = brianr.screen_resolution()  # Brian's screen resolution function is called when "1" is entered.
            return resolution
        elif the_display == "2":
            the_video_mode = ade.video_mode()  # Ade's video mode function is called when "2" is entered.
            return the_video_mode
        elif the_display == "3":
            the_fps_limit = kolaczkowski.framerate_limit()  # Tomasz's framerate limit function is called when "3" is
            # entered.
            return the_fps_limit
        elif the_display == "4":
            return {}
        elif the_display == "5":
            return {}
        elif the_display == "6":  # If the user exits, then no data is entered, so we must return an empty dictionary.
            print("Goodbye")
            return {}
        else:
            print("Invalid option, please select an option from the list.")  # The user must input a valid number,
            # or else the loop will keep on looping


if __name__ == "__main__":  # This prevents the user from running my function directly from the command line or
    # otherwise and instead tells the user to run the "setup.py" file instead
    print("HEY! Don't run me directly, I'm a module! I serve as a library for the setup.py file, run that instead.")
