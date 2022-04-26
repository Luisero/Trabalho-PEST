
import rich
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, FloatPrompt, InvalidResponse

console = Console()
mod_carro = dict()
'''
Nome do carro:string
Marca: string
Valor de fábrica: float
ParaPCD : bool
preco: float
quantidade: int
'''
carros = list()
def menu():
   
    menu = Table(title='Concessionária Sol quente')
    menu.add_column('Menu vendedor')
    menu.add_column('Menu comprador')
    menu.add_row('Cadastrar carro','Consultar carro')
    menu.add_row('Editar','Comprar carro')
    console.print(menu)
    mode = inputEscolha('Digite aqui para se logar: [0]Vendedor [1]|Ciente: ', ['0','1'], 'Valor inválido! Tente novamente')
    #modo vendedor
    if mode == '0':
        #menu de vendas
        continuar = 's'
        while continuar == 's':
            modo = inputEscolha('O que deseja fazer? [0]Cadastrar [1]Editar: ',['0','1'], 'Valor inválido! Tente novamente')
            #modo cadastrar
            if modo == '0':
                marca = inputText('Qual a marca do carro? ')
                modelo = inputText('Qual o modelo do carro? ')
                valor_fabrica = inputFloat()

            else: #modo editar
                if len(carros) == 0:
                    print('Nenhum carro para editar.')
                else: 
                    printCarros(carros)

            continuar = inputEscolha('Deseja fazer mais alguma coisa? [s]Cadastrar ou editar [n]Voltar ao menu principal: ',['s','n'], 'Valor inválido! Tente novamente')

                    
    else: #modo cliente
        print('Cliente')
    
def inputEscolha(texto, escolhas, erro):
    res = input(texto).lower()

    while res != escolhas[0] and res != escolhas[1]:
        print(erro)
        res = input(texto).lower()
    if res == escolhas[0]:
        return escolhas[0]
    else:
        return escolhas[1]

def printCarros(lista_carro):
    for modelo in lista_carro:
        print(f"Marca: {modelo['Marca']}")

def inputText(texto):
    res = Prompt.ask(texto)
    while True:
        try:
            res = int(res)
            res = Prompt.ask('[on red]Valor inválido! Tente novamente.[on red/]')

        except:
            return res
    
def inputInt():
    pass

def inputFloat():
    try:
        res = FloatPrompt.ask()
    except InvalidResponse('fdf'):
        return res
      


menu() 