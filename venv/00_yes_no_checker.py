show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask user if they have played the game before
    show_instructions = input("Have thou played the"
                              " game before?").lower()

    # If input yes, continue program
    if show_instructions == "yes":
        print("thy program continues")

    elif show_instructions == "y":
        print("thy program continues")

    # If input no, display instructions
    elif show_instructions == "no":
        print("display thy instructions")

    elif show_instructions == "n":
        print("display thy instructions")

    #If input not yes or no, clarify question
    else:
        print("please insert a yes / no")
