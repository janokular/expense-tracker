import datetime


def get_today_date() -> str:
    '''Return current date in dd-mm-yyyy format'''
    return datetime.date.today().strftime('%d-%m-%Y')


def get_month_name(date: str) -> str:
    '''Return full month name from dd-mm-yyyy date format'''
    return datetime.datetime.strptime(date, '%d-%m-%Y').strftime('%B')
