'''
Created on 25 de mar de 2020

@author: tsjabrantes
'''
# *************************************************************************************************************
# This parameter is called End.
# Normally, once print has taken
# the content we passed and written it to the screen,
# then it writes a special character that creates
# a new line called the newline character.
# *************************************************************************************************************

left = 0
for left in range(left, 7):
    for right in range(left, 7):
        print("[" + str(left) + "|" + str(right) + "]", end=" ")
    print()