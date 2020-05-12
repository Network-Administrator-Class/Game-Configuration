"""
Will determine the gameplay settings
"""
__author__ = "Craig O'Connor"
__date__ = "May 2020"
__credits__ = "Part of Skills Demo 3"
__version__ = 0.1


def gameplay():
    print('\n\tGameplay Menu \n\n'
          '1) Difficulty\n'
          '2) Field of view\n'
          '3) Input device\n'
          '4) Sensitivity\n'
          '5) Exit\n')

    user_choice = 0
    while user_choice not in ["1", "2", "3", "4", "5"]:
        user_choice = input("Enter the setting in which you wish to change")
        if user_choice == "1":
            the_difficulty = difficulty()
            return the_difficulty

        elif user_choice == "2":
            the_fov = fov()
            return the_fov
        elif user_choice == "3":
            the_input_dev = input_device()
            return the_input_dev

        elif user_choice == "4":
            the_sensitivity = sensitivity()
            return the_sensitivity

        elif user_choice == "5":
            print("Goodbye")
            return {}

        else:
            print("Invalid option, please select an option from the list.")


def difficulty():
    print('\n\tDifficulty Menu \n\n'
          '1) Easy\n'
          '2) Normal\n'
          '3) Hard\n'
          '4) Exit\n')

    the_difficulty = 0
    while the_difficulty not in ["1", "2", "3", "4"]:
        the_difficulty = input("Please select a Main Menu option between 1 and 5: ")

        if the_difficulty == "1":
            return {"difficulty": "easy"}

        elif the_difficulty == "2":
            return {"difficulty": "normal"}

        elif the_difficulty == "3":
            return {"difficulty": "hard"}

        elif the_difficulty == "4":
            print("Goodbye")
            return {}

        else:
            print("Invalid option, please select an option from the list.")


def fov():
    print('\n\tFielf of View Menu \n\n')

    the_fov = 60

    while the_fov >= 60 and the_fov <= 120:
        try:
            the_temp_fov = int(input("Please input an FOV between 60 and 120:"))

            if the_temp_fov < 60 or the_temp_fov > 120:
                print("Invalid option, please input an FOV between 60 and 120.")

            else:
                the_fov = str(the_temp_fov)
                return {"fov": the_fov}

        except ValueError:
            print("Error, please enter a valid number")
            continue


def sensitivity():
    print('\n\tMouse Sensitivity Menu \n\n')

    the_sensitivity = 50

    while the_sensitivity >= 1 and the_sensitivity <= 150:
        try:
            the_temp_sensitivity = int(input("Please input a sensitivity between 1 and 150:"))

            if the_temp_sensitivity < 1 or the_temp_sensitivity > 150:
                print("Invalid option, please input a sensitivity between 1 and 150.")

            else:
                the_sensitivity = str(the_temp_sensitivity)
                return {"mouse_sensitivity": the_sensitivity}

        except ValueError:
            print("Error, please enter a valid number")
            continue
