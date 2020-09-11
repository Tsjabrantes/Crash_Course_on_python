'''
Created on 6 de abr de 2020

@author: tsjabrantes
'''
# *****************************************************************************************************************
# Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase
# received, in upper case. For example: "Universal Serial Bus" should return "USB"; "local area network" should
# return "LAN”. 
# ******************************************************************************************************************
# def initials(phrase):
#     words = phrase.___
#     result = ""
#     for word in words:
#         result += ___
#     return ___
# 
# print(initials("Universal Serial Bus")) # Should be: USB
# print(initials("local area network")) # Should be: LAN
# print(initials("Operating system")) # Should be: OS

def initials(phrase):
    words = phrase.split(" ")
    result = ""
    for word in words:
        result += "".join(word[0])
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS