import csv


RED = '\033[31m'
RESET = '\033[0m'


def id_validator(id: int, filepath: str) -> bool:
    '''Validate if id is in range'''
    with open(filepath, 'r', newline='') as csv_expenses:
        for expense in csv.reader(csv_expenses):
            if id == int(expense[0]):
                return True
        
        print(f'{RED}error: (ID: {id}) is out of range{RESET}')
        return False


def description_validator(description: str) -> bool:
    '''Check if description is not empty'''
    if description == '':
        print(f'{RED}error: Description cannot be empty{RESET}')
        return False
    else:
        return True


def amount_validator(amount: float) -> bool:
    '''Check if amount is positive and has only two decimal points'''
    if amount > 0:
        precision = len(str(amount).split('.')[1])
        if precision > 2:
            print(f'{RED}error: Amount can only have two decimal points{RESET}')
            return False
        else:
            return True
    else:
        print(f'{RED}error: Amount must be positive{RESET}')
        return False


def add_args_validator(description: str, amount: str) -> bool:
    '''Validate required add args: description and amount'''
    return (
        description_validator(description)
        and amount_validator(amount)
    )


def update_args_validator(description: str = None, amount: float = None) -> bool:
    '''Validate optional update args: description and amount'''
    if description is not None and not description_validator(description):
        return False
    
    if amount is not None and not amount_validator(amount):
        return False
    
    if description is not None and amount is not None:
        if not description_validator(description) and not amount_validator(amount):
            return False
    
    return True
