student_grades = {
    'Abiy': [95, 80],
    'Abebe': [79, 86],
    'Demeke': [75, 87]
}

# def get_grades(name):
#     if name in student_grades:
#         return student_grades[name]
#     else:
#         return []

# print(get_grades('Abiy'))


# better way
# def get_name(name):
#     return student_grades.get(name, [])

# print(get_name('sado'))

# what if we want to add element if we don't find

# def get_name(name, grade=[]):
#     return student_grades.setdefault(name, grade)

# # print(get_name('sador', [89, 100]))
# print(get_name('Abiy', [89, 100]))

# using defaultdict
from collections import defaultdict

counter = defaultdict(int)
for char in 'hello world':
    counter[char] += 1

print(counter)

