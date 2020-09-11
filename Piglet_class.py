'''
Created on 23 de jun de 2020

@author: tsjabrantes
'''

class Piglet():
    name = "piglet"
    
    def speak(self):
        print("Oink! I'm {}! Oink!".format(self.name))

hamlet = Piglet()
hamlet.name = "Hamelet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

        