'''
Created on 5 de jul de 2020

@author: tsjabrantes
'''
'''
Remember our Person class from the last video? Let’s add a docstring to the greeting method. How about, 
“Outputs a message with the name of the person”.
'''

class Person:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        """Outputs a message with the name of the person"""
        print("Hello! My name is {name}.".format(name=self.name)) 

help(Person)
