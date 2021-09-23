def majority_element_indexes(lst):
    '''
    Return a list of the indexes of the majority element.
    Majority element is the element that appears more than
    floor(n / 2) times.
    If there is no majority element, return []
    >>> majority_element_indexes([1, 1, 2])
    [0, 1]
    >>> majority_element_indexes([1, 2])
    []
    >>> majority_element_indexes([])
    []
    '''
    # n = len(lst)//2 
    #  [1, 1, 2] {1: 2, 2, 1 } 


    n = len(lst) // 2
    count = 0
    seen = {}
    result = []
    for index, val in enumerate(lst):
        if val not in seen:
            seen[val] = index
            count += 1
        else:
            count += 1
            if count > n:
                res.append(seen[val])
                res.append(index)




