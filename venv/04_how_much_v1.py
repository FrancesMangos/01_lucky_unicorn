error = "Please enter a whole number between 1 and 10"

valid = False
while not valid:
    #ask the question
    response = int(input("How much money would you like to play with?"))

    #if the amount is too low or too high
    if 0 < response <= 10:
        print("You have asked to"
              " play with ${}".format(response))

    #output an error
    else:
        print(error)

