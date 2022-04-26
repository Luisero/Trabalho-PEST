
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

console = Console()

def menu():
    carro = dict()
    carros = list()
    menu = Table(title='Concessionária Sol quente')
    menu.add_column('Menu vendedor')
    menu.add_column('Menu comprador')
    menu.add_row('Cadastrar carro','Consultar carro')
    menu.add_row('Editar','Comprar carro')
    console.print(menu)
    mode = Prompt.ask('Digite para se logar. [0]Vendedor [1]Comprador', choices=['0','1'])
    if mode == '0':
        mode = Prompt.ask()

menu() 