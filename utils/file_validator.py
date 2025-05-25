import os
import csv


def validate_file(csv_file):
    '''Check if expenses.csv exisits'''
    if not os.path.exists(csv_file):
        pass