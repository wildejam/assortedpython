import pyautogui
import time
# ---------------------------------------------STARTUP DIALOGUE---------------------------------------------------------
print("heya jamison, hope you're doing well. good day today yeah?")
print("type run to start, and move the mouse to a corner of the screen to stop if things go awry.")
print("good luck at school m80. stay determined")
# ---------------------------------------------FUNCTION-----------------------------------------------------------------
def tabopener():
    run = input("type run to start program: ")
    if run == "run":
        # -----------------countdown-----------------------------------
        print("")
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
        print("the program is now running")

        # ------------------actual program-----------------------------
        # open chrome
        pyautogui.moveTo(612, 748,)
        pyautogui.click(button = 'left')

        # opens coronatabs bookmark folder
        pyautogui.moveTo(658, 85, duration = 1)
        pyautogui.click(button = 'left')

        # opens google classroom & re-opens coronatabs folder
        pyautogui.moveTo(660, 135)
        pyautogui.click(button = 'middle')
        pyautogui.moveTo(658, 85)
        pyautogui.click(button='left')

        # opens google calendar & re-opens coronatabs folder
        pyautogui.moveTo(665, 166)
        pyautogui.click(button='middle')
        pyautogui.moveTo(658, 85)
        pyautogui.click(button='left')

        # opens school inbox
        pyautogui.moveTo(685, 206)
        pyautogui.click(button='middle')

        # opens personal inbox & re-opens coronatabs folder
        pyautogui.moveTo(774, 83)
        pyautogui.click(button='middle')
        pyautogui.moveTo(658, 85)
        pyautogui.click(button='left')

        # opens thisislanguage
        pyautogui.moveTo(696, 230)
        pyautogui.click(button='middle')
        # ----------------------------------exit dialogue-------------------------------------------------------
        print("aight my work here is done mate. have a good one.")
        input("press enter to quit.")


    else:
        print("")
        print("invalid input you idiot")
        tabopener()

tabopener()