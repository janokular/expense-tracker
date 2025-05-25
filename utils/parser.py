import argparse


def parse_arguments():
    '''Parse arguments needed for program logic'''
    parser = argparse.ArgumentParser(description='Program used to track and manage your expenses')

    subparsers = parser.add_subparsers(dest='action')

    add_parser = subparsers.add_parser('add', help='Add an expense with a description and amount')

    update_parser = subparsers.add_parser('update', help='Update an expense')

    list_parser = subparsers.add_parser('list', help='View all expenses')

    delete_parser = subparsers.add_parser('delete', help='Delete an expense')

    summary_parser = subparsers.add_parser('summary', help='View a summary of all expenses')

    return parser.parse_args()
