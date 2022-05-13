
'''email = input().lower()
email = email.split('@')


if len(email) == 2:
    for i in range(0,2):
        email[i] = email[i].split('.com')
    if len(email[1]) == 2:
        print('Email certin')

else:
    print('Valor invalido')
    

import os

print(os.getcwd())
print(__file__)

tamanho = len(__file__)
print(__file__[0:tamanho-8])'''

special_characters = "!@#$%^&*()-+?_=,<>/."
s=input()
# Example: $tackoverflow

if any(c in special_characters for c in s):
    print("yes")
else:
    print("no")