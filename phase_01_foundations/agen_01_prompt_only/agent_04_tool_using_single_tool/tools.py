from datetime import datetime

def get_current_time():
    """Return current time as string"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")