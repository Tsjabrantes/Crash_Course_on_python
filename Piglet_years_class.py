'''
Created on 23 de jun de 2020

@author: tsjabrantes
'''

class Piglet():
    years = 0
    def pig_years(self):
        return self.years * 18

piggy = Piglet()
print(piggy.pig_years())

piggy.years = 2
print(piggy.pig_years())
        