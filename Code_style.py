'''
Created on 21 de mar de 2020

@author: tsjabrantes
'''
def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)

# *****************************************************************************************
# In programming lingo, when we
# re-write code to be more self-documenting,
# we call this process refactoring.
# So how would it look if we refactored this code?
# *****************************************************************************************

def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)
    
circle_area(5)

