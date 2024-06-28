#Kevin Sleem
#June 28, 2024
#P2LAB2
#This program creates a car dictionary



cars = {
    'Camaro': 18.21,
    'Prius': 52.36,
    'Model S': 110,
    'Silverado': 26
}

keys = cars.keys()
values = cars.values()
print(keys)
print('\n')
x = str(input("Enter a vehicle to see it's mpg: "))
print('\n')
if x in cars:
    print(f'The', x, 'gets', cars[x], 'mpg.')
print('\n')

print('How many miles will you drive the', x + '?', end=' ')
y =float(input())
z = y / cars[x]
print('\n')
print(f'{z:.3f}', 'gallons(s)of gas are needed to drive the', x, y, 'miles.')  



