'''
Created on 5 de abr de 2020

@author: tsjabrantes
'''
# ******************************************************************************************************************
# Modify the double_word function so that it returns the same word repeated twice, followed by the length of the new
# doubled word. For example, double_word("hello") should return hellohello10.
# ******************************************************************************************************************
def double_word(word):
    return word * 2 + str(len(word * 2))

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0