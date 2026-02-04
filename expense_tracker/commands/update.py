import csv

from ..core.file_service import get_file
from ..core.args_service import id_validator
from ..core.args_service import update_validator


def update(id: int, description: str, amount: float):
    '''Update expense's description or amount'''
    FILE = get_file()

    expenses = []

    if (
        id_validator(id, FILE)
        and update_validator(description, amount)
    ):
        with open(FILE, 'r', newline='') as csv_expenses:
            for expense in csv.reader(csv_expenses):
                expenses.append(expense)

        for expense in expenses:
            if id == int(expense[0]):
                if description:
                    expense[2] = description
                if amount:
                    expense[3] = amount

        with open(FILE, 'w', newline='') as csv_expenses:
            csv.writer(csv_expenses).writerows(expenses)

        print(f'Expense (ID: {id}) updated successfully')


def run(args):
    update(args.id, args.description, args.amount)


def register(subparsers):
    update_parser = subparsers.add_parser(
        'update',
        help='update an expense'
    )
    update_parser.add_argument(
        '-i', '--id',
        type=int,
        required=True,
        help='expense id',
    )
    update_parser.add_argument(
        '-d', '--description',
        type=str,
        help='expense description',
    )
    update_parser.add_argument(
        '-a', '--amount',
        type=float,
        help='expense amount',
    )
    update_parser.set_defaults(func=run)
