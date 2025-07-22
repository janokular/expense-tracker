import argparse


def parse_arguments():
    '''Parse arguments needed for the program's logic'''
    parser = argparse.ArgumentParser(description='Program used to track and manage your expenses')

    subparsers = parser.add_subparsers(dest='action')

    add_parser = subparsers.add_parser('add', help='add an expense with a description and amount')
    add_parser.add_argument('--description', required=True)
    add_parser.add_argument('--amount', required=True, type=float)

    delete_parser = subparsers.add_parser('delete', help='delete an expense')
    delete_parser.add_argument('--id', required=True, type=int)

    subparsers.add_parser('list', help='view all expenses')

    summary_parser = subparsers.add_parser('summary', help='view a summary of all expenses')
    summary_parser.add_argument('--month', type=int, choices=range(1, 12), help='view a summary of expenses for a specific month')

    update_parser = subparsers.add_parser('update', help='update an expense')
    update_parser.add_argument('--id', required=True, type=int)
    update_parser.add_argument('--description')
    update_parser.add_argument('--amount', type=float)

    args =  parser.parse_args()

    if not args.action:
        parser.error('No arguments provided')

    return args
