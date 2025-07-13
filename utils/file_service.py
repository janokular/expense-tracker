import os


def validate_file(csv_file):
    '''Check if expenses.csv exisits else create it'''
    if not os.path.exists(csv_file):
        with open (csv_file, 'w') as file:
            pass
