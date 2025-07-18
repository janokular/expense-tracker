import csv
from utils.args_validator import is_id_in_range
from utils.args_validator import is_amount_valid, is_description_not_empty


def update_expense(id: int, description: str, amount: float, file):
    '''Update expense's description or amount'''
    expenses = []

    print(description)

    if is_id_in_range(id, file) and (is_description_not_empty(description) or is_amount_valid(amount)):
        with open(file, 'r', newline='') as csv_expenses:
            for expense in csv.reader(csv_expenses):
                expenses.append(expense)

        for expense in expenses:
            if id == int(expense[0]):
                if description:
                    expense[2] = description
                if amount:
                    expense[3] = amount

        with open(file, 'w', newline='') as csv_expenses:
            csv.writer(csv_expenses).writerows(expenses)

        print(f'Expense (ID: {id}) updated successfully')
