from datetime import timedelta

GIGASECOND = 10**9

def add_gigasecond(date):
    return date + timedelta(seconds=GIGASECOND)