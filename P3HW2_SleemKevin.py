# Kevin Sleem
# July 4, 2024
# P3HW2
# Employee Pay Calculations

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
payrate = float(input("Enter employee's pay rate: "))
print("------------------------------")
print("Employee name:", employee_name)
print('\n')
print("Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay")
print('-----------------------------------------------------------------------')
overtime = hours_worked - 40
regular_hours = hours_worked - overtime

if hours_worked <= 40:
    overtime = 0.0

overtime_pay = overtime * payrate * 1.5
regular_pay = regular_hours * payrate
gross_pay = regular_pay + overtime_pay

payrate = (f'{payrate:.2f}')
overtime = (f'{overtime:.2f}')
overtime_pay = (f'{overtime_pay:.2f}')
regular_pay = (f'{regular_pay:.2f}')
gross_pay = (f'{gross_pay:.2f}')

print(f'{hours_worked:.2f} {payrate:>13} {overtime:>8} {overtime_pay:>10} {regular_pay:>14} {gross_pay:>12}')
