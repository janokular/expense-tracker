import csv

from ..core.file_service import get_file
from ..core.print_service import column_print


def list():
    '''List all expenses'''
    FILE = get_file()
    
    expenses = []
    
    with open(FILE, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            expenses.append(
                [
                    expense[0],
                    expense[1],
                    expense[2],
                    f'${expense[3]}'
                ]
            )

    if expenses:
        column_print(expenses)


def register(subparsers):
    list_parser = subparsers.add_parser(
        'list',
        help='view all expenses'
    )
    list_parser.set_defaults(func=lambda args: list())
