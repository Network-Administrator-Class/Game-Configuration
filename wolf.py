"""Sample Code"""

__author__ = "Wolf Ó Spealáin"
__date__ = "April 2020"
__credits__ = "Part of Skills Demo 3"
__version__ = 0.1


def colour():
    """
    Prompts the user to pick a colour from a menu and returns the RGB code.
    Wolf, April 2020.
    """
    print("\nCOLOUR MENU\n\n1) Black\n2) White\n3) Red\n3) Green\n4) Blue\n")
    selection = -1
    while selection not in ["0", "1", "2", "3", "4"]:
        selection = input("Please select a colour (0-4): ")
        if selection == "0":
            return "#000000"
        elif selection == "1":
            return "#FFFFFF"
        elif selection == "2":
            return "#FF0000"
        elif selection == "3":
            return "#00FF00"
        elif selection == "4":
            return "#0000FF"


def buy_weapon():
    """Allows user to buy a weapon with money."""
    selection = None
    print("\nWeapons:\n1) Sword (150)\n2) Stick (5)\n0) Leave with buying.")
    while selection not in ["0", "1", "2"]:
        selection = input("Pick a weapon (1-2): ")
        if selection == "1":
            return {"Sword": 150}
        elif selection == "2":
            return {"Stick": 5}
