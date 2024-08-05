class Apple:
    def __init__(self):
        self.color = "red"
        self.flavor = "sweet"
honeycrisp = Apple()
print(honeycrisp.color)
# prints "red"

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
honeycrisp = Apple("red", "sweet")
fuji = Apple("red", "tart")
print(honeycrisp.flavor)
print(fuji.flavor)
# prints "sweet" and "tart"

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "an apple which is {} and {}".format(self.color, self.flavor)
honeycrisp = Apple("red", "sweet")
print(honeycrisp)
# prints "an apple which is red and sweet"

class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
jonagold = Apple("red", "sweet")
print(jonagold.color)


class Apple:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and its flavor is {}".format(self.color, self.flavor)
jonagold = Apple("red", "sweet")
print(jonagold)

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def __add__(self, other):
        return self.area() + other.area()    
triangle1 = Triangle(10, 5)
triangle2 = Triangle(6, 8)
print("The area of triangle 1 is", triangle1.area())
print("The area of triangle 2 is", triangle2.area())
print("The area of both triangles is", triangle1 + triangle2)

def confirm_length(word):
    # Complete the condition statement using a string operation. 
    if len(word) > 0: 
        # Complete the return statement using a string operation.
        return len(word) 
    else:
        return 0
print(confirm_length("a")) # Should print 1
print(confirm_length("This is a long string")) # Should print 21
print(confirm_length("Monday")) # Should print 6
print(confirm_length("")) # Should print 0

def string_words(string):
    # Complete the return statement using both a string operation and 
    # a string method in a single line.
    return len(string.split())
print(string_words("Hello, World")) # Should print 2
print(string_words("Python is awesome")) # Should print 3
print(string_words("Keep going")) # Should print 2
print(string_words("Have a nice day")) # Should print 4

def alphabetize_lists(list1, list2):
  new_list = [] # Initialize a new list.
  new_list = list1 + list2 # Combine the lists.
  new_list.sort() # Sort the combined lists.
  return new_list 
Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]
print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']

def increments(start, end):
    return [ n+2 for n in range(start, end+1) ] # Create the required list comprehension.
print(increments(2, 3)) # Should print [4, 5]
print(increments(1, 5)) # Should print [3, 4, 5, 6, 7]
print(increments(0, 10)) # Should print [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def countries(countries_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.
    for continent, country in countries_dict.items():
        # Use a string method to format the required string.
        result += "{}".format(country) + '\n'
    return result
print(countries({"Africa": ["Kenya", "Egypt", "Nigeria"], "Asia":["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))
# Should print:
# ['Kenya', 'Egypt', 'Nigeria']
# ['China', 'India', 'Thailand']
# ['Ecuador', 'Bolivia', 'Brazil']

def combine_guests(guests1, guests2):
  guests2.update(guests1) # Use a dictionary method to combine the dictionaries.
  return guests2
Ricks_guests = { "Adam":2, "Camila":3, "David":1, "Jamal":3, "Charley":2, "Titus":1, "Raj":4}
Tessas_guests = { "David":4, "Noemi":1, "Raj":2, "Adam":1, "Sakira":3, "Chidi":5}
print(combine_guests(Ricks_guests, Tessas_guests))
# Should print:
# {'David': 1, 'Noemi': 1, 'Raj': 4, 'Adam': 2, 'Sakira': 3, 'Chidi': 5, 'Camila': 3, 'Jamal': 3, 'Charley': 2, 'Titus': 1}

def count_letters(text):
  import string
  # Initialize a new dictionary.
  result = {} 
 # Complete the for loop to iterate through each "text" character and 
  # use a string method to ensure all letters are lowercase.
  for letter in text: 
    # Complete the if-statement using a string method to check if the
    # character is a letter.
    if letter in string.ascii_letters:
      letter = letter.lower() 
      # Complete the if-statement using a logical operator to check if 
      # the letter is not already in the dictionary.
      if letter not in result:
           # Use a dictionary operation to add the letter as a key
           # and set the initial count value to zero.
        result[letter] = 0       
      # Use a dictionary operation to increment the letter count value 
      # for the existing key.
      result[letter] += 1   
  return result
print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}
print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
