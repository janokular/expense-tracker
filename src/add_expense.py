import csv
from utils.date_service import get_current_date


def add_expense(description, amount, file):
    '''Add new expense'''
    id = 1
    date = get_current_date()

    with open(file, 'r', newline='') as csv_expenses:
        id += sum(1 for expense in csv.reader(csv_expenses))

    with open(file, 'a', newline='') as csv_expenses:
        csv.writer(csv_expenses).writerow([id,
                                 date,
                                 description,
                                 amount])

    print(f'Expense added successfully (ID: {id})')
