import re


def validate_phone_number(phone_number: str) -> bool:
    pattern = '^\\+[1-9]{1}[0-9]{7,14}$'
    return re.match(pattern, phone_number) is not None


def validate_email(email: str) -> bool:
    pattern = '^([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+\\.[A-Za-z]{2,}$'
    return re.match(pattern, email) is not None
