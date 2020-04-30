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
    while selection not in range(0, 5):
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
