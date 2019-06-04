from datetime import datetime, timedelta
from time import mktime
from dateutil.relativedelta import relativedelta
import calendar

def diff_month(d1, d2):
    """
    get the difference in months between two datetimes
    :param d1: first datetime
    :param d2: second datetime
    :return: the number of months
    """
    return (d1.year - d2.year)*12 + d1.month - d2.month

def dt_local_to_dt_timezone(date_local, tz_local, tz_new):
    """
    translates from datetime in local timezone to timestamp in a new tz
    :param date_local: naive or local datetime
    :param tz_local: timezone of "date_local"
    :param tz_new: the new timezone to change "date_local"
    :return: returns the same datetime to tz_new
    """
    date_utc=pytz.timezone(tz_local).localize(date_local).astimezone(tz_new)
    return date_utc


def get_n_months(date, num_months):
    """
    returns a list with the "num_months" dates from "date"
    :param date: a datetime to get the dates from
    :param num_months: the number of months to get,  0 means this month, positive future month, negative previous month
    :return: a list containing "num_month" the datetimes
    """
    if num_months >0:
        initial=1
        final = num_months+1
    elif num_months < 0:
        initial=num_months
        final = 0
    else:
        initial = 0
        final = 0
    return [date_n_month(date, x) for x in range(initial,final)]

def day_before(date):
    """
    calculates the last complete day a given datetime object
    :param date: input datetime
    :return: the previous complete day EX: datetime(2014,6,22,23,59,59)
    """
    return datetime(date.year, date.month, date.day, 0, 0, 0) - timedelta(seconds=1)


def date_n_month(date, n_month):
    """
    returns the same date with "n_month" offset
    :param date: the date
    :param n_month: the number of month, 0 means this month, positive future month, negative previous month
    :return: the same date minus the "n_month_back" month
    """
    month = date.month + n_month
    year = int(date.year + month / 12)
    month = (month % 12) if (month % 12) != 0 else 12
    day = min(date.day, calendar.monthrange(year, month)[1])
    hour = date.hour
    minute = date.minute
    second = date.second
    ts_previous = datetime(year, month, day, hour, minute, second)
    return ts_previous


def first_day_n_month(date, n=0):
    """
    get the first day of the n th month from a datetime object
    :param date:  the datetime object
    :param n: the n th month, 0 means this month, positive future month, negative previous month
    :return: the first day of the datetime object's month
    """
    date = date_n_month(date, n)
    return datetime(date.year, date.month, 1, 0, 0, 0)


def last_day_n_month(date, n=0):
    """
    calculates the last day of the n th month from a datetime object
    :param date: the datetime
    :param n: the n th month, 0 means this month, positive future month, negative previous month
    :return: the datetime of the complete last day of the month, EX:datetime(2014,6,30,23,59,59)
    """
    date = date_n_month(date, n)
    return datetime(date.year, ((date.month) % 12) +1, 1, 0, 0, 0) - relativedelta(seconds=1)


def first_day_n_years(date, n=0):
    """
    geet the first day of the n th  previous year from a datetime object
    :param date: the datetime object
    :param n: the n th year, 0 means this year, positive future years, negative previous years
    :return:  a datetime of the first day of the current year
    """
    return datetime(date.year + n, 1, 1, 0, 0, 0)
