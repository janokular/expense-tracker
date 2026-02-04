import csv

from ..core.file_service import get_file
from ..core.date_service import get_today_date
from ..core.args_service import amount_validator
from ..core.args_service import description_validator


def add(description: str, amount: float):
    '''Add new expense'''
    FILE = get_file()

    new_id = 1
    date = get_today_date()

    if (
        description_validator(description)
        and amount_validator(amount)
    ):
        with open(FILE, 'r', newline='') as csv_expenses:
            for expense in csv.reader(csv_expenses):
                new_id += 1

        with open(FILE, 'a', newline='') as csv_expenses:
            csv.writer(csv_expenses).writerow(
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
