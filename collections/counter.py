from collections import defaultdict, Counter
def top_three_letters(string):
    """
    Given a string find the top three most frequent letters 
    This method shoutld reutn al list of tuples, where the tuple contains the character and count

    >>> top_three_letters('abbccc')
    [('c', 3), ('b', 2), ('a', 1)]

    >>> top_three_letters('aabbccd')
    [('a', 2), ('b', 2), ('c', 2)]
    """
    # loop through the string and store the count for each letter
    # sort the dictionary by the count and find the top three most frequent letters
    # return a formatted list to match the output

    # counter = defaultdict(int)
    # for char in string:
    #     counter[char] += 1
    # top_three = sorted(counter, key=lambda count: counter[count], reverse=True)[:3]
    # result = []
    # for letter in top_three:
    #     result.append((letter, counter[letter]))
    # return result

    print(Counter(string).most_common(3))