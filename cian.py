"""
Asking the user to name their account for the play session.
"""
__author__ = "Cían Murphy"
__date__ = "May 2020"
__credits__ = "Part of Skills Demo 3"
__version__ = 0.1


def account():
    """
    Asks the user what they want their display name to be
    Cían , May 2020
    """
    print("\n What would you like your display name to be?")
    selection = 0
    account_name = input("Input:\n")
    return {"account_name": account_name}