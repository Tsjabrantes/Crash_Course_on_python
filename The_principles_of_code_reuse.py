'''
Created on 20 de mar de 2020

@author: tsjabrantes
'''
# name = "Kay"
# number = len(name) * 9
# print("Hello " + name + ". Your lucky number is " + str(number))
# 
# name = "Cameron"
# number = len(name) * 9
# print("Hello " + name + ". Your lucky number is " + str(number))

# ***********************************************************************************************************
# Writing the same code above like a function
# Then we call the function twice, once with each name. Since we've grouped the calculation and print
# statements into a function, our code is not only easier to read but it's also now reusable. We can execute
# the code inside the lucky number function as many times as we need it, by just calling it with a different
# name.
# ***********************************************************************************************************
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")


