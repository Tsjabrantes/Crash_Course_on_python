'''
Created on Mar 19, 2020

@author: uid96630
'''
def hint_username(username):
    if len(username) < 3:
        print("Invalid username. must be at least 3 characters long")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username")   

hint_username("Tsjabrantes")