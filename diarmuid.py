"""
Asking the user for the type of Creature's that the user want's to choose.
"""
__author__ = "Diarmuid Mahony"
__date__ = "May 2020"
__credits__ = "Part of Skills Demo 3"
__version__ = 0.1


def creatures():
    """
    Promps the user for there choice on the type of creature that the user wants to be
    in the game
    diarmuid , May 2020
    """
    print("\nClasses Menu \n1) Warrior\t\t2) Fighter\t\t3) Knight\n4) Paladin\t\t5) Barbarian\t6) Martial Artist\n7)"
          " Monk \t\t8)Berzerker\t\t9)Wizard ")
    selection = 0
    while selection not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        selection = input("Please select a class between  (1-9): ")
        if selection == "1":
            return "Warrior"
        elif selection == "2":
            return "Fighter"
        elif selection == "3":
            return "Knight"
        elif selection == "4":
            return "Paladin"
        elif selection == "5":
            return "Barbarian"
        elif selection == "6":
            return "Berzerker"
        elif selection == "7":
            return "Monk"
        elif selection == "8":
            return "Martial Artist"
        elif selection == "9":
            return "wizard"

def gender():
    print("Enter 1 if your male:\nEnter 2 if your Female:\nEnter 3 if your Other: ")
    selection = 0
    while selection not in ["1", "2", "3"]:
        selection = input("Please Enter your gender  (1-3): ")
        if selection == "1":
            return "Male"
        elif selection == "2":
            return "Female"
        elif selection == "3":
            return "Other"
