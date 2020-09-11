'''
Created on 4 de abr de 2020

@author: tsjabrantes
'''

def decade_counter():
    year = 0   # The error was happening because variable year was not initialized.
    while year < 50:
        year += 10
    return year

print(decade_counter())