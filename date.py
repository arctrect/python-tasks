from dateutil.parser import parse
import datetime

def is_valid_date(date_string, format='%d-%m-%Y'):
    try:
        date_obj = parse(date_string, dayfirst=True)
        return date_obj.strftime(format) == date_string
    except ValueError:
        return False

def today():
    today = datetime.datetime.today()
    return today.strftime('%d-%m-%Y')

def tomorrow():
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(days=1)
    return tomorrow.strftime('%d-%m-%Y')