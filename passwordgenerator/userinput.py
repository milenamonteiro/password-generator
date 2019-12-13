'''Import to get the functions from the other file'''
import functions as password

def yes_no(text):
    '''Is called for every Y/N input with the print text.
    Verifies if the input is Yes or No'''
    yes = set(['yes', 'y', 'ye', ''])
    _no = set(['no', 'n'])
    while True:
        choice = input(text).lower()
        # prints the text and attributes the input to choice
        if choice in yes:
            return True
        if choice in _no:
            return False
        print("Please answer with 'Yes' or 'No'")

while True:
    try:
        LENGHT = int(input('What will be the lenght of the password? '))
    except ValueError:
        print("Please enter an integer number")
        continue
    if isinstance(LENGHT, int):
        # if the input value is integer the looping stops
        break

# all variables are booleans
SYMBOLS = yes_no('Do you want symbols in it? [Y]Yes [N]No ')
NUMBERS = yes_no('Do you want numbers in it? [Y]Yes [N]No ')
LOWER = yes_no('Do you want lower case characters in the password? [Y]Yes [N]No ')
UPPER = yes_no('Do you want upper case characters in the password? [Y]Yes [N]No ')

# just testing the function
print(password.new_default())
