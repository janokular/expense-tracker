import os


def get_file():
    '''Return expenses.csv file'''
    FILE = 'expenses.csv'

    if not os.path.exists(FILE):
        with open (FILE, 'w') as file:
            pass
            
    return FILE
