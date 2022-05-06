email = input().lower()
email = email.split('@')


if len(email) == 2:
    for i in range(0,2):
        email[i] = email[i].split('.com')
    if len(email[1]) == 2:
        print('Email certin')

else:
    print('Valor invalido')
