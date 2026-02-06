import csv

from ..core.file_service import get_filepath
from ..core.print_service import column


def list():
    '''List all expenses'''
    filepath = get_filepath()
    expenses = []
    
    with open(filepath, 'r', newline='') as file:
        for expense in csv.reader(file):
            expenses.append(
                [
                    expense[0],
                    expense[1],
                    expense[2],
                    expense[3]
                ]
            )

    if expenses:
        column(expenses)
    else:
        print('No expenses for listing')


def register(subparsers):
    list_parser = subparsers.add_parser(
        'list',
        help='view all expenses'
    )
    list_parser.set_defaults(func=lambda args: list())
