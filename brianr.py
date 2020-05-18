#!/usr/bin/env python3

"""
Ask user for their choice of Screen Resolution setting!
Algorithm:
Step 1: Output choices to user 1 to 4
step 2: Request input to user for choices 1 to 4
step 3: if choice selection is not in 1 to 4
step 4: ask user to input a valid answer
step 5: loop steps 3 and 4 until a valid answer is inputted by the user
step 6: if user input is a valid answer output the corresponding option to the json file.

Testing:
Test 1 : user choice input '1' to select "720p"
Test 2 : user choice input '2' to select "1080p"
Test 3 : user choice input '3' to select "1440p"
Test 4 : user choice input '4' to select "2160p"

result test 1: "resolution": "720p"
result test 2: "resolution": "1080p"
result test 3: "resolution": "1440p"
result test 4: "resolution": "2160p"
"""

__author__ = "Brian Rudden"
__date__ = "5th May 2020"
__credits__ = "NET5 Programming and Design Principles 5N2927 - Skills Demo 3"
__version__ = 0.2


def screen_resolution():
    """
        Requests input from the user for their selection of Screen Resolution
    """
    print("\n\tScreen Resolution Configuration \n\n"
          "1) 1280x720 — HD / 720p.\n"
          "2) 1920x1080 — FHD (Full HD) / 1080p.\n"
          "3) 2560x1440 — QHD/WQHD (Quad HD) / 1440p.\n"
          "4) 3840x2160 — UHD (Ultra HD) / 4K 2160p\n")
    resolution = 0
    while resolution not in ["1", "2", "3", "4", ]:
        resolution = input("Please select a Screen Resolution choice between 1 and 4:\t")
        if resolution == "1":
            return {"resolution": "720p"}
        elif resolution == "2":
            return {"resolution": "1080p"}
        elif resolution == "3":
            return {"resolution": "1440p"}
        elif resolution == "4":
            return {"resolution": "2160p"}
        else:
            print("Please select a valid option from the list: 1,2,3 or 4!")
