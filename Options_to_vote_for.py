'''
Created on 4 de abr de 2020

@author: tsjabrantes
'''

def votes(params):
    for vote in params:
        print("Possible option:" + vote)

votes(['yes', 'no', 'maybe'])