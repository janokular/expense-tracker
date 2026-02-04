def column_print(expenses: list):
    '''Columnate expenses lists'''
    HEADER = [
        'ID',
        'DATE',
        'DESCRIPTION',
        'AMOUNT'
    ]
    expenses.insert(0, HEADER)

    id_col_len = 0
    date_col_len = 0
    description_col_len = 0
    amount_col_len = 0

    for e in expenses:
        if id_col_len < len(e[0]):
            id_col_len = len(e[0])
        
        if date_col_len < len(e[1]):
            date_col_len = len(e[1])

        if description_col_len < len(e[2]):
            description_col_len = len(e[2])
        
        if amount_col_len < len(e[3]):
            amount_col_len = len(e[3])

    for e in expenses:
        print(
            f'{e[0]} {' ' * (id_col_len - len(e[0]))}',
            f'{e[1]} {' ' * (date_col_len - len(e[1]))}',
            f'{e[2]} {' ' * (description_col_len - len(e[2]))}',
            f'{e[3]} {' ' * (amount_col_len - len(e[3]))}'
        )
