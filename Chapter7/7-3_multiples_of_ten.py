'''
7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not .
'''

number = int(input('\nEnter your number: '))

if number % 10 == 0:
    print('Your number is multiple of Ten.')
else:
    print('Your number is not multiple of Ten.')