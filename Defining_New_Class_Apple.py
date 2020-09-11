'''
Created on 2 de jun de 2020

@author: tsjabrantes
'''
'''
class Apple:
    pass
'''    

class Apple:
     
    color = ""      # attributes 
    Flavor = ""     # attributes
        
jonagold = Apple()              # we're creating a new instance of
jonagold.color = "red"          # to a variable called 
jonagold.flavor = "sweet"       # our Apple class and assigning it
                                # jonagold.
print(jonagold.color)           # The syntax used to access the attributes is called
print(jonagold.flavor)          # dot notation because of the dot used in the expression.
print(jonagold.color.upper())   # Dot notation lets you access any of
                                # the abilities that the object might have,
golden = Apple()                # called methods or information that
golden.color = "Yellow"         # it might store called attributes, like flavor.
golden.flavor = "Soft"          # The attributes and methods of some objects can be
                                # other objects and can have
print(golden.color)             # attributes and methods of their own.
print(golden.flavor)            # For example, we could use the upper method
print(golden.color.upper())     # to turn the string of the color attribute to uppercase.
                                # So print (jonagold.color.upper()).
                                # Both golden and jonagold are instances of the Apple class. 