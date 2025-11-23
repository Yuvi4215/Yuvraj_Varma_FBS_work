import re


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))



print(is_valid_email("yuvraj.varma@sample.com"))
print(is_valid_email("invalid-email@.com"))
print(is_valid_email("email@invalid_mail.com"))