import csv
from enums.MonthsEnum import MonthsEnum


def add(description, amount, file):
    print(description)
    print(amount)


def update(id, description, amount, file):
    print(id)
    print(description)
    print(amount)


def list(file):
    pass


def delete(id, file):
    print(id)


def summary(month, file):
    print(f'Total expenses for {MonthsEnum(month).name}:')
