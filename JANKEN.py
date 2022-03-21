import secrets

print("ROHAN, I CHALLENGE YOU TO A GAME OF JANKEN. YOU WILL NEVER DEFEAT ME!!!!!")
print("")
print("Play by typing \"rock\", \"paper\", or \"scissors\" into the prompt.")

def janken():
    # ---------------------------------------------VARIABLES & SETUP----------------------------------------------------
    player = ""
    cpu = ""
    print("")

    # ---------------------------------------------DATA ACQUIREMENT-----------------------------------------------------
    player = input("What do you decide to play? ")
    cpu = secrets.randbelow(3)

    # ---------------------------------------------CPU PLAY-------------------------------------------------------------
    if cpu == 0:
        cpu = "rock"
    elif cpu == 1:
        cpu = "paper"
    elif cpu == 2:
        cpu = "scissors"
    else:
        print("error creating cpu string; restarting program.")
        janken()

    # --------------------------------------------PLAYER PLAYS ROCK-----------------------------------------------------
    if player == "rock":
        print("You played rock!")
        if cpu == "paper":
            print("")
            print("Janken Boy played paper!")
            print("I PLAYED PAPER ROHAN. YOU LOSE!!!")
            print("")
            rematch = input("REMATCH? y or n: ")
            if rematch == "y":
                janken()
            elif rematch == "n":
                quit()
            else:
                print("Invalid input.")
                print("I DON'T CARE WHAT YOU SAY; WE'RE PLAYING AGAIN!")
                janken()
        elif cpu == "scissors":
            print("")
            print("Janken Boy played scissors!")
            print("NANIII??!! HOW COULD I HAVE LOST?")
            print("")
            rematch = input("REMATCH? y or n: ")
            if rematch == "y":
                janken()
            elif rematch == "n":
                quit()
            else:
                print("Invalid input.")
                print("I DON'T CARE WHAT YOU SAY; WE'RE PLAYING AGAIN!")
                janken()
        else:
            print("")
            print("Janken Boy played rock!")
            print("NANIII??!! IT WAS A TIE!")
            print("")
            rematch = input("REMATCH? y or n: ")
            if rematch == "y":
                janken()
            elif rematch == "n":
                quit()
            else:
                print("Invalid input.")
                print("I DON'T CARE WHAT YOU SAY; WE'RE PLAYING AGAIN!")
                janken()

    # -------------------------------------------PLAYER PLAYS PAPER-----------------------------------------------------
    elif player == "paper":
        print("You played paper!")
        if cpu == "scissors":
            print("")
            print("Janken Boy played scissors!")
            print("I PLAYED SCISSORS ROHAN. YOU LOSE!!!")
            print("")
            rematch = input("REMATCH? y or n: ")
            if rematch == "y":
                janken()
            elif rematch == "n":
                quit()
            else:
                print("Invalid input.")
                print("I DON'T CARE WHAT YOU SAY; WE'RE PLAYING AGAIN!")
                janken()
        elif cpu == "rock":
            print("")
            print("Janken Boy played rock!")
            print("NANIII??!! HOW COULD I HAVE LOST?")
            print("")
            rematch = input("REMATCH? y or n: ")
            if rematch == "y":
                janken()
            elif rematch == "n":
                quit()
            else:
                print("Invalid input.")
                print("I DON'T CARE WHAT YOU SAY; WE'RE PLAYING AGAIN!")
                janken()
        else:
            print("")
            print("Janken Boy played paper!")
            print("NANIII??!! IT WAS A TIE!")
            print("")
            rematch = input("REMATCH? y or n: ")
            if rematch == "y":
                janken()
            elif rematch == "n":
                quit()
            else:
                print("Invalid input.")
                print("I DON'T CARE WHAT YOU SAY; WE'RE PLAYING AGAIN!")
                janken()

    # ---------------------------------------------------PLAYER PLAYS SCISSORS------------------------------------------
    elif player == "scissors":
        print("You played scissors!")
        if cpu == "rock":
            print("")
            print("Janken Boy played rock!")
            print("I PLAYED ROCK ROHAN. YOU LOSE!!!")
            print("")
            rematch = input("REMATCH? y or n: ")
            if rematch == "y":
                janken()
            elif rematch == "n":
                quit()
            else:
                print("Invalid input.")
                print("I DON'T CARE WHAT YOU SAY; WE'RE PLAYING AGAIN!")
                janken()
        elif cpu == "paper":
            print("")
            print("Janken Boy played paper!")
            print("NANIII??!! HOW COULD I HAVE LOST?")
            print("")
            rematch = input("REMATCH? y or n: ")
            if rematch == "y":
                janken()
            elif rematch == "n":
                quit()
            else:
                print("Invalid input.")
                print("I DON'T CARE WHAT YOU SAY; WE'RE PLAYING AGAIN!")
                janken()
        else:
            print("")
            print("Janken Boy played scissors!")
            print("NANIII??!! IT WAS A TIE!")
            print("")
            rematch = input("REMATCH? y or n: ")
            if rematch == "y":
                janken()
            elif rematch == "n":
                quit()
            else:
                print("Invalid input.")
                print("I DON'T CARE WHAT YOU SAY; WE'RE PLAYING AGAIN!")
                janken()

    # ------------------------------------PLAYER ENTERS INVALID INPUT---------------------------------------------------
    else:
        print("ROHAN QUIT MESSING AROUND AND PLAY JANKEN WITH ME!!!")
        print("(Invalid Input.)")
        janken()

janken()