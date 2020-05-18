"""
Ask user for their choice of Video mode
"""

__author__ = "Ade Lawal"
__date__ = "18th May 2020"
__credits__ = "NET5 Programming and Design Principles 5N2927 - Skills Demo 3"
__version__ = 0.2


def video_mode():
    print('\n\tvideo mode \n\n'
          '1) Fullscreen\n'
          '2) Windowed\n'
          '3) Borderless Windowed\n')

    video = 0
    while video not in ["1", "2", "3",]:
        video = input("Please select a Video mode choice from 1 to 3:\t")
        if video == "1":
            return {"video_mode": "720p"}
        elif video == "2":
            return {"video_mode": "1080p"}
        elif video == "3":
            return {"video_mode": "1440p"}
        else:
            print("Please select a valid option from the list: 1,2, and 3!")