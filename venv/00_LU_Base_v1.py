import random

#Functions go here
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            #ask the question
            response = int(input(question))

            #if the amount is too low or too high
            if low < response <= high:
                return response


            #output an error
            else:
                print(error)

        except ValueError:
            print(error)

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

#Main routine goes here
played_before = yes_no("Have thou played "
                         "the game before?")

if played_before == "no":
    instructions()
else:
    print("program continues")

how_much = num_check("How much money would you "
                             "like to play with?", 0, 10 )

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    #increase # of rounds played
    rounds_played += 1

    #print round number
    print()
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)

    #Adjust balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
        else:
            chosen = "zebra"
        balance -= 0.5

    print("You got a {}. Your balance is ${:.2f}".format(chosen, balance))
    #If balance is low,exit the game and output suitable message
    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print("Final Balance", balance)
