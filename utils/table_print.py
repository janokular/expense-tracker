def print_table(expenses: list):
    '''Print expenses inside a table'''
    expenses.insert(0, ['ID', 'Date', 'Description', 'Amount'])

    id_col_len = 0
    date_col_len = 0
    description_col_len = 0
    amount_col_len = 0

    for expense in expenses:
        if id_col_len < len(expense[0]):
            id_col_len = len(expense[0])
        
        if date_col_len < len(expense[1]):
            date_col_len = len(expense[1])

        if description_col_len < len(expense[2]):
            description_col_len = len(expense[2])
        
        if amount_col_len < len(expense[3]):
            amount_col_len = len(expense[3])

    for expense in expenses:
        print(expense[0] + ' ' * (id_col_len - len(expense[0])),
              expense[1] + ' ' * (date_col_len - len(expense[1])),
              expense[2] + ' ' * (description_col_len - len(expense[2])),
              expense[3] + ' ' * (amount_col_len - len(expense[3])))
