def column_print(expenses: list):
    '''Columnate expenses lists'''
    HEADER = [
        'ID',
        'DATE',
        'DESCRIPTION',
        'AMOUNT'
    ]
    expenses.insert(0, HEADER)

    id_spacing = 0
    date_spacing = 0
    desc_spacing = 0
    amount_spacing = 0

    for e in expenses:
        if id_spacing < len(e[0]):
            id_spacing = len(e[0])
        
        if date_spacing < len(e[1]):
            date_spacing = len(e[1])

        if desc_spacing < len(e[2]):
            desc_spacing = len(e[2])
        
        if amount_spacing < len(e[3]):
            amount_spacing = len(e[3])

    for e in expenses:
        print(
            f'{e[0]} {' ' * (id_spacing - len(e[0]))}',
            f'{e[1]} {' ' * (date_spacing - len(e[1]))}',
            f'{e[2]} {' ' * (desc_spacing - len(e[2]))}',
            f'{e[3]} {' ' * (amount_spacing - len(e[3]))}'
        )
