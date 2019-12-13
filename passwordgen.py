'''Module to pick a random item'''
import random

CHARS = "abcdefghijklmnopqrstuvwxyz1234567890"

LENGHT = input('What will be the lenght of the password? ')
LENGHT = int(LENGHT)

PASSWORD = ''

for c in range(LENGHT):
    PASSWORD += random.choice(CHARS)

print(PASSWORD)
