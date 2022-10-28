import pandas as pd


class EditBudget:

    def edit_budget(self, budget):
        print(budget)
        category = input("What would you like to edit: ")
        print(budget[2022][10][category])
        amount = input("What is the new amount: ")
        budget[2022][10][category] = amount

        df = pd.DataFrame(budget)
        df.to_json('budget.json')

        return budget
