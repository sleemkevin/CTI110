Dictionaries, mutable
x = {}
type(x)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["txt"]
14

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
"jpg" in file_counts
"html" in file_counts
False

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["cfg"] = 8
print(file_counts)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["csv"] = 17
print(file_counts)

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23, 'cfg':8}
del file_counts["cfg"]
print(file_counts)

for loop prints keys
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
  print(extension)

.items gets pairs
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts.keys()
file_counts.values()

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for value in file_counts.values():
  print(value)

def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result
count_letters("aaaaa")
count_letters("tenant")
count_letters("a long string with a lot of letters")

