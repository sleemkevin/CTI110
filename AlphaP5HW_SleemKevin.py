#Kevin Sleem
#July 18, 2024
#P5HW
#Math Quiz

print('Welcome to Math Quiz')
print('\n')
import random
global selection

def introduction():
    print('\n')
    print('MAIN MENU')
    print('----------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    global selection
    selection = input('Please choose one of the menu options: ')
introduction()

def program():
    while True:
        number1 = int(random.uniform(0,1000))
        number2 = int(random.uniform(0,1000))
        guesses = 0
        if selection == '1':
            sum1= number1 + number2
            print(number1)
            print('+', number2)
            answer1 = int(input('Enter answer.'))
            while True:
                if answer1 < sum1:
                    print('Sorry, guess is too low.')
                    guesses += 1
                    answer1 = int(input('Try again: '))
                elif answer1 > sum1:
                    print('Sorry, guess is too high')
                    guesses += 1
                    answer1 = int(input('Try again: '))
                elif answer1 == sum1:
                    print('Congratulations!!!! Your answer is correct.')
                    guesses += 1
                    print('Number of guesses: ', guesses)
                    introduction()
                    break
            
        elif selection == '2':
            sum2 = number1 - number2
            print(number1)
            print('-', number2)
            answer2 = int(input('Enter answer. '))
            while True:
                if answer2 < sum2:
                    print('Sorry, guess is too low.')
                    guesses += 1
                    answer2 = int(input('Try again: '))
                elif answer2 > sum2:
                    print('Sorry, guess is too high')
                    guesses += 1
                    answer2 = int(input('Try again: '))
                elif answer2 == sum2:
                    print('Congratulations!!!! Your answer is correct.')
                    guesses += 1
                    print('Number of guesses: ', guesses)
                    introduction()
                    break

        elif selection == '3':
            print('Thank you for playing...')
            print('Bye!!')
            break
program()
