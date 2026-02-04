import csv

from ..core.file_service import get_file
from ..core.args_service import id_validator


def delete(id: int):
    '''Delete expense'''
    FILE = get_file()

    expenses = []
    
    if id_validator(id, FILE):
        with open(FILE, 'r', newline='') as csv_expenses:
            for expense in csv.reader(csv_expenses):
                if id != int(expense[0]):
                    expenses.append(expense)

        # Adjust IDs
        for expense in expenses[id - 1:]:
            expense[0] = int(expense[0]) - 1

        with open(FILE, 'w', newline='') as csv_expenses:
            csv.writer(csv_expenses).writerows(expenses)

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
