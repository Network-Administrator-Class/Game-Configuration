#!/bin/env python3

"""
Prototype of the initial configuration options for a multi-user role-playing-game.
"""

# from saving import *
import wolf  # Sample function: Prompts the user to pick a colour from a menu and returns the RGB code.
import diarmuid  # To get the classes of the user
import fearghals_functions
import brianr  # Screen resolution config.
import fearghal

__author__ = "Python Class"
__date__ = "April 2020"
__credits__ = "Part of Skills Demo 3"
__version__ = 0.1


def main():
    main_menu()


def main_menu():
    filename = "config.json"
    settings = fearghals_functions.load(filename)
    fearghals_functions.show()

    if settings.get('money') is None:
        money = 1000
        fearghals_functions.append_settings({"money": money})

    settings = fearghals_functions.load(filename)
    money = settings.get('money')

    choice = None
    while choice != "0":
        print("\n\nCONFIGURATION MENU\n")
        print("0) Exit configuration.")
        print("1) Flag colour :", settings.get('flag'))  # Code by Wolf
        print("2) The gender  :", settings.get('gender'))
        print("3) Creature :", settings.get('creatures'))
        print("4) Buy weapon :", settings.get("weapon"))
        print("5) Enter Options Menu")
        print("\nMoney:", money)
        choice = input("Enter menu choice (0 to 5): ")
        if choice == "1":
            flag = wolf.colour()
            fearghals_functions.append_settings({"flag": flag})
            settings = fearghals_functions.load(filename)
        elif choice == "2":
            gender = diarmuid.gender()
            fearghals_functions.append_settings({"gender": gender})
            settings = fearghals_functions.load(filename)

        elif choice == "3":
            creatures = diarmuid.creatures()
            fearghals_functions.append_settings({'creatures': creatures})
            settings = fearghals_functions.load(filename)
        elif choice == "4":
            purchase = wolf.buy_weapon()
            if purchase.get("Sword") is not None:
                weapon = purchase.get("Sword")
            elif purchase.get("Stick") is not None:
                weapon = purchase.get("Stick")
            elif purchase == {}:
                weapon = 0
            print("I have $", money, ", and the price for the weapon I have chosen is: $", weapon, sep="")  # Debug
            money = money - weapon
            fearghals_functions.append_settings({"weapon": weapon})
            fearghals_functions.append_settings({"money": money})
            settings = fearghals_functions.load(filename)

        elif choice == "5":
            options = fearghal.options()
            print(options)
            fearghals_functions.append_settings(options)

        elif choice == "0":
            print("Configuration saved. Goodbye!")
            exit()


#
# # Save Configuration File
# save(settings, the_filename)
# print("Goodbye! Configuration saved.")


# # Load Configuration File
# the_filename = "game.cfg"
# settings = load(the_filename)
# show(settings)
# money = settings.get("money")
#
# Main Menu

if __name__ == "__main__":
    main()
