'''
Created on Mar 31, 2020

@author: uid96630
'''
def is_perfect_power(a, b):
    while a % b == 0:
        a = a / b
    if a == 1:
        return True
    return False

print(is_perfect_power(8,2))