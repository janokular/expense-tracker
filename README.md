## Expense tracker
```
# Add new expense
expense_tracker.py add --description "Lunch" --amount 20

# List expenses
expense_tracker.py list

# Update expense's description
expense_tracker.py update --id 1 --description "Dinner"

# Update expense's amount
expense_tracker.py update --id 1 --amount 15.5

# Update expense's description and amount
expense_tracker.py update --id 1 --description "Groceries" --amount 34.75

# Delete expense
expense_tracker.py delete --id 1

# Summary of all expenses
expense_tracker.py summary

# Summary of expenses for July
expense_tracker.py summary --month 7
```
