'''
Created on 7 de abr de 2020

@author: tsjabrantes
'''
# ******************************************************************************
# In these two expressions we're using the greater than operator to align text to
# the right so that the output is neatly aligned.
# In the first expression we're saying we want the numbers to be aligned to
# the right for a total of three spaces. 
# ********************************************************************************
def to_ceslsius(x):
    return (x-32)*5/9
for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_ceslsius(x)))