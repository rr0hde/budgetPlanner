from art import logo
from time import sleep
from createBudget import CreateBudget
from viewBudget import ViewBudget
from editBudget import EditBudget
import pandas as pd
import os
import json
import pyautogui

print(logo)
# sleep(2)

user_exit = True

while user_exit:

    print("Please make a selection from the following choices:")
    print("\t1. Create Budget")
    print("\t2. View Budget")
    print("\t3. Edit Budget")
    print("\t4. Delete Budget")
    print("\t0. Exit")
    user_choice = int(input("Enter choice here: "))

    if user_choice == 0:
        user_exit = False

    if user_choice == 1:
        create_budget = CreateBudget()
        budget = create_budget.create_budget()
        # user_exit = False

    if user_choice == 2:
        file = 'budget.json'
        with open(file) as budget_file:
            dict_budget = json.load(budget_file)

        print(dict_budget['2022'])
        budget = pd.DataFrame.from_dict(dict_budget['2022'])
        budget.reset_index(level=0, inplace=True)
        print(budget)
        # budget_normalize = pd.json_normalize(budget[2022])
        # print(budget_normalize)
        # df = pd.DataFrame.from_dict(budget)
        # print(df)
        # time.sleep(10)
        pass

    if user_choice == 3:
        edit_budget = EditBudget()
        budget = edit_budget.edit_budget(budget)
        print(budget)

    if user_choice == 4:
        os.remove('budget.json')
