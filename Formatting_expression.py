'''
Created on 7 de abr de 2020

@author: tsjabrantes
'''
# ***********************************************************************************************
# In this case between the curly brackets we're writing a formatting expression.
# There are a bunch of different expressions we can write.
# These expressions are needed when we want to tell Python to format our values in
# a way that's different from the default.
# The expression starts with a colon to separate it from the field name that we
# saw before.
# After the colon, we write .2f.
# This means we're going to format a float number and
# that there should be two digits after the decimal dot.
# So no matter what the price is, our function always prints two decimals. 
# *************************************************************************************************
price = 7.5
with_tax = price * 1.09
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

