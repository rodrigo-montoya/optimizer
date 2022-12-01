from math import ceil
from datetime import datetime, timedelta

def date_to_week(date, format='%d/%m/%Y', custom_start='01/01/2022'):
    the_date = datetime.strptime(date, format)
    start_date = datetime.strptime(custom_start, format)
    return (the_date - start_date).days // 7

def week_to_date(week, format='%d/%m/%Y', custom_start='01/01/2022'):
    start_date = datetime.strptime(custom_start, format)
    return (start_date + timedelta(days=week*7)).strftime(format)

def num_to_week(num):
    return ceil(num/7)