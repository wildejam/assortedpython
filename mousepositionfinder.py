import pyautogui
import time
print(pyautogui.size())
def findmouse():
    run = input("type run to start: ")
    if run == "run":
        time.sleep(3)
        print(pyautogui.position())
        quit = input("quit program?: ")
        if quit:
            exit()
    else:
        print("invalid input")
        findmouse()

findmouse()