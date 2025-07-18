import datetime


def get_current_date():
    '''Return current date in yyyy-mm-dd format'''
    return datetime.date.today()


def get_month_name(date: str):
    '''Return full month name from yyyy-mm-dd date format'''
    return datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%B')
