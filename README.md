## Expense tracker
```
# Initial setup
# Create and activate virtual environment
python3 -m venv .venv
. ./.venv/bin/activate

# Installation
pip3 install .

# Exit the virtual enviroment
deactivate

# Uninstallation
pip3 uninstall expense_tracker
```
```
# Add new expense
expense_tracker add --description "Lunch" --amount 20

# List expenses
expense_tracker list

# Update expense's description
expense_tracker update --id 1 --description "Dinner"

# Update expense's amount
expense_tracker update --id 1 --amount 15.5

# Update expense's description and amount
expense_tracker update --id 1 --description "Groceries" --amount 34.75

# Delete expense
expense_tracker delete --id 1

# Summary of all expenses
expense_tracker summary

# Summary of expenses for July
expense_tracker summary --month 7
```
