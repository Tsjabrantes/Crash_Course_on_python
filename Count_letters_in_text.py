'''
Created on 15 de mai de 2020

@author: tsjabrantes
'''
'''
Let's check out a simple example of counting how many times each letter
appears in a piece of text.
Here you can see how the dictionary can have any number of entries and the pairs
of key values always count how many of each letter there are in the string.
'''

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))


