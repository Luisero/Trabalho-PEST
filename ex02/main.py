from curses.ascii import isspace
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from clear import clear
from bemvindo import boasVindas
console = Console()
mod_carro = dict()
'''
Modelo do carro:string
Marca: string
Valor de fábrica: float
ParaPCD : string (sim/nao)
preco: float
quantidade: int
'''
carros = list()
clear() 
#boasVindas('Bem vindo!','blue')
def menu():
   while True:
        
        menu = Table(title='Concessionária Sol quente')
        menu.add_column('Menu vendedor')
        menu.add_column('Menu comprador')
        menu.add_row('Cadastrar carro','Consultar carro')
        menu.add_row('Editar','Comprar carro')
        console.print(menu)
        mode = inputEscolha('Digite aqui para se logar: [green][0][green/]Vendedor [blue][1][blue/]Cliente ', escolhas=['0','1'], erro='[on red]Valor inválido! Tente novamente[on red/]')
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
            res = inputEscolha('Deseja consultar um carro? [green][0]Sim[green/] [blue][1]Sair ao menu[blue/]', escolhas=['0','1'], erro='[on red]Valor inválido. Tente novamente[on red/]')

            if res == '1': #sair ao menu
                pass
            else: #Consultar o carro
    
                if len(carros) == 0:
                    console.print('[yellow]Nenhum carro disponível.[yellow/]')
                else:
                    cliente_pcd = inputEscolha('Vocé é PCD? [green][0]Sim[green/] [blue][1]Não [blue/]', escolhas=['0','1'], erro='[on red]Valor inválido. Tente novamente[on red/]')
                    if cliente_pcd == '0':
                        cliente_pcd = True
                    else:
                        cliente_pcd = False

                    consultar(cliente_pcd)
                     
                    






def cadastrar():
    continuar  = 's'
    while continuar == 's':
        mod_carro.clear()

        marca = inputText('Qual a marca do carro? ').title()
        modelo = inputText('Qual o modelo do carro? ').title()
        #verificar se o modelo já está cadastrado
        igual = True
        while igual:
            if len(carros) != 0:
                for carro in carros:
                    if modelo == carro['Modelo']:
                        igual = True
                        console.print('[on red]Carro já cadastrado![on red/]')
                        modelo = inputText('Qual o modelo do carro? ').title()
                        if modelo != carro['Modelo']:
                            igual = False
                    else:
                        igual = False
                
            else:
                igual = False

        valor_fabrica = inputFloat('Qual o valor de fabrica? ')
        while valor_fabrica <= 0:
            console.print('[on red]Valor inválido. Tente novamente[on red/]]')
            valor_fabrica = inputFloat('Qual o valor de fabrica? ')
        quantidade = inputInt('Qual a quantidade?')
        while quantidade <=0:
            console.print('[on red]Valor inválido. Tente novamente[on red/]]')
            quantidade = inputInt('Qual a quantidade?')
        paraPCD = inputEscolha('Esse carro é para PCD? [green][0]Sim[green/] [blue][1]Não[blue/]',escolhas=['0','1'], erro='Valor inválido! Tente novamente')
        if paraPCD == '0':
            paraPCD='Sim'
        else:
            paraPCD = 'Não'
        preco = 0
        if paraPCD=='Sim':
            preco = f'{valor_fabrica*1.15:.2f}' #o preço é o valor de fabrica + 15%
        else:
            preco = f'{valor_fabrica*1.3:.2f}' #o preoço é o valor de fabrica + 30%
        preco = float(preco)
        mod_carro['Marca'] = marca
        mod_carro['Modelo'] = modelo
        mod_carro['Valor_fabrica'] = valor_fabrica
        mod_carro['Quantidade'] = quantidade
        mod_carro['Para_PCD'] = paraPCD
        mod_carro['Preco'] = preco
        carros.append(mod_carro.copy())
        continuar = inputEscolha('Deseja continuar? [green][0]Sim[green/] [blue][1]Não[blue/]',escolhas=['0','1'], erro='[on red]Valor inválido! Tente novamente.[on red/]')
        if continuar == '0':
            continuar = 's'
        else:
            continuar = 'n'


def editar():
    continuar = '0'
    while continuar == '0':
        if len(carros) == 0:
            console.print('[on yellow]Nenhum carro para editar.[on yellow/]')
        else: 
            clear()
            printCarros(carros)
            modelo = inputText('Qual o modelo do carro para editar? ').title()
            achou = False
            for carro in carros:
                if carro['Modelo'] == modelo:
                    achou = True
            while not achou:
                console.print('[on red]Carro não encontrado![on red/]')
                modelo = inputText('Qual o modelo do carro para editar? ').title()
                for carro in carros:
                    if carro['Modelo'] == modelo:
                        achou = True
            for i,modelo_carro in enumerate(carros):
                if modelo_carro['Modelo'] == modelo:
                    achou = True
                    chave = inputEscolha('O que você que editar? [blue][Preco][blue/] [green][Quantidade][green/]', escolhas=['Preco','Quantidade'], erro='[on red]Valor inválido![on red/]')
                    if chave == 'Preco':
                        preco =  inputFloat('Digite o novo preço ')
                        while preco <= 0:
                            console.print('[on red]Valor inválido. Tente novamente[on red/]]')
                            preco =  inputFloat('Digite o novo preço ')
                        modelo_carro['Preco'] = preco

                    else:
                        quantidade = inputInt('Digite a nova quantidade')
                        while quantidade <= 0:
                            console.print('[on red]Valor inválido. Tente novamente[on red/]]')
                            quantidade = inputInt('Digite a nova quantidade')
                        modelo_carro['Quantidade'] = quantidade
        continuar = inputEscolha('Deseja continuar editando carros? [green][0]Sim[green/] [blue][1]Não[blue/]',escolhas=['0','1'], erro='[on red]Valor inválido[on red/]')
                
def consultar(cliente_pcd):
    clear()
    carros_pcd = []
    carros_nopcd = []

    for carro in carros: #cria uma lista de carros pcd e de não pcd
        if carro['Para_PCD'] == 'Sim':
            carros_pcd.append(carro) 
        else:
            carros_nopcd.append(carro)
    if carros_pcd: #se o cliente for pcd
        printCarros(carros_pcd)
        quercomprar = inputEscolha('Quer comprar um carro? [green][0]Sim[green/] [blue][1]Não[blue/]', escolhas=['0','1'], erro='[on red]Valor inválido! Tente novamente [on red/]')
        if quercomprar == '0':
           comprar(carros_pcd) 
            
        else:
            console.print('[on yellow]Tudo bem[on yellow/]')
        printCarros(carros_pcd)
    else:#se o cliente não for pcd
        printCarros(carros_nopcd)

def comprar(lista_carros):
    modelo = inputText('Qual o modelo do carro quer comprar? ').title()
    achou = False
    for carro in lista_carros:
        if carro['Modelo'] == modelo:
            achou = True
            quantidade = inputInt('Quantos carros quer comprar? ')
            while quantidade <= 0 or ((carro['Preco'] - quantidade )<0):
                console.print('[on red]Valor inválido! Tente novamente [on red/]')
                quantidade = inputInt('Quantos carros quer comprar? ')
            

    while not achou:
        console.print('[on red]Carro não encontrado![on red/]')
        modelo = inputText('Qual o modelo do carro comprar? ').title()
        for carro in lista_carros:
            if carro['Modelo'] == modelo:
                achou = True

  



#############INPUTS##################################################################
def inputEscolha(texto, escolhas, erro):
    res = Prompt.ask(texto).title()
    if len(escolhas) == 2:
        while res != escolhas[0] and res != escolhas[1]:
            console.print(erro)
            res = Prompt.ask(texto).title()
        if res == escolhas[0]:
            return escolhas[0]
        else:
            return escolhas[1]
    

def inputText(texto):
    res = Prompt.ask(texto).title()
    while True:
        try:
            res = int(res)
            res = Prompt.ask('[on red]Valor inválido! Tente novamente.[on red/] ')

        except:
            if isSpace(res):
                res = Prompt.ask('[on red]Valor inválido! Tente novamente.[on red/] ')
            else:
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
             
        

def inputFloat(texto):
    res = Prompt.ask(texto)
    while True:
        try:
            res = float(res)
        except :
            console.print('[on red]Valor inválido! Tente novamente.[on red/] ')
            res = Prompt.ask(texto)
        if(type(res) == float):
            return res
            
def isSpace(texto):
    espacos = 0
    for i in range(0, len(texto)):
        if texto[i:i+1] == ' ':
            espacos += 1

    if espacos == len(texto):
       return True
    else:
       return False

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
        pcd_text = ''
        if modelo['Para_PCD'] == 'Sim':
            pcd_text = f'[blue]{modelo["Para_PCD"]}[blue/]'
        else:
            pcd_text = f'[yellow]{modelo["Para_PCD"]}[yellow/]'
        menu_carros.add_row(modelo['Marca'], modelo['Modelo'], '[green]R$'+str(modelo['Preco'])+'[green/]', '[blue]'+str(modelo['Quantidade'])+'[blue/]', 'R$'+str(modelo['Valor_fabrica']), pcd_text)
    console.print(menu_carros)
menu() 