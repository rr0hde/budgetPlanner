from art import logo
from time import sleep
import pyautogui

print(logo)
sleep(2)

user_exit = True

while user_exit:
    pyautogui.click(x=128, y=928)
    pyautogui.hotkey('alt', 'l')
    print("Please make a selection from the following choices:")
    print("\t1. Create Budget")
    print("\t2. View Budget")
    print("\t3. Edit Budget")
    print("\t0. Exit")
    user_choice = int(input("Enter choice here: "))

    if user_choice == 0:
        user_exit = False

    if user_choice == 1:
        pass

    if user_choice == 2:
        pass

    if user_choice == 3:
        pass
