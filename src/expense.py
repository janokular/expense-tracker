import csv
from enums.MonthsEnum import MonthsEnum
from utils.date_service import *


def add_expense(description, amount, file):
    '''Add new expense'''
    id = 1
    date = get_current_date()

    with open(file, 'r', newline='') as csv_file:
        expenses_reader = csv.reader(csv_file)
        id += sum(1 for expense in expenses_reader)

    with open(file, 'a', newline='') as csv_file:
        expenses_writer = csv.writer(csv_file)
        expenses_writer.writerow([id,
                                 date,
                                 description,
                                 amount])

    print(f'Expense added successfully (ID: {id})')


def update_expense(id, description, amount, file):
    print(description)
    print(amount)

    print(f'Expense {id} updated successfully')


def delete_expense(id, file):

    print(f'Expense {id} deleted successfully')


def list_expenses(file):
    '''List all expenses'''
    with open(file, 'r', newline='') as csv_file:
        expenses_reader = csv.reader(csv_file)
        for expense in expenses_reader:
            print(f'{expense[0]} {expense[1]} {expense[2]} ${expense[3]}')


def summary_of_expenses(month, file):
    '''Summary of total or specific month expenses'''
    total = 0.0
    month_name = MonthsEnum(month).name if month else None

    with open(file, 'r', newline='') as csv_file:
        expenses_reader = csv.reader(csv_file)
        for expense in expenses_reader:
            date = expense[1]
            amount = float(expense[3])
            if not month or get_month_name(date) == month_name:
                total += amount

    print(f'Total expenses for {month_name}: ${total}' if month else 
          f'Total expenses: ${total}')
