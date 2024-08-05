String Indexing
fruit = "Pineapple"
print(fruit[:4])
print(fruit[4:])
pine
apple

name = "Jaylen"
print(name[1])
a

message = "A kong string with a silly typo"
new_message = message[0:2] + "l" + message[3:]
print(new_message)
A long string with a silly typo

pets="Cats & Dogs"
"Dragons" in pets
False
"Cats" in pets
True

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email


pets="Cats & Dogs"
pets.index("a")

"Mountains".upper()
"Mountains".lower()

answer = "YES"
if answer.lower() == "yes":
  print("User said yes")

"The number of times e occurs in this string is 4".count("e")

Strip removes whitespace, right and left
" yes ".strip()
" yes ".lstrip()
" yes ".rstrip()

"Forest".endswith("rest")
True

string.isalpha()
Isnumeric is just numbers
"Forest".isnumeric()
"12345".isnumeric()

int("12345") + int("54321")

" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"])
"...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"])

"This is another example".split()

string.split(delimiter) -
test = "How-much-wood-would-a-woodchuck-chuck"
print(test.split("-"))    

string.replace(old, new)
print(test.replace("wood", "plastic"))  # prints "How much plastic would a plasticchuck chuck"

delimiter.join(list of strings)
print("-".join(test.split()))

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))
Hello Manny, your lucky number is 15

name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
Your lucky number is 15, Manny.

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))
7.5 8.175
Base price: $7.50. With Tax: $8.18

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
 0 F | -17.78 C
 10 F | -12.22 C
 20 F |  -6.67 C
 30 F |  -1.11 C
 40 F |   4.44 C
 50 F |  10.00 C
 60 F |  15.56 C
 70 F |  21.11 C
 80 F |  26.67 C
 90 F |  32.22 C
100 F |  37.78 C

def student_grade(name, grade):
    return "{} received {}% on the exam.".format(name,grade)
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty 
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the 
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""
    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for string in input_string.lower():
        # The if-statement checks if the "letter" is not a space.
        if string.replace(" ",""):
            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
new_string = string + new_string
            reverse_string = string + reverse_string
    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code. 
    if new_string[::-1]==reverse_string:
        # If True, the "input_string" contains a palindrome.
        return True        
    # Otherwise, return False.
    return False
print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.1f} km".format(miles,km)
    return result
print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km


def nametag(first_name, last_name):
    return("{} {:.1s}.".format(first_name,last_name))
print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = sentence.rfind(old)
        new_sentence = sentence[:i]+new
        return new_sentence
    # Return the original sentence if there is no match 
    return sentence
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"
