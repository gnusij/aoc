from datetime import date

from .models import default_user
from .models import Puzzle


def get_today():
    return date.today().year, date.today().day

def get_puzzle(year, day, session=None):
    return Puzzle(year=year, day=day, session=session)

def get_puzzle_today():
    return get_puzzle(*get_today())

def get_data(year, day, session=None):
    return get_puzzle(year=year, day=day, session=session).input

def get_ex(year, day, session=None):
    return get_puzzle(year=year, day=day, session=session).example

def get_data_today():
    return get_puzzle_today().input

def get_ex_today():
    return get_puzzle_today().example

