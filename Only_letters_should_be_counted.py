'''
Created on 25 de mai de 2020

@author: tsjabrantes
'''
'''
Use a dictionary to count the frequency of letters in the input string. 
Only letters should be counted, not blank spaces, numbers, or punctuation. 
Upper case should be considered the same as lower case. 
For example, count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in ___:
    # Check if the letter needs to be counted or not
    ___
    # Add or increment the value in the dictionary
    ___
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
'''
def count_letters(text):
    result = {}
# Go through each letter in the text
#     print(text)
    for letter in text:
        letter_low = letter.lower()
# Check if the letter needs to be counted or not
        if letter_low.isalpha():
            if letter_low not in result:
                result[letter_low] = 0
# Add or increment the value in the dictionary
            result[letter_low] += 1          
    return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}
