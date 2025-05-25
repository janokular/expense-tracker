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
            add()
        case 'update':
            update()
        case 'list':
            list()
        case 'delete':
            delete()
        case 'summary':
            summary()
        case _:
            print('Something went wrong')

if __name__ == '__main__':
    main()
