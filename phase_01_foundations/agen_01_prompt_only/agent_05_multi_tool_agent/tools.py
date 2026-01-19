from datetime import datetime

def get_current_time():
    """Return current time as string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_current_date():
    """Return current date as string"""
    return datetime.now().strftime("%Y-%m-%d")

def get_sum(a, b):
    """Sum two numbers"""
    return a + b