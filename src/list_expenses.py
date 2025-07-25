import csv
from utils.table_print import print_table


def list_expenses(file):
    '''List all expenses'''
    expenses = []

    with open(file, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            expenses.append([expense[0],
                            expense[1],
                            expense[2],
                            f'${expense[3]}'])
    
    if expenses:
        print_table(expenses)
