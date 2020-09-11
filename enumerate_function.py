'''
Created on 4 de mai de 2020

@author: tsjabrantes
'''
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("alex@example.com", "Alex Diego"),
                   ("shay@example.com", "Shay Brandt")]))