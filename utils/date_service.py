import datetime


def get_current_date():
    return datetime.date.today()


def get_month_from_date(date_string):
    '''Return full month name string from yyyy-mm-dd string'''
    return datetime.datetime.strptime(date_string, "%Y-%m-%d").strftime('%B')
