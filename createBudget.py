from datetime import datetime as dt
import pandas as pd
from os.path import exists


class CreateBudget:

    def create_budget(self):

        if exists('budget.json'):
            print("Budget already exists.")
            return
        else:
            year = dt.now().year
            month = dt.now().month
            budget = {year: {month: {}}}

            user_exit = True

            while user_exit:
                category = input("Enter your category: ").title()
                if category == "0":
                    return budget
                else:
                    amount = int(input("Enter your amount: "))
                    budget[year][month][category] = amount

                df = pd.DataFrame(budget)
                df.to_json('budget.json')
