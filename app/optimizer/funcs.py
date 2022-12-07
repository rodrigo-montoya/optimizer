from math import ceil
from datetime import datetime, timedelta, date

def date_to_week(date, format='%Y-%m-%d', custom_start=f'{date.today().year}-01-01'):
    the_date = datetime.strptime(date, format)
    start_date = datetime.strptime(custom_start, format)
    return ceil((the_date - start_date).days / 7)

def week_to_date(week, format='%Y-%m-%d', custom_start=f'{date.today().year}-01-01'):
    start_date = datetime.strptime(custom_start, format)
    return (start_date + timedelta(days=week*7)).strftime(format)

def num_to_week(num):
    return (num // 7) + 1