x = ["Now", "we", "are", "cooking!"]
type(x)
<class 'list'>

x = ["Now", "we", "are", "cooking!"]
print(x)
['Now', 'we', 'are', 'cooking!']

x = ["Now", "we", "are", "cooking!"]
len(x)
4

x = ["Now", "we", "are", "cooking!"]
"are" in x
True

x = ["Now", "we", "are", "cooking!"]
print(x[0])
print(x[3])
x[:2]

def get_word(sentence, n):
    # Only proceed if n is positive 
    if n > 0:
        words = sentence.split()
        # Only proceed if n is not more than the number of words 
        if n <= len(words):
            return(words[n-1])
    return("")
print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kiwi")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
print(fruits)

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")
fruits.insert(25, "Peach")
fruits.remove("Melon")
fruits.pop(3)
fruits[2] = "Strawberry"
print(fruits)

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
print(result)
(1, 23, 20)

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
result = convert_seconds(5000)
hours, minutes, seconds = result
print(hours, minutes, seconds)
1 23 20

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds - hours * 3600) // 60
  remaining_seconds = seconds - hours * 3600 - minutes * 60
  return hours, minutes, remaining_seconds
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)
0 16 40

Tuples, immutable, parentheses
fullname = ('Grace', 'M', 'Hopper')

def file_size(file_info):
    name, type, number= file_info
    return("{:.2f}".format(number / 1024))
print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)
print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
Total characters: 22, Average length: 5.5

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))
1 - Ashley
2 - Dylan
3 - Reese

def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))
['Alex Diego <alex@example.com>', 'Shay Brandt <shay@example.com>']

def skip_elements(elements):
    # code goes here
    new_list = []
    for index, element in enumerate(elements):
        if index%2==0: 
            new_list.append(element)
    return(new_list)
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

List Comprehension
multiples = []
for x in range(1,11):
  multiples.append(x*7)
print(multiples)
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]

multiples = [x*7 for x in range(1,11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)
[6, 4, 4, 2, 4, 1]

z = [x for x in range(0,101) if x % 3 == 0]
print(z)

def odd_numbers(n):
    return [x for x in range(n+1) if x%2 !=0]
print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames= [file.replace('.hpp','.h') for file in filenames]
print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for file in filenames:
  if '.hpp' in file:
    newfilenames.append((file,file[:-2]))
  else:
    newfilenames.append((file,file))

print (newfilenames)

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate new_filenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
new_filenames = []
for filename in filenames:
    if filename.endswith('.hpp'):
        new_filename = filename.replace('.hpp', '.h')
        new_filenames.append(new_filename)
    else:
        new_filenames.append(filename)
print(new_filenames)

def pig_latin(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say += word[1:]+word[0]+'ay'
    if word != words[len(words)-1]:
      say +=' '
    # Turn the list back into a phrase
  return say
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def biography_list(people):
    # Iterate over each "person" in the given "people" list of tuples. 
    for person in people: 
        # Separate the 3 items in each tuple into 3 variables:
        # "name", "age", and "profession" 
    name, age, profession = person
        # Format the required sentence and place the 3 variables 
        # in the correct placeholders using the .format() method.
        print("{} is {} years old and works as {}.".format(name, age, profession))
# Call to the function:
biography_list([("Ira", 30, "a Chef"), ("Raj", 35, "a Lawyer"), ("Maria", 25, "an Engineer")])
# Click Run to submit code
# Output should match:
# Ira is 30 years old and works as a Chef
# Raj is 35 years old and works as a Lawyer
# Maria is 25 years old and works as an Engineer

