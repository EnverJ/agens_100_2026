from datetime import datetime

def get_current_time():
    """return current time as string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_date():
    """get current date as a string"""
    return datetime.now().strftime("%Y-%m-%d")

def get_sum(a,b):
    return (a + b)