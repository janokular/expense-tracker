import csv

from ..core.file_service import get_file
from ..core.date_service import get_month_name
from ..enums.MonthsEnum import MonthsEnum


def summary(month: int):
    '''Summary of total or specific month expenses'''
    FILE = get_file()
    
    total = 0.0
    month_name = MonthsEnum(month).name if month else None

    with open(FILE, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            date = expense[1]
            amount = float(expense[3])
            if not month or get_month_name(date) == month_name:
                total += amount

    print(f'Total expenses for {month_name}: ${total}' if month else 
          f'Total expenses: ${total}')


def run(args):
    summary(args.month)


def register(subparsers):
    summary_parser = subparsers.add_parser(
        'summary',
        help='view a summary of all expenses'
    )
    summary_parser.add_argument(
        '-m', '--month',
        type=int,
        choices=range(1, 13),
        help='view a summary of expenses for a specific month'
    )
    summary_parser.set_defaults(func=run)
