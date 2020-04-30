def colour():
    """
    Prompts the user to pick a colour from a menu and returns the colour name.
    Wolf, April 2020.
    """
    print(""
          "1) Black"
          "2) White"
          "3) Red"
          "3) Green"
          "4) Blue")
    selection = -1
    while selection not in range(0,5): 
        selection = input("Please select a colour (0-4): ")
        if colour == 0:
            return "#000000"
        elif colour == 1:
            return "#FFFFFF"
        elif colour == 2:
            return "#FF0000"
        elif colour == 3:
            return "#00FF00"
        elif colour == 4:
            return "#0000FF"
