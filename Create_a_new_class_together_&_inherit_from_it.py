'''
Created on 11 de jul de 2020

@author: tsjabrantes
'''
'''
Let’s create a new class together and inherit from it. Below we have a base class called Clothing. 
Together, let’s create a second class, called Shirt, that inherits methods from the Clothing class. 
Fill in the blanks to make it work properly.
'''

class Clothing:
    material = ""
    def __init__(self,name):
        self.name = name
    def checkmaterial(self):
        print("This {} is made of {}.".format(self.name,self.material))
            
class Shirt(Clothing):
    material="Cotton"

polo = Shirt("Polo")
polo.checkmaterial()
