#Kevin Sleem
#July 2, 2024
#P5LAB
#Change Calculator, Enter a money float value with 2 places after the decimal
#that determines change


def total():
    import random
    global change
    number = round(random.uniform(0.01, 100.00), 2)
    print(f'You owe ${number}')
    cash = float(input('How much cash will you put in the self-checkout? '))
    change = cash - number
    print(f'Change is : ${change:.2f}')
    print('\n')
total()
    
def disperse_change():
    #Convert change from a float to an integer
    global change
    change = int(change*100)

    if change == 0:
        print('No change')

    #Calculate the amount of each coin needed 
    num_dollars = change//100
    change = change - (num_dollars * 100)

    num_quarters = change//25
    change = change - (num_quarters * 25)

    num_dimes = change//10
    change = change - (num_dimes * 10)

    num_nickels = change//5
    change = change - (num_nickels * 5)

    num_pennies = change//1

    if num_dollars > 0:
        print(num_dollars, end=' ')
        if num_dollars == 1:
            print('Dollar')
        else:
            print('Dollars')

    if num_quarters > 0:
        print(num_quarters, end=' ')        
        if num_quarters == 1:
            print('Quarter')
        else:
            print('Quarters')

    if num_dimes > 0:
        print(num_dimes, end=' ')
        if num_dimes == 1:
            print('Dime')
        else:
            print('Dimes')

    if num_nickels > 0:
        print(num_nickels, end=' ')
        if num_nickels == 1:
            print('Nickel')
        else:
            print('Nickels')

    if num_pennies > 0:
        print(num_pennies, end=' ')
        if num_pennies == 1:
            print('Penny')
        else:
            print('Pennies')

disperse_change()

