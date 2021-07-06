#Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input("Have thou played the game before?").lower()


        if response == "yes" or response == "y":
            response = "yes"
            return response

        # If input no, display instructions
        elif response == "no" or response == "n":
            response = "no"
            return response

        #If input not yes or no, clarify question
        else:
            print("<error> please insert a yes / no")

#Main code goes here...
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask user if they have played the game before
    show_instructions = input("Have thou played the game before?").lower()

    # If input yes, continue program
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("thy program continues")

    # If input no, display instructions
    elif show_instructions == "no"or show_instructions == "n":
        show_instructions = "no"
        print("display thy instructions")

    #If input not yes or no, clarify question
    else:
        print("<error> please insert a yes / no")


    print("You chose {}".format(show_instructions))
