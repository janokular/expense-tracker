#!/bin/env python3


from utils.parser import parse_arguments
from utils.file_validator import validate_file
from src.expenses import *


def main():
    CSV_FILE = 'expenses.csv'

    validate_file(CSV_FILE)

    args = parse_arguments()

    match args.action:
        case 'add':
            add(args.description, args.amount, CSV_FILE)
        case 'update':
            update(args.id, args.description, args.amount, CSV_FILE)
        case 'list':
            list(CSV_FILE)
        case 'delete':
            delete(args.id, CSV_FILE)
        case 'summary':
            summary(args.month, CSV_FILE)
        case _:
            print('Something went wrong')

if __name__ == '__main__':
    main()
