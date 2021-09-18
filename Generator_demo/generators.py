
# res = (i for i in range(5))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

import sys


# alist = [i for i in range(100000)]
# print(sys.getsizeof(alist)) 
# agene = (i for i in range(100000))
# print(sys.getsizeof(agene))

def add(alist):
    res = 0
    for i in alist:
        res += i
    yield res
        

print(next(add([2, 3, 4, 5])))