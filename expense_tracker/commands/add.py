import csv

from ..core.file_service import get_filepath
from ..core.date_service import get_today_date
from ..core.args_service import add_args_validator


def add(description: str, amount: float):
    '''Add new expense'''
    filepath = get_filepath()
    new_id = 1
    date = get_today_date()

    if add_args_validator(description, amount):
        with open(filepath, 'r', newline='') as file:
            for expense in csv.reader(file):
                new_id += 1

        with open(filepath, 'a', newline='') as file:
            csv.writer(file).writerow(
                [
                    new_id,
                    date,
                    description,
                    amount
                ]
            )

        print(f'Expense added successfully (ID: {new_id})')


def run(args):
    add(args.description, args.amount)


def register(subparsers):
    add_parser = subparsers.add_parser(
        'add',
        help='add an expense with a description and amount'
    )
    add_parser.add_argument(
        '-d', '--description',
        type=str,
        required=True,
        help='expense description',
    )
    add_parser.add_argument(
        '-a', '--amount',
        type=float,
        required=True,
        help='expense amount',
    )
    add_parser.set_defaults(func=run)
