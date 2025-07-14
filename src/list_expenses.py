import csv


def list_expenses(file):
    '''List all expenses'''
    with open(file, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            print(f'{expense[0]} {expense[1]} {expense[2]} ${expense[3]}')
