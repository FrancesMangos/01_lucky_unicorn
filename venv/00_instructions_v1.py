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

def instructions():
    print("*** How to Play ***")
    print()
    print("The rules of the game go here")
    print()
    return ""
# Main code goes here...
played_before = yes_no("Have thou played "
                         "the game before?")

if played_before == "no":
    instructions()
else:
    print("program continues")
