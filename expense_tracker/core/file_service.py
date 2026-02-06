import os


FILEPATH = 'expenses.csv'


def get_filepath() -> str:
    '''Get expenses.csv filepath'''
    filepath_validator(FILEPATH)            
    return FILEPATH


def filepath_validator(filepath: str):
    '''Create CSV file if filepath does not exist'''
    if not os.path.exists(filepath):
        with open (filepath, 'w') as file:
            pass
