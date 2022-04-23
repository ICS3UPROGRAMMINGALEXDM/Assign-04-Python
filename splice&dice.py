#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Gets a string from the user, then asks how long they want the
# sub strings to be, along with how many times this sub string is repeated.
# The program will then loop through according to the users "order" and display
# The final string.
import colorama
from colorama import Style, Fore

# function is used to split at each character, then input into an array.
# takes the argument string
def split_string(string):
    return [char for char in string]


# function is used to loop through each letter to match the size of the
# sub word/phrase and loops through that loop to match the number of copies
def looping():
    final_string = ""
    new_string = ""
    counter = 0
    # Loop is to match the number of copies
    for number in range(copies):

        for number in range(size):
            new_string = new_string + charArr[counter]
            counter += 1
        # final_string is the string that will be displayed to the user
        final_string = final_string + new_string
        # resetting variables so that they can be looped starting from 0 again
        new_string = ""
        counter = 0
    print("\nThe Splice&Dice result is...")
    print(Fore.YELLOW + final_string)


def main():
    restartLoop = True

    while restartLoop:
        answerLoop = True
        errorLoop = True

        u_string = input(
            Style.BRIGHT + Fore.WHITE + "Enter a word or phrase to be Splice&Diced: "
        )
        # This calls the function that will
        global charArr
        charArr = split_string(u_string)
        # Loop is here so that the user can re-enter the parameters if they were invalid
        while errorLoop:
            u_size = input(
                Fore.WHITE
                + "Enter how many characters long you want the Splice&Diced word to be: "
            )
            u_copies = input(
                "Enter how many times you want the Splice&Diced word to repeat: "
            )
            # Error checking
            try:
                global size
                size = int(u_size)
                global copies
                copies = int(u_copies)
                if (copies < 1) or (size < 1) or (size > len(charArr)):
                    print(
                        "Make sure copies and size are greater than 0. AND that "
                        + "size is NOT greater than the amout of characters in the"
                        + " word/phrase"
                    )
                else:
                    errorLoop = False
                    # Calls function to create the final string
                    looping()
                    # Used to ask user if they would like to restart program
                    while answerLoop:
                        answer = input(
                            Fore.WHITE
                            + "\nWould you like to Splice&Dice another word? (y/n): "
                        )

                        if answer == "y":
                            answerLoop = False
                        elif answer == "n":
                            answerLoop = False
                            restartLoop = False
                        else:
                            print("I don't understand, please try again.")

            except ValueError:
                print(
                    Fore.RED
                    + "Please ensure that the size and number of"
                    + " copies entered is a valid number"
                )


if __name__ == "__main__":
    main()
