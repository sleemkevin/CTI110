#Kevin Sleem
#June 29, 2024
#P3LAB
#Change Calculator


amount = float(input('Enter the amount of money as a float: $'))
amount = int(amount*100)
dollars = int(amount//100)

if dollars == 1:
    print(dollars, 'Dollar')
elif dollars > 1:
    print(dollars, 'Dollars')

amount = amount%100
quarters = int(amount//25)

if quarters == 1:
    print(quarters, 'Quarter')
elif quarters > 1:
    print(quarters, 'Quarters')

amount = amount%25
dimes = int(amount//10)

if dimes == 1:
    print(dimes, 'Dime')
elif dimes > 1:
    print(dimes, 'Dimes')

amount = amount%10    
nickels = int(amount//5)

if nickels == 1:
    print(nickels, 'Nickel')
elif nickels > 1:
    print(nickels, 'Nickels')

amount = amount%5
pennies = int(amount//1)

if pennies == 1:
    print(pennies, 'Penny')
elif pennies > 1:
    print(pennies, 'Pennies')
