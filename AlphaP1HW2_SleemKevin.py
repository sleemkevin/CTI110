#Kevin Sleem
#June 18, 2024
#P1HW2
#This lab includes input and print functions to create math functions

print ('Enter Budget:', end=' ')
budget= int(input())
print ('Enter your travel destination:', end=' ')
travel_destination= (input())
print ('How much do you think you will spend on gas?', end=' ')
gas= int(input())
print ('Approximately how much will you need for accomodation/hotel?', end=' ')
hotel= int(input())
print ('Last, how much do you need for food?', end=' ')
food= int(input())

print('\n')
print('----------Travel Expenses----------')
print('Location:', travel_destination)
print('Initial Budget:', budget)
print('\n')
print('Fuel:', gas)
print('Accomodation:', hotel)
print('Food:', food)
print('\n')
print('Remaining Balance:', budget - gas - hotel - food)
