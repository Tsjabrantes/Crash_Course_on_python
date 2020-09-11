'''
Created on Mar 31, 2020

@author: uid96630
'''
# ***********************************************************************************************
# Additional Recursion Sources
# 
# In the past videos, we visited the basic concepts of recursive functions.
# 
# A recursive function must include a recursive case and base case. 
# The recursive case calls the function again, with a different value.
# The base case returns a value without calling the same function.
# 
# A recursive function will usually have this structure:
# def recursive_function(parameters):
#     if base_case_condition(parameters):
#         return base_case_value
#     recursive_function(modified_parameters)
# **************************************************************************************************
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:                   # --> Conditional block in the Base case
        print("Returning 1")                   
        return 1
    result = n * factorial(n - 1) # --> Recursive case
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial(4)