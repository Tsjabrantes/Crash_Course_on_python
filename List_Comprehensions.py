'''
Created on 4 de mai de 2020

@author: tsjabrantes
'''
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

# ****************************************************************************************************************************************
# List comprehensions let us create new lists based on sequences or ranges.
# So we can use this technique whenever we want to create a list based on a range
# like in this example.

multiples = [x * 7 for x in range(1, 11)]
print(multiples)

# ****************************************************************************************************************************************
# Let's check out a different example.
# Say we have a list of strings with the names of programming languages like
# this one, and we want to generate a list of the length of the strings.
# We could iterate over the list and add them using a pen like we did before.

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lenghts = [len(language) for language in languages]
print(lenghts)
