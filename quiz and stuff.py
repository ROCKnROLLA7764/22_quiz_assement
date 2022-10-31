greeting = "Welcome to the" \
           " times tablez math quiz"
sides = "*" * 3

greeting = "{} {} {}".format(sides, greeting, sides)

top_bottom = "$" * len (greeting)

print(top_bottom)
print(greeting)
print(top_bottom)

show_instructions = input("have you played this game before").lower().strip()

rounds_played = 0

score = 0

if show_instructions == "yes" or show_instructions == "y":
    print("program continues")

elif show_instructions == "no":
    print("display instructions")
elif show_instructions == "n":
    print("display instructions")
else:
    print("please answer yes/no")

time_table =int(input("What times table do you want to be quizzed on? "))
max_value =int(input("Enter the maximum value for your times table: "))

print("Here is the {} times table quiz ... Good luck".format(time_table))

for x in range(1,max_value+1):


    print()
    print("*** Round #{} ***".format(rounds_played))
    answer = x * time_table
    guess = int(input("what is {} x {} = ".format(x,time_table)))
    rounds_played +=1
    if guess == answer:
        print("correct")
        score +=1

    else:
        print("incorrect, {} x {} = {}".format(x,time_table,answer))

    print("score")

