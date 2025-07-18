import csv
from utils.date_service import get_current_date
from utils.args_validator import is_amount_valid, is_description_not_empty


def add_expense(description: str, amount: float, file):
    '''Add new expense'''
    id = 1
    date = get_current_date()

    if is_description_not_empty(description) and is_amount_valid(amount):
        with open(file, 'r', newline='') as csv_expenses:
            for expense in csv.reader(csv_expenses):
                id += 1

        with open(file, 'a', newline='') as csv_expenses:
            csv.writer(csv_expenses).writerow([id,
                                    date,
                                    description,
                                    amount])

        print(f'Expense added successfully (ID: {id})')
