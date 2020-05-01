#!/bin/env python3

"""
Prototype of the initial configuration options for a multi-user role-playing-game.
"""

from saving import *
import wolf  # Sample function: Prompts the user to pick a colour from a menu and returns the RGB code.

__author__ = "Python Class"
__date__ = "April 2020"
__credits__ = "Part of Skills Demo 3"
__version__ = 0.1

# Load Configuration File
filename = "game.cfg"
settings = load(filename)
show(settings)
money = settings.get("money")

# Main Menu
choice = None
while choice != "0":
    print("\n\nCONFIGURATION MENU\n")
    print("0) Exit and save configuration.")
    print("1) Flag colour :", settings.get('flag'))  # Code by Wolf
    print("2) Magic powers :", settings.get('power'))
    print("3) Creature :", settings.get('creature'))
    print("4) Buy weapon :", settings.get('weapon'))
    print("\nMoney:", settings.get('money'))
    choice = input("Enter menu choice (1-4): ")
    if choice == "1":
        flag = wolf.colour()
        settings.update({"flag": flag})
    if choice == "4":
        purchase = wolf.buy_weapon()
        weapon = purchase[0]
        money = money - purchase[1]
        print(weapon, money)
        settings.update({"weapon": weapon})
        settings.update({"money": money})

# Save Configuration File
save(settings, filename)
print("Goodbye! Configuration saved.")
