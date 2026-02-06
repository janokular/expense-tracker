from argparse import ArgumentParser

from .commands import add
from .commands import delete
from .commands import list
from .commands import summary
from .commands import update


def build_parser() -> ArgumentParser:
    parser = ArgumentParser(
        prog='expense_tracker',
        description='Expense Tracker - track and manage your expenses'
    )
    subparsers = parser.add_subparsers(
        dest='command'
    )

    add.register(subparsers)
    delete.register(subparsers)
    list.register(subparsers)
    summary.register(subparsers)
    update.register(subparsers)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
