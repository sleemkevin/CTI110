#Kevin Sleem
#June 20, 2024
#P1HW2
#This lab includes input and print functions to create a travel itinerary and
#budget

print('This program calculates and displays travel expenses')
print('\n')

budget = int(input('Enter Budget: '))
travel_destination = input('Enter your travel destination: ')
gas = int(input('How much do you think you will spend on gas? '))
hotel = int(input('Approximately how much will you need for accomodation/hotel? '))
food = int(input('Last, how much do you need for food? '))

print('\n')
print('--------Travel Expenses--------')
width = 10
print('Location:', (f'{travel_destination:>21}'))
a_budget = '${:.2f}'.format(budget)
print('Initial Budget:', (f'{a_budget:>13}'))
print('\n')
a_gas = '${:.2f}'.format(gas)
print('Fuel:', (f'{a_gas:>22}'))
a_hotel = '${:.2f}'.format(hotel)
print('Accomodation:', (f'{a_hotel:>14}'))
a_food = '${:.2f}'.format(food)
print('Food:', f'{a_food:>22}')
print('\n')
calculation = budget - gas - hotel - food
a_calculation = '${:.2f}'.format(calculation)
print('Remaining Balance:', (f'{a_calculation:>9}'))
