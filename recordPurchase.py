import pandas as pd


class RecordPurchase:

    def record_purchases(self, purchases):

        user_exit = True

        while user_exit:
            date_of_purchase = input("What was the date of purchase?: ")
            if date_of_purchase == 0:
                user_exit = False
            else:
                category = input("In what category does this belong?: ")
                amount = int(input("What was the amount?: "))
                purchases = {date_of_purchase: {category: amount}}

            df = pd.DataFrame(purchases)
            df.to_json('purchases.json')
