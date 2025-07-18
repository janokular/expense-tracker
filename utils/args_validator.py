import csv


def is_id_in_range(id: int, file):
    '''Check if expense id is in range'''
    with open(file, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            if id == int(expense[0]):
                return True
        
        print(f'Error: (ID: {id}) is out of range')
        return False


def is_description_not_empty(description: str):
    '''Check if description is not empty'''
    if description == '':
        print('Error: Description cannot be empty')
        return False
    else:
        return True


def is_amount_valid(amount: float):
    '''Check if amount is positive and has only two decimal points'''
    number_of_decimal_points = len(str(amount).split('.')[1])

    if amount < 0 or number_of_decimal_points > 2:
        print('Error: Amount must be positive and can only have two decimal points')
        return False
    else:
        return True