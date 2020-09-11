'''
Created on 23 de mai de 2020

@author: tsjabrantes
'''
'''
2.Question 2

The highlight_word function changes the given word in a sentence to its upper-case version. 
For example, highlight_word("Have a nice day", "nice") returns "Have a NICE day". 
Can you write this function in just one line? 

def highlight_word(sentence, word):
    return(___)

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
'''

def highlight_word(sentence, word):
    return("{}".format(sentence.replace(word,word.swapcase())))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))
