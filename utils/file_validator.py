import os
import csv


def validate_file(csv_file):
    '''Check if expenses.csv exisits'''
    if not os.path.exists(csv_file):
       # Create an epmty CSV file
        with open (csv_file, 'w') as file:
            pass