def clear():
    from os import system, name 
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')