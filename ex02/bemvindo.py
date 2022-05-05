


def boasVindas(texto,cor):
    from time import sleep
    from clear import clear
    from rich.console import Console
    console  = Console()
    for i in range(0,len(texto)):
        console.print(f'[{cor}]{texto[0:i+1]: ^25.25}[{cor}/]')
        sleep(.2)
        if i == len(texto)-1:
            sleep(1)
        clear()

if __name__ == '__main__':
    boasVindas('Bem vindo','on blue')