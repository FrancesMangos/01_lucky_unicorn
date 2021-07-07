# Functions go here...
def yes_no(question):
    valid = False
    while not valid:
        response = input("Have thou played "
                         "the game before?").lower()


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

# Main code goes here...
show_instructions = yes_no("Have thou played "
                         "the game before?").lower()
print("You chose {}".format(show_instructions))
