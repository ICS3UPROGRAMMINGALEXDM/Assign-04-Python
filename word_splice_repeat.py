#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Gets a string from the user, then asks how long they want the
# sub strings to be, along with how many times this sub string is repeated.
# The program will then loop through according to the users "order" and display
# The final string.

# function is used to split at each character, then input into an array.
# takes the argument string
def split_string(string):
    return[char for char in string]



def main():
    restartLoop = True

    while restartLoop:
        answerLoop = True
        errorLoop = True

        u_string = input("Enter a word or phrase to be splice and diced: ")
        # This calls the function that will
        charArr = split_string(u_string)

        while errorLoop:
            u_size = input(
                "Enter how many characters long you want the spliced word to be: "
            )
            u_copies = input(
                "Enter how many times you want the spliced word to repeat: "
            )

            try:
                size = int(u_size)
                copies = int(u_copies)
                if (copies < 1) or (size < 1) or (size > len(charArr)):
                    print(
                        "Make sure copies and size are greater than 0. AND that "
                        +"size is NOT greater than the amout of characters in the"
                        +" word/sentence")
                else:
                    errorLoop = False
                    print(charArr)

            except ValueError:
                print(
                    "Please ensure that the size and number of"
                    + " copies entered is a valid number")



if __name__ == "__main__":
    main()