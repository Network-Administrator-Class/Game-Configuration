# !/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import brianr


def options():
    print('\n\tOptions Menu \n\n'
          '1) Audio\n'
          '2) Gameplay\n'
          '3) Display\n'
          '4) Controls\n')

    option = 0
    while option not in ["1", "2", "3", "4", "5"]:
        option = input("Please select a Main Menu option between 1 and 5: ")
        if option == "1":
            return {"options": "audio"}
        elif option == "2":
            return {"options": "gameplay"}
        elif option == "3":
            the_display_menu = display()
            return the_display_menu

        elif option == "4":
            print("Goodbye")
            return {}
        else:
            print("Invalid option, please select an option from the list.")


def display():
    print('\n\tDisplay Menu \n\n'
          '1) Resolution\n'
          '2) Video Mode\n'
          '3) Frame Rate Limit\n'
          '4) Vertical Sync\n'
          '5) Quality\n'
          '6) Exit and Save\n')

    # print("\nResolution \n1) Video Mode\t\t2) Frame Rate Limit\n3) Vertical Sync\t\t4) Quality\t\t5)")
    the_display = 0
    while the_display not in ["1", "2", "3", "4", "5"]:
        the_display = input("Please select a Main Menu option between 1 and 5: ")
        if the_display == "1":
            resolution = brianr.screen_resolution()
            display_list = {"display": [resolution]}
            return display_list

        elif the_display == "6":
            print("Goodbye")
            return {}
        else:
            print("Invalid option, please select an option from the list.")


if __name__ == "__main__":
    print("HEY! Don't run me directly, I'm a module! I serve as a library for the setup.py file, run that instead.")
