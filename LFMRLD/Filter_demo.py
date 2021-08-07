# Filter() method filters the given sequence with the help of a fucntion that tests element in the sequence to be true or not
# syntax filter(function, iterable)

# using lambda as function
odd_number = filter(lambda x: x % 2 != 0, range(20))
# print(dir(odd_number))
# print(odd_number.__next__())
# print(odd_number.__next__())
# print(odd_number.__next__())
print(list(odd_number))

# check vowel or consonant

def isVowel(letter):
    VOWEL = ('a', 'e', 'i', 'o', 'u')
    return True if letter in VOWEL else False

result = list(filter(isVowel, 'hello world, is there any thing new today?'))
print(result)





