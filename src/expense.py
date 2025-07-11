import csv
from enums.MonthsEnum import MonthsEnum
from utils.date_service import *


def add(description, amount, file):
    '''Add new expense'''
    id = 1
    date = get_current_date()

    with open(file, 'r', newline='') as csv_file:
        expense_reader = csv.reader(csv_file)
        id += sum(1 for expense in expense_reader)

    with open(file, 'a', newline='') as csv_file:
        expense_writer = csv.writer(csv_file)
        expense_writer.writerow([id,
                                 date,
                                 description,
                                 amount])

    print(f'Expense added successfully (ID: {id})')


def update(id, description, amount, file):
    print(description)
    print(amount)

    print(f'Expense {id} updated successfully')


def list(file):
    '''List all expenses'''
    with open(file, 'r', newline='') as csv_file:
        expense_reader = csv.reader(csv_file)
        for expense in expense_reader:
            print(f'{expense[0]} {expense[1]} {expense[2]} ${expense[3]}')


def delete(id, file):

    print(f'Expense {id} deleted successfully')


def summary(month, file):
    '''Summary of total or specific month expenses'''
    total = 0.0

    with open(file, 'r', newline='') as csv_file:
        expense_reader = csv.reader(csv_file)
        for expense in expense_reader:
            if month:
                if (get_month_from_date(expense[1]) == MonthsEnum(month).name):
                    total += float(expense[3])
            else:
                total += float(expense[3])

    if month:
        print(f'Total expenses for {MonthsEnum(month).name}: ${total}')
    else:        
        print(f'Total expenses: ${total}')
