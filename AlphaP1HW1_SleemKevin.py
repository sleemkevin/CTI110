#Kevin Sleem
#June 18, 2024
#P1HW1
#This lab includes input and print functions to create math functions

print('----Calculating Exponents----\n')
print('\n')

print ('Enter an integer as the base value:', end=' ')
base_value= int(input())
print ('Enter an integer as the exponent:', end= ' ')
exponent= int(input())
print('\n')
print('\n')

first_calculation= base_value**exponent
print (base_value, 'raised to the power of', exponent, 'is', first_calculation)
print('\n')
print('\n')      

print('----Addition and Subtraction----')
print('\n')
print('\n')

print ('Enter a starting integer:',end=' ')
starting_integer= int(input())
print ('Enter an integer to add:', end=' ')
add_integer= int(input())
print ('Enter an integer to subtract:', end=' ')
subtract_integer= int(input())
print('\n')
print('\n')

second_calculation= starting_integer + add_integer - subtract_integer
print (starting_integer, '+', add_integer, '-', subtract_integer, 'is equal to', second_calculation)


