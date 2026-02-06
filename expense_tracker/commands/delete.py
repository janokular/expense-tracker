import csv

from ..core.file_service import get_filepath
from ..core.args_service import id_validator


def delete(id: int):
    '''Delete expense'''
    filepath = get_filepath()
    expenses = []
    
    if id_validator(id, filepath):
        with open(filepath, 'r', newline='') as file:
            for expense in csv.reader(file):
                if id != int(expense[0]):
                    expenses.append(expense)

        for expense in expenses[id - 1:]:
            expense[0] = int(expense[0]) - 1

        with open(filepath, 'w', newline='') as file:
            csv.writer(file).writerows(expenses)

        print(f'Expense (ID: {id}) deleted successfully')


def run(args):
    delete(args.id)


def register(subparsers):
    delete_parser = subparsers.add_parser(
        'delete',
        help='delete an expense'
    )
    delete_parser.add_argument(
        '-i', '--id',
        type=int,
        required=True,
        help='expense id',
    )
    delete_parser.set_defaults(func=run)
