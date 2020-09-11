'''
Created on 26 de jun de 2020

@author: tsjabrantes
'''
class Apple():
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    def __str__(self):
        return "This apple is {} and it's flavor is {}.".format(self.color, self.flavor)
    
jonagold = Apple("red", "sweet")
print(jonagold)