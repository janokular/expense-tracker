import csv
from enums.MonthsEnum import MonthsEnum
from utils.date_service import *
from utils.id_checker import is_id_in_range


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


def update_expense(id, description, amount, file):
    print(description)
    print(amount)

    print(f'Expense {id} updated successfully')


def delete_expense(id, file):
    '''Delete expense'''
    if is_id_in_range(id, file):
        with open(file, 'r', newline='') as csv_expenses:
            expenses = [expense for expense in csv.reader(csv_expenses) if int(expense[0]) != id]

        # Adjust IDs
        for expense in expenses[id - 1:]:
            expense[0] = int(expense[0]) - 1

        with open(file, 'w', newline='') as csv_expenses:
            csv.writer(csv_expenses).writerows(expenses)

        print(f'Expense {id} deleted successfully')


def list_expenses(file):
    '''List all expenses'''
    with open(file, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            print(f'{expense[0]} {expense[1]} {expense[2]} ${expense[3]}')


def summary_of_expenses(month, file):
    '''Summary of total or specific month expenses'''
    total = 0.0
    month_name = MonthsEnum(month).name if month else None

    with open(file, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            date = expense[1]
            amount = float(expense[3])
            if not month or get_month_name(date) == month_name:
                total += amount

    print(f'Total expenses for {month_name}: ${total}' if month else 
          f'Total expenses: ${total}')
