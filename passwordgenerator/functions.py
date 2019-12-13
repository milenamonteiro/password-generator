'''Modules'''
import string
import random

def new_default(size=12, chars=string.ascii_uppercase +
                string.ascii_lowercase + string.digits):
    '''
    If the user wants a default password this method is called.
    Returning a 12 size password with letters and numbers'''
    return ''.join(random.choice(chars) for _ in range(size))
