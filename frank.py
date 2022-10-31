import random

# Functions go here :...
def yes_no(question):

    valid = False
    while not valid:

        # asks user for input
        response = input(question).lower()
        # assesses response as yes/no or prompts correct input
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or "n":
            response = "no"
            return response
        else:
            print("Please enter yes or no")


def instructions() :
    print("****How to play****")
    print()
    print("The rules of the game go here")
    print()
    return ""

def number_check(question):
    error = "please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if 0 < response <= 10:
                print("You have asked to play with ${}".format(response))
                return response
            # output an error
            else:
                print(error)

        except ValueError:
            print(error)


# main routine
played_before = yes_no("have you played this game before").lower().strip()

if played_before == "no":
    instructions()

how_much = number_check("how much do you want to play with ?")
balance = how_much

# main routine goes here
tokens = ["unicorn","horse", "horse","zebra", "zebra", "donkey","donkey"]

rounds_played = 0

play_again = input("press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1
    chosen = random.choice(tokens)

    # Adjust balance
    if chosen == "unicorn":
        balance += 5
    elif chosen == "donkey":
        balance -= 1
    elif chosen == "zebra":
        balance -= 0.5
    else:
        chosen == "horse"
        balance -=0.5

    print("you got a {}. your balance is ${}".format(chosen,balance))

    if balance < 1:
        play_again = "xxx"
        print("sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print("your final balance is ${}".format(balance))
print("thank you for playing goodbye")
