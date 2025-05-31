import argparse


def parse_arguments():
    '''Parse arguments needed for program logic'''
    parser = argparse.ArgumentParser(description='Program used to track and manage your expenses')

    subparsers = parser.add_subparsers(dest='action')

    add_parser = subparsers.add_parser('add', help='add an expense with a description and amount')
    add_parser.add_argument('--description', required=True)
    add_parser.add_argument('--amount', required=True, type=float)

    update_parser = subparsers.add_parser('update', help='update an expense')
    update_parser.add_argument('--id', required=True, type=int)
    update_parser.add_argument('--description')
    update_parser.add_argument('--amount', type=float)

    subparsers.add_parser('list', help='view all expenses')

    delete_parser = subparsers.add_parser('delete', help='delete an expense')
    delete_parser.add_argument('--id', required=True, type=int)

    summary_parser = subparsers.add_parser('summary', help='view a summary of all expenses')
    summary_parser.add_argument('--month', type=int, choices=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], help='view a summary of expenses for a specific month')

    args =  parser.parse_args()

    if not bool(args.action):
        parser.error('No arguments provided')

    return args
