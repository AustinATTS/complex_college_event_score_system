import re

def validate_email(email):
    regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.match(regex, email) is not None

def validate_phone(phone):
    regex = r'^\+?1?\d{9,15}$'
    return re.match(regex, phone) is not None
