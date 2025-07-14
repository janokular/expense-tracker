import csv


def is_id_in_range(id, file):
    '''Check if expense id is in range'''
    with open(file, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            if id == int(expense[0]):
                return True
            
        print(f'ID: {id} is out of range')
        return False
