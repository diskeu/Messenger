from datetime import date, datetime

def format_value(value):
    """Formats value to correspond the sql syntax"""
    # if isinstance(value, (datetime, date, str)): return f"{value}" could possible add extra querys
    if type(value) == bool: return value
    if value == -1: return "DEFAULT"
    elif value == None: return None
    return str(value)