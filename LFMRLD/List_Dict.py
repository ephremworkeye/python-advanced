# List comprehenison offers a shorter syntax when we want to create a new list based on the values of an existing list
# syntax : newlist = [expression for item in iterable if condition == True]

even_numbers = [num for num in range(20) if num % 2 == 0]
print(even_numbers)

titles = [name.title() for name in ['abiy', 'alemu', 'dereje']]
titles2 = [name[0].upper() + name[1:] for name in ['abiy', 'alemu', 'dereje']]
print(titles)
print(titles2)

another = [letter for letter in 'helloworld' if letter in ['a', 'e', 'i', 'o', 'u']]
print(another)

output = [x if x > 6 else 'None' for x in range(20) if x % 2 == 0]
print(output)

# this listcomp combines the elements of two lists if they are not equal:
unique = [(x, y) for x in [2, 3, 4] for y in [3, 6, 9] if x != y]
print(unique)

# to get all positive
absolute = [abs(num) for num in [-6, 3, 4, -2, 1, 0, -9]]
print(absolute)

# nested list comprehension
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
 ]
rows = [[row[i] for row in matrix] for i in range(4)]
print(rows)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])

print(transposed)