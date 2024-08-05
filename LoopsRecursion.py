numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print (squared_numbers)

sequence = range(10)
new_list = []
for x in sequence:
    if x % 2 == 0:
        new_list.append(x)

sequence = range(10)
new_list = [x for x in sequence if x % 2 == 0]

index = 0
while index < len(greeting):
print (greeting[index:index+1])
Index += 1

H E L L O

greeting = ‘Hello’
for i in range(len(greeting)):
print i

0 1 2 3 4 

for char in greeting:
print(char)

H E L L O

index = 0
while index < len(greeting):
print (greeting[index])
Index += 1

H E L L O

def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line
print(format_phone("2025551212")) # Outputs: (202) 555-1212
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)
greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli'])

def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result
factorial(4)

def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
    
def is_power_of(number, base):
 # Base case: when number is smaller than base.
    number = number/base 
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return False
    else:
        return True
    # Recursive case: keep dividing number by base.
    return is_power_of(number, base)
print(is_power_of(8,2))     # Should be True
print(is_power_of(64,4))    # Should be True
print(is_power_of(70,10))   # Should be False

def sequence(low, high):
    # Complete the outer loop range to make the loop run twice
    # to create two rows
    for x in range(2): 
        # Complete the inner loop range to print the given variable
        # numbers starting from "high" to "low" 
        # Hint: To decrement a range parameter, use negative numbers
        for y in range(high, low-1, -1): 
            if y == low:
                # Don’t print a comma after the last item
                print(str(y)) 
            else:
                # Print a comma and a space between numbers
                print(str(y), end=", ") 
sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.

def digits(n):
    count = 0
    if n == 0:
      count += 1
    while (n>0): # Complete the while loop condition
        # Complete the body of the while loop. This should include 
        # performing a calculation and incrementing a variable in the
        # appropriate order.  
          count += 1
          n = n // 10
    return count
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

def countdown(start):
    x = start
    if x > 0:
        return_string = "Counting down to 0: "
        while x >= 0: # Complete the while loop
            return_string += str(x) # Add the numbers to the "return_string"
            if x > 0:
                return_string += ","
            x -= 1 # Decrement the appropriate variable
    else:
        return_string = "Cannot count down to 0"
    return return_string
print(countdown(10)) # Should be "Counting down to 0: 10,9,8,7,6,5,4,3,2,1,0"
print(countdown(2)) # Should be "Counting down to 0: 2,1,0"
print(countdown(0)) # Should be "Cannot count down to 0"

def even_numbers(maximum):
    return_string = "" # Initializes variable as a string
    # Complete the for loop with a range that includes all even numbers
    # up to and including the "maximum" value, but excluding 0.
    for x in range(2, maximum + 1, 2): 
        # Complete the body of the loop by appending the even number
        # followed by a space to the "return_string" variable.
        return_string += str(x) + " "  
    # This .strip command will remove the final " " space at the end of
    # the "return_string".
    return return_string.strip() 
print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed






def rows_asterisks(rows):
    # Complete the outer loop range to control the number of rows
    for x in range(1, rows+1): 
        # Complete the inner loop range to control the number of 
        # asterisks per row
        for y in range(x): 
            # Prints one asterisk and one space
            print("*", end=" ")
        # An empty print() function inserts a line break at the 
        # end of the row 
        print()
rows_asterisks(5)
# Should print the asterisk rows shown above

def divisible(max, divisor):
    count = 0 # Initialize an incremental variable
    for x in range(max): # Complete the for loop
        if x % divisor == 0:
            count += 1 # Increment the appropriate variable
    return count
print(divisible(100, 10)) # Should be 10
print(divisible(10, 3)) # Should be 4
print(divisible(144, 17)) # Should be 9

def print_prime_factors(number):
  # Start with two, which is the first prime
  factor = 2
  # Keep going until the factor is larger than the number
  while factor <= number:
    # Check if factor is a divisor of number
    if number % factor == 0:
      # If it is, print it and divide the original number
      print(factor)
      number = number / factor
    else:
      # If it's not, increment the factor by one
      factor += 1
  return "Done"
print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT


def is_power_of_two(n):
  # Check if the number can be divided by two without a remainder
  if n == 0:
    return False
  while n % 2 == 0:
    n = n / 2
  # If after dividing by two the number is 1, it's a power of two
  if n == 1:
    return True
  return False
print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

import math
def sum_divisors(n):
  sum = 1
  # Return the sum of all divisors of n, not including n
  div = 2
  if n == 0:
    return 0
  while div < n/2+1:
    if n % div == 0:
      sum += div
    div += 1
  return sum
print(sum_divisors(6)) # Should be 6 (sum of 1+2+3)
print(sum_divisors(12)) # Should be 16 (sum of 1+2+3+4+6)

def multiplication_table(number):
	# Initialize the starting point of the multiplication table
	multiplier = 1
	# Only want to loop through 5
	while multiplier <= 5:
		result = number*multiplier 
		# What is the additional condition to exit out of the loop?
		if result>25:
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		# Increment the variable for the loop
		multiplier += 1
multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24

def factorial(n):
    result = 1
    for x in range(2,n+1):
        result *= x
    return result
for n in range(10):
    print(n, factorial(n))

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1
  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)
print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

def sum_positive_numbers(n):
  sum = 0
  if n == 1:
    return 1
  else:
    sum += n + sum_positive_numbers(n-1)    
  return sum
print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

def loop(start, stop, step):
	return_string = ""
	if step == 0:
		step = 1
	if start > stop:
		step = abs(step) * -1
	else:
		step = abs(step)
	for count in range(start,stop,step):
		return_string += str(count) + " "
	return return_string.strip()
print(loop(11,2,3)) # Should be 11 8 5
print(loop(1,5,0)) # Should be 1 2 3 4
print(loop(-1,-2,0)) # Should be -1
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24 
print(loop(1,1,1)) # Should be empty

def counter(start, stop):
	x = start
	if start > stop:
		return_string = "Counting down: "
		while x >= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x -= 1			
	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x != stop:
				return_string += ","
			x += 1
	return return_string
print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

def multiplication_table(start, stop):
	for x in range(start, stop+1):
		for y in range(start, stop+1):
			print(x*y, end=" ")
		print()
multiplication_table(1, 3)
# Should print the multiplication table shown above

import math
def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (n>0):
		count += 1
		n = math.floor(n/10)
	return count
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = int(filesize/block_size)
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize%block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return (full_blocks+1)*block_size
    return full_blocks*block_size

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

def format_name(first_name, last_name):
	# code goes here
	string = "Name: "
	if first_name != "" and last_name != "":
	  string += last_name + ", " + first_name
	elif first_name != "" and last_name == "":
	  string += first_name
	elif first_name == "" and last_name != "":
	  string += last_name
	else:
	  string = ""
	return string 
print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"
print(format_name("", "Madonna"))
# Should be "Name: Madonna"
print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"
print(format_name("", ""))
# Should be ""

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

def fractional_part(numerator, denominator):
	# Operate with numerator and denominator to 
	if denominator:
	  res = numerator/denominator
	else:
	  res = 0
	res = res - int(res)
# keep just the fractional part of the quotient
	return res
print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0
