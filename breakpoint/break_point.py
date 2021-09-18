import sys
# max =  7
# alist  = [4, 2, 7, 1]
# using print funciton
# def max_vlaue(alist):
#     max_num = -(sys.maxsize)
#     for num in alist:
#         print(num, max_num)
#         if num > max_num:
#             max_num = num
#     return max_num
# print(max_vlaue([4, 2, 7, 1]))

# def min_value(alist):
#     min_num = sys.maxsize
#     for num in alist:
#         print(num, min_num) 
#         if num < min_num:
#             min_num = num
#     return min_num

# print(min_value([-89999, 2, 0, -1, 10000]))

# def min_value(alist):
#     min_num = sys.maxsize
#     for num in alist:
#         breakpoint()
#         if num < min_num:
#             min_num = num
#     return min_num

# print(min_value([-89999, 2, 0, -1, 10000]))

def count_unique(s):
    """
    Count of unique characters in string
    >>> count_unique('aabb')
    2
    >>> count_unique('abcdef')
    6
    """
    
    # unique = {}
    # for char in s:
    #     if char not in unique:
    #         unique[char] = 1

    # return len(unique)

    # using set compherension
    return len({c for c in s})
    