'''
Created on 11 de jul de 2020

@author: tsjabrantes
'''

class Birds():
    color = ""
    number = 0
    
    def count(self):
        return self.number + 1
parrot = Birds()
parrot.color = "bluejay"
parrot.number = 1
print(parrot.color + " " + str(parrot.count()))

'''
class Birds():
    def __init__(self, color, number):
        self.color = color
        self.number = number
    def __str__(self):
        return "This bird is {} and it's number is {}.".format(self.color, self.number + 1)
    
animal = Birds("bluejay", 1)
print(animal)
'''