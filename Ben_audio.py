#!/usr/bin/env python3

"""
Ask user the choice of sound settings
"""

____author__ = "Bento Pedro Langa"
____date____ = "6th May 2020"
____credits_ = "NET5 Programming and Design Principles 5N2927 - Skills Demo 3"
____version_ = 1.0


def audio_options():
    """
        Requests input from the user for their selection of audio options.
    """
    print("\n\tVolume Control \n\n"
          "1) Master.\n"
          "2) Effects.\n"
          "3) Voice.\n"
          "4) Footsteps.\n"
          "5) Back.\n")
    choice = 0
    while choice not in ["1", "2", "3", "4", "5"]:
        resolution = input("Please select audio settings of choice from the menu between 1 and 4:\t")
        if choice == "1":
            return {"audio": "Master"}
        elif choice == "2":
            return {"audio": "Effects"}
        elif choice == "3":
            return {"audio": "Voice"}
        elif choice == "4":
            return {"audio": "Footsteps"}
        elif choice == "5":
            return {"choice": "Back"}

        else:
            print("Please select a valid option from the Volume Control Menu")
