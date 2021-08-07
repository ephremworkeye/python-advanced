#zip funciton

alist1 = [1, 2, 3, 4]
alist2 = [5, 6, 7, 8]
alist3 = [9, 10, 11, 12]
print(list(zip(alist1, alist2, alist3)))

a, b, c = zip(*zip(alist1, alist2, alist3))
print(a, b, c)