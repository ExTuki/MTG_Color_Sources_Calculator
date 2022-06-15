import sys
print('This program tells you, how many mana sources of each color you need in your (60 card) deck.')
print('Use this for only one colour of your choice; you can do this for each color separately.')
print('Consider delve and convoke cards to be the mana value you typically cast them for.')
print('This tells you how many untapped mana sources you have, consider lowering tapped mana sources, or adding untapped ones.')




while True:
    q1 = input('Does your deck contain a CCC card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 23 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 1CCC card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 20 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a CC card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 20 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 2CCC card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 18 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 1CC card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 18 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 3CCC card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 16 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 2CC card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 16 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 3CC card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 14 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a C card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 14 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 4CC card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 13 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 1C card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 13 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 2C card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 11 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 3C card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 10 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 4C card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 9 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    q1 = input('Does your deck contain a 5C card? (y/n)')
    if q1 == 'y':
        print('Your deck needs 8 untapped mana sources of the chosen color.')
    elif q1 == 'n':
        break
    else:
        print('Please repeat.')

while True:
    finish = input('Your deck needs probably less than 8 mana sources of the chosen color. Do you want to exit (y/n)')
    if finish == 'y':
        sys.exit()
    elif finish == 'n':
        print('Ok then...')
    else:
        print('Please repeat')
