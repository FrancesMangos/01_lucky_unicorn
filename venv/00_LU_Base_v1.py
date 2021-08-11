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
    statement_generator("How to Play", "*")
    print()
    print("Choose a starting amount (minimum $1, maximum $10)")
    print()
    print("Then press <enter> to play."
          " You will either get a horse, a zebra, a donkey or a unicorn")
    print()
    print("It costs $1 per round. Depending on your prize you might win some money back. "
          "Here are the payout amounts:")
    print("Unicorn: $5.00 (Balance increases by $4")
    print("Horse: $0.50 (Balance decreases by $0.50")
    print("Zebra: $0.50 (Balance decreases by $0.50")
    print("Donkey: $0.00 (Balance decreases by $1")

    return ""

def statement_generator(statement, decoration):

    sides = decoration * 3

    greeting = "{} {} {}".format(sides, statement, sides)

    top_bottom = decoration * len(greeting)

    print(top_bottom)
    print(greeting)
    print(top_bottom)

    return ""

#Main routine goes here
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

played_before = yes_no("Have thou played "
                         "the game before?")

if played_before == "no":
    instructions()
else:
    print("program continues")

print()
statement_generator("Let's get Started", "-")
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
    print("Round #{}".format(rounds_played))

    chosen_num = random.randint(1, 100)

    #Adjust balance
    if 1 <= chosen_num <= 5:
        prize_decoration = "!"
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        prize_decoration = "@"
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            prize_decoration = "+"
            chosen = "horse"
        else:
            chosen = "zebra"
            prize_decoration = "~"
            balance -= 0.5

    outcome = "You got a {}. Your balance is:" \
              " ${:.2f}".format(chosen, balance)

    statement_generator(outcome, prize_decoration)

    #If balance is low,exit the game and output suitable message
    if balance < 1:
        play_again = "xxx"
        statement_generator("Sorry you have run out of money", ".")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print("Final Balance:", balance)
