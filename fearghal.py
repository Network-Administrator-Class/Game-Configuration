# !/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
import diarmuid
import wolf


def options():
    print("\nAudio \n1) Gameplay\t\t2) Display\n3) Controls\t\t4)")
    option = 0
    while option not in ["1", "2", "3", "4", "5"]:
        option = input("Please select a Main Menu option between 1 and 5:")
        if option == "1":
            return {"options": "audio"}
        elif option == "2":
            return {"options": "gameplay"}
        elif option == "3":
            return {"options": "display"}
        elif option == "4":
            print("Goodbye")
            return {}
        else:
            print("Invalid option, please select an option from the list.")


if __name__ == "__main__":
    print("HEY! Don't run me directly, I'm a module! I serve as a library for the setup.py file, run that instead.")
