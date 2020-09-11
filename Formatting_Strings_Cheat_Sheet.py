'''
Created on 9 de abr de 2020

@author: tsjabrantes
'''
# *********************************************************************************************************************************
# Python offers different ways to format strings. In the video, we explained the format() method. In this reading, we'll highlight
# three different ways of formatting strings. For this course you only need to know the format() method. But on the internet, you 
# might find any of the three, so it's a good idea to know that the others exist.
# Using the format() method
# 
# The format method returns a copy of the string where the {} placeholders have been replaced with the values of the variables. 
# These variables are converted to strings if they weren't strings already. Empty placeholders are replaced by the variables 
# passed to format in the same order.
# **********************************************************************************************************************************

# "base string with {} placeholders".format(variables)

example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# If the placeholders indicate a number, they’re replaced by the variable corresponding to that order (starting at zero).

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""

# If the placeholders indicate a field name, they’re replaced by the variable corresponding to that field name. 
# This means that parameters to format need to be passed indicating the field name.

# "{var1} {var2}".format(var1=value1, var2=value2)
# "{:exp1} {:exp2}".format(value1, value2)

# If the placeholders include a colon, what comes after the colon is a formatting expression. See below for the expression reference.

# {:d} integer value
# '{:d}'.format(10.5) → '10'














