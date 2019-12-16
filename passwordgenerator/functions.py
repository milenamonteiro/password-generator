'''Modules'''
import secrets
import string

def new_default(size=12, chars=string.ascii_uppercase +
                string.ascii_lowercase + string.digits):
    '''
    If the user wants a default password this method is called.
    Returning a 12 size password with letters and numbers'''
    return ''.join(secrets.choice(chars) for _ in range(size))

def create_password(size, chars):
    '''Generates a password with the characters given'''
    return ''.join(secrets.choice(chars) for _ in range(size))

def redirect_choice(size, symbols, lower, upper, numbers):
    '''Sending the chars to a function'''
    chars = ''
    if symbols:
        chars += "!@#$%&*^"
    if lower:
        chars += string.ascii_lowercase
    if upper:
        chars += string.ascii_uppercase
    if numbers:
        chars += string.digits
    if chars == '':
        return new_default()

    return create_password(size, chars)
