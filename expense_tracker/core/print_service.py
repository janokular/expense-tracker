def column(expenses: list):
    '''Columnate expenses list'''
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

    for expense in expenses:
        if id_spacing < len(expense[0]):
            id_spacing = len(expense[0])
        if date_spacing < len(expense[1]):
            date_spacing = len(expense[1])
        if desc_spacing < len(expense[2]):
            desc_spacing = len(expense[2])
        if amount_spacing < len(expense[3]):
            amount_spacing = len(expense[3])

    for expense in expenses:
        print(
            f'{expense[0]} {' ' * (id_spacing - len(expense[0]))}',
            f'{expense[1]} {' ' * (date_spacing - len(expense[1]))}',
            f'{expense[2]} {' ' * (desc_spacing - len(expense[2]))}',
            f'{expense[3]} {' ' * (amount_spacing - len(expense[3]))}'
        )
