#Kevin Sleem
#July 10, 2024
#P4LAB2
#Number Mulitplier


integer = int(input('Enter an integer: '))

while True:
    if integer >= 0:
        for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            print(f'{integer} * {number} = {integer * number}')

    else:
        print('This program does not handle negative numbers.')

    answer = input('Would you like to run the program again? ')
    if answer in ['yes', 'YES', 'Yes']:
        integer = int(input('Enter an integer: '))
    else:
        print('Exiting program...')
        break

