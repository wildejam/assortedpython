import pyautogui
import time

# -------------------------------------------------MOUSE FUNCTION PROGRAM-----------------------------------------------

def autoclicker():
    run = input("Type \"run\" to begin the program: ")
    if run == "run":
        print("Program running in 10 seconds.")
        time.sleep(5)
        print("Program running in 5 seconds.")
        time.sleep(1)
        print("Program running in 4 seconds.")
        time.sleep(1)
        print("Program running in 3 seconds.")
        time.sleep(1)
        print("Program running in 2 seconds.")
        time.sleep(1)
        print("Program running in 1 second.")
        time.sleep(1)
        print("The program is now running. To stop it, either exit the program manually or move the mouse cursor to" +
              " a corner of the screen very quickly.")
        while run == "run":
            pyautogui.click()
    else:
        print("")
        print("Invalid Input.")
        autoclicker()

# -----------------------------------------STARTUP DIALOGUE & CALLING THE FUNCTION--------------------------------------
print("")
print("Screen " + str(pyautogui.size()))
print("Current " + str(pyautogui.position()))
print("")
print("This is a mouse autoclicker program. It will make the mouse click constantly while active.")
print("To run it type \"run\". You will then be given a 10 second countdown before it begins.")
print("Be careful! This program can lead to lots of grief if not handled properly.")
print("IMPORTANT: TO TERMINATE THE PROGRAM, MOVE THE MOUSE TO ANY OF THE 4 CORNERS OF THE SCREEN. DOING SO WILL END "
      "THE PROGRAM.")
print("")

autoclicker()