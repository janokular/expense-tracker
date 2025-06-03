import csv
import datetime
from enums.MonthsEnum import MonthsEnum


def add(description, amount, file):
    '''Add new expense'''
    id = 1

    with open(file, 'r', newline='') as csv_file:
        expense_reader = csv.reader(csv_file)
        id += sum(1 for row in expense_reader)

    with open(file, 'a', newline='') as csv_file:
        expense_writer = csv.writer(csv_file)
        expense_writer.writerow([id,
                                 description,
                                 amount,
                                 datetime.date.today().month])

    print(f'Expense added successfully (ID: {id})')


def update(id, description, amount, file):
    print(id)
    print(description)
    print(amount)


def list(file):
    pass


def delete(id, file):
    print(id)


def summary(month, file):
    if month:
        print(f'Total expenses for {MonthsEnum(month).name}: ${0}')
