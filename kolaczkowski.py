"""
Ask user for their choice of Frame Rate Limit!
"""

__author__ = "Tomasz Kolaczkowski"
__date__ = "7th May 2020"
__credits__ = "NET5 Programming and Design Principles 5N2927 - Skills Demo 3"
__version__ = 0.2


def framerate_limit():
    """
        Requests input from the user for their selection of Frame Rate Limit
    """
    print("\n\tFrame rate limit \n\n"
          "1) 60 Fps.\n"
          "2) 72 Fps.\n"
          "3) 90 Fps.\n"
          "4) 120 Fps.\n"
          "5) 144 Fps.\n"
          "6) 240 Fps.\n"
          "7) Unlimited.\n")
    framerate_limit = 0
    while framerate_limit not in ["1", "2", "3", "4", "5", "6", "7" ]:
        framerate_limit = input("Please select a Frame Rate Limit choice between 1 and 7:\t")
        if framerate_limit == "1":
            return {"framerate_limit": "60 Fps"}
        elif framerate_limit == "2":
            return {"framerate_limit": "72 Fps"}
        elif framerate_limit == "3":
            return {"framerate_limit": "90 Fps"}
        elif framerate_limit == "4":
            return {"framerate_limit": "120 Fps"}
        elif framerate_limit == "5":
            return {"framerate-limit": "144 Fps"}
        elif framerate_limit == "6":
            return {"framerate_limit": "240 Fps"}
        elif framerate_limit == "7":
            return {"framerate_limit": "Unlimited"}
        else:
            print("Please select a valid option from the list: 1,2,3,4,5,6 or 7!")
