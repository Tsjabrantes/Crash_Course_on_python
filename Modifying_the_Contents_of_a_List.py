'''
Created on 2 de mai de 2020

@author: tsjabrantes
'''
# *****************************************************************************************************************
# The skip_elements function returns a list containing every other element from an input list, starting with the 
# first element. Complete this function to do that, using the for loop to iterate through the input list.
# *****************************************************************************************************************
'''
def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for ___
        # Does this element belong in the resulting list?
        if ___
            # Add this element to the resulting list
            ___
        # Increment i
        ___

    return ___

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []
'''
def skip_elements(elements):
    # Initialize variables
    new_list = []
    i = 0

    # Iterate through the list
    for element in elements:
        # Does this element belong in the resulting list?
        if element not in new_list:
            # Add this element to the resulting list
            new_list.append(element)
        # Increment i
        i += 1

    return new_list[::2]

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []



