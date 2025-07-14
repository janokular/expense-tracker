import csv
from utils.id_checker import is_id_in_range


def update_expense(id, description, amount, file):
    '''Update expense's description or amount'''
    if is_id_in_range(id, file):
        print(description)
        print(amount)

        print(f'Expense {id} updated successfully')
