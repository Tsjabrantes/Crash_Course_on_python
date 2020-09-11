'''
Created on 23 de jun de 2020

@author: tsjabrantes
'''
'''
Ok, now it's your turn! Have a go writing methods for class. Create a Dog class with
dog-years based on Piglet class shown before (one human years is about 7 dog_years).
'''
class Dog:
    years = 0
    def dog_years(self):
        return self.years * 7
    
fido = Dog()
fido.years = 3
print(fido.dog_years())