#!/bin/env python3


from utils.parser import parse_arguments
from utils.file_service import validate_file
from src.expense import *


def main():
    CSV_FILE = 'expenses.csv'

    validate_file(CSV_FILE)

    args = parse_arguments()

    match args.action:
        case 'add':
            add_expense(args.description, args.amount, CSV_FILE)
        case 'update':
            update_expense(args.id, args.description, args.amount, CSV_FILE)
        case 'delete':
            delete_expense(args.id, CSV_FILE)
        case 'list':
            list_expenses(CSV_FILE)
        case 'summary':
            summary_of_expenses(args.month, CSV_FILE)
        case _:
            print('Something went wrong')

if __name__ == '__main__':
    main()
