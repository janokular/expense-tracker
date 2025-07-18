import csv
from utils.args_validator import is_id_in_range


def delete_expense(id: int, file):
    '''Delete expense'''
    expenses = []
    
    if is_id_in_range(id, file):
        with open(file, 'r', newline='') as csv_expenses:
            for expense in csv.reader(csv_expenses):
                if id != int(expense[0]):
                    expenses.append(expense)

        # Adjust IDs
        for expense in expenses[id - 1:]:
            expense[0] = int(expense[0]) - 1

        with open(file, 'w', newline='') as csv_expenses:
            csv.writer(csv_expenses).writerows(expenses)

        print(f'Expense (ID: {id}) deleted successfully')
