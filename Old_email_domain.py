'''
Created on 6 de abr de 2020

@author: tsjabrantes
'''
def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in  email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print(replace_domain("tsjabrantes@hotmail.com", "hotmail.com", "gmail.com"))
print(replace_domain("tsjabrantes@yahoo.com.br", "yahoo.com.br", "gmail.com"))