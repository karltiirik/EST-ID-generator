__author__ = 'Karl Tiirik'
from random import randint, randrange
import datetime


def gen_est_id():
    """
    Generates a valid Estonian identification number, algorithm http://et.wikipedia.org/wiki/Isikukood
    :return: Estonian ID in string format
    """
    id = ""

    # random birth date between 1800.01.01 and today
    start_date = datetime.date(1800, 1, 1)
    end_date = datetime.date.today()
    b_date = rand_birth_date(start_date, end_date)

    # gender and century digit
    gender = randint(0, 1)
    century_digit = get_century_digit(b_date)[gender]
    id += century_digit

    # birth date
    id += format_date(b_date)

    # nth baby that day
    id += rand_int(0, 999)

    # calculate checksum
    id += calc_checksum(id)

    return id


def rand_birth_date(start_date, end_date):
    """
    Returns a random date between start_date and end_date
    :param start_date: datetime.date format
    :param end_date: datetime.date format
    :return: datetime.date format
    """
    delta = end_date - start_date
    r_days = randrange(delta.days + 1)
    r_date = start_date + datetime.timedelta(days=r_days)
    return r_date


def get_century_digit(date):
    """
    Returns possible values for century digit
    :param date: datetime.date format
    :return: list with corresponding century digits for date [MALE, FEMALE]
    """
    year = date.year
    if 1800 <= year <= 1899:
        return ['1', '2']
    elif 1900 <= year <= 1999:
        return ['3', '4']
    elif 2000 <= year <= 2099:
        return ['5', '6']
    """
    # For the future
    elif 2100 <= year <= 2199:
        return ['7', '8']
    """

def format_date(date):
    """
    Format date
    :param date: datetime.date format
    :return: formatted date string 'YYMMDD'
    """
    f_date = str(date.year)[2:] + str(date.month).zfill(2) + str(date.day).zfill(2)
    return f_date


def rand_int(mn, mx):
    """
    Generates a random int between mn and mx and and pads it with "0"-s
    :param mn: min number(inc), integer format
    :param mx: max number(inc) integer format
    :return: random number between mn and mx padded with 0-s, string format
    """
    r_int = str(randint(mn, mx)).zfill(len(str(mx)))
    return r_int


def calc_checksum(number):
    """
    Calculates checksum using Modulo 11 and weights
    :param number: 10 digits, in string format
    :return: checksum, string format
    """
    LVL_1_WEIGHTS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    LVL_2_WEIGHTS = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    cs = 0

    remainder = modulo_11(number, LVL_1_WEIGHTS)
    if remainder != 10:
        cs = remainder
    else:
        remainder = modulo_11(number, LVL_2_WEIGHTS)
        if remainder != 10:
            cs = remainder

    return str(cs)


def modulo_11(number, weights):
    """
    Modulo 11 method with weights
    :param number: in string format
    :param weights: list of integers
    :return: integer
    """
    sum = 0

    for i in range(len(number)):
        sum += int(number[i]) * weights[i]

    return sum % 11


print(gen_est_id())
