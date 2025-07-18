import csv
from enums.MonthsEnum import MonthsEnum
from utils.date_service import get_month_name


def summary_of_expenses(month: int, file):
    '''Summary of total or specific month expenses'''
    total = 0.0
    month_name = MonthsEnum(month).name if month else None

    with open(file, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            date = expense[1]
            amount = float(expense[3])
            if not month or get_month_name(date) == month_name:
                total += amount

    print(f'Total expenses for {month_name}: ${total}' if month else 
          f'Total expenses: ${total}')
