'''
Created on 2 de mai de 2020

@author: tsjabrantes
'''
# ******************************************************************************************************************
# Try out the enumerate function for yourself in this quick exercise. Complete the skip_elements function to return 
# every other element from the list, this time using the enumerate function to check if an element is on an even 
# position or an odd position.
# ******************************************************************************************************************
'''
def skip_elements(elements):
    # code goes here
    
    return ___

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
'''
def skip_elements(elements):
    # code goes here
    new_list = []
    index = 0

    # Iterate through the list
    for index, element in enumerate(elements):
        new_list.append("{}".format(element))
    return new_list[::2]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

