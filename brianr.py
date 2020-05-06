"""
Ask user for their choice of Screen Resolution setting!
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
