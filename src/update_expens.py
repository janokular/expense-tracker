import csv
from utils.id_checker import is_id_in_range


def update_expense(id, description, amount, file):
    '''Update expense's description or amount'''
    expenses = []

    if is_id_in_range(id, file):
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

        print(f'Expense {id} updated successfully')
