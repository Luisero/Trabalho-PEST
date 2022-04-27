
from turtle import mode
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
   while True:
        menu = Table(title='Concessionária Sol quente')
        menu.add_column('Menu vendedor')
        menu.add_column('Menu comprador')
        menu.add_row('Cadastrar carro','Consultar carro')
        menu.add_row('Editar','Comprar carro')
        console.print(menu)
        mode = inputEscolha('Digite aqui para se logar: [green][0][green/]Vendedor [blue][1][blue/]Cliente ', escolhas=['0','1'], erro='Valor inválido! Tente novamente')
        #modo vendedor
        if mode == '0':
            #menu de vendas
            continuar = 's'
            while continuar == 's':
                modo = inputEscolha('O que deseja fazer? [green][0][green/]Cadastrar [blue][1][blue/]Editar ',escolhas=['0','1'], erro='Valor inválido! Tente novamente')
                #modo cadastrar
                if modo == '0':
                    cadastrar()
                    
                else: #modo editar
                    editar()
                break

                
                
        else: #modo cliente
            print('Cliente')





def cadastrar():
    continuar  = 's'
    while continuar == 's':
        mod_carro.clear()
        marca = inputText('Qual a marca do carro? ').title()
        modelo = inputText('Qual o modelo do carro? ').title()
        valor_fabrica = inputFloat('Qual o valor de fabrica? ')
        quantidade = inputInt('Qual a quantidade?')
        paraPCD = inputEscolha('Esse carro é para PCD? [green][0]Sim[green/] [blue][1]Não[blue/]',escolhas=['0','1'], erro='Valor inválido! Tente novamente')
        if paraPCD == '0':
            paraPCD='Sim'
        else:
            paraPCD = 'Não'
        preco = 0
        if paraPCD=='s':
            preco = valor_fabrica*1.15 #o preço é o valor de fabrica + 15%
        else:
            preco = valor_fabrica*1.3 #o preoço é o valor de fabrica + 30%
        mod_carro['Marca'] = marca
        mod_carro['Modelo'] = modelo
        mod_carro['Valor_fabrica'] = valor_fabrica
        mod_carro['Quantidade'] = quantidade
        mod_carro['Para_PCD'] = paraPCD
        mod_carro['Preco'] = preco
        carros.append(mod_carro.copy())
        continuar = inputEscolha('Deseja continuar? [green][0]Sim[green/] [blue][1]Não[blue/]',escolhas=['0','1'], erro='[on red]Valor inválido! Tente novamente.[on red/]')


def editar():
    if len(carros) == 0:
        print('Nenhum carro para editar.')
    else: 
        printCarros(carros)




#############INPUTS##################################################################
def inputEscolha(texto, escolhas, erro):
    res = Prompt.ask(texto).lower()

    while res != escolhas[0] and res != escolhas[1]:
        console.print(erro)
        res = Prompt.ask(texto).lower()
    if res == escolhas[0]:
        return escolhas[0]
    else:
        return escolhas[1]


def inputText(texto):
    res = Prompt.ask(texto)
    while True:
        try:
            res = int(res)
            res = Prompt.ask('[on red]Valor inválido! Tente novamente.[on red/] ')

        except:
            return res
    
def inputInt(texto):
     while True:
        res = Prompt.ask(texto)
        try:
            res = int(res)
        except ValueError:
            console.print('[on red]Valor inválido! Tente novamente.[on red/] ')
        if(type(res) == int):
            return res
            break
        

def inputFloat(texto):
    while True:
        try:
            res = float(Prompt.ask(texto))
        except ValueError:
            console.print('[on red]Valor inválido! Tente novamente.[on red/] ')
        if(type(res) == float):
            return res
            break
########################################################################################
def printCarros(lista_carro):
    menu_carros = Table(title='Carros cadastrados')
    menu_carros.add_column('Marca')
    menu_carros.add_column('Modelo')
    menu_carros.add_column('Preço')
    menu_carros.add_column('Quantidade')
    menu_carros.add_column('Valor de fábrica')
    menu_carros.add_column('Para PCD?')
    for modelo in lista_carro:
        menu_carros.add_row(modelo['Marca'], modelo['Modelo'], '[green]R$'+str(modelo['Preco'])+'[green/]', '[blue]'+str(modelo['Quantidade'])+'[blue/]', str(modelo['Valor_fabrica']), modelo['Para_PCD'])
    console.print(menu_carros)
menu() 