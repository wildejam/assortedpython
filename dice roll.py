import random

def dice():
    user_input = "roll"
    print("This program will simulate rolling a dice. Type \"roll\" to roll the dice, and type \"quit\" to end the program." +
          "\nTyping anything else into the program will also result in it's termination.")
    while user_input == "roll":
        print("")
        user_input = input("What would you like to do?: ")
        if user_input == "roll":
            print(random.randrange(1,7))
    if(user_input == "quit"):
        quit()

dice()