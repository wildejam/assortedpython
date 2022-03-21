import secrets

def rng_guesser():
    value = secrets.randbelow(100)
    guess = ""
    guesses_left = 10
    play_again = ""
    print("")
    print("Try to guess the random integer number we have generated. We will tell you if your guess is too high or too low.")
    print("\nRules: \n1.) The number is between 1 and 100 (1 and 100 are included)" +
          "\n2.) No values other than integers! Not abiding by this rule will result in a crash." +
          "\n3.) You have 10 guesses. Once you use all 10 the game ends.")
    while guess != value and guesses_left > 0:
        print("")
        print("Guesses Left: " + str(guesses_left))
        if guesses_left > 0:
            guess = int(input("Your guess: "))
            if guess < value:
                guesses_left = guesses_left - 1
                print("Too low!")
            elif guess > value:
                guesses_left = guesses_left - 1
                print("Too high!")
            elif guess == value:
                print("Nice work! You got it!")
                play_again = input(
                    "\nDo you wish to play again? Please type Y or N (In capital letters!) for Yes or No: ")
                if play_again == "Y":
                    rng_guesser()
                elif play_again == "N":
                    exit()
                else:
                    print("Invalid Answer. Program terminating.")
            else:
                guesses_left = guesses_left - 1
                print("Invalid Number.")
        if guesses_left == 0:
            print("You are out of guesses. Better luck next time.")
            print("The number was " + str(value) + ".")
            play_again = input("\nDo you wish to play again? Please type Y or N (In capital letters!) for Yes or No: ")
            if play_again == "Y":
                rng_guesser()
            elif play_again == "N":
                exit()
            else:
                print("Invalid Answer. Program terminating.")

rng_guesser()