from rich.table import Table
from rich.console import  Console
from time import sleep

console = Console()
cadastro = dict()
controle = list()
edicao = dict()
elemento = dict()
def menu():
    global a
    tabela_menu = Table(title='Budega Sol Frio')
    tabela_menu.add_column('Cadastrar Produto', justify='center')
    tabela_menu.add_column(' Editar Produto ', justify='center')
    tabela_menu.add_column('  Fazer Comprar ', justify='center')
    tabela_menu.add_row('[Digite 1]','[Digite 2]','[Digite 3]')
    console.print(tabela_menu)
    a = inputnum('Digite aqui -> ', erro = 'Digite somente números! Tente novamente! \nDigite aqui -> ')
    if a == 1:
        cadastrar()
    elif len(controle) != 0:
        if a == 2:
            editar()
        elif a == 3:
            comprar()
    else:
        if a == 2:
            console.print('[on red]Não há item cadastrado![on red/]')
            menu()
        elif a == 3:
            console.print('[on red]Não há item cadastrado![on red/]')
            menu()
    while a != 1 and a != 2 and a != 3:
        console.print('[on yellow]Função não encontrada!\nTente novamente![on yellow/]')
        menu()
def cadastrar():
    global a
    while a == 1 or finalizar == 'S':
        cadastro.clear()
        produto = inputtexto('Digite o nome do produto: ', erro = 'Erro! Tente Novamente! \nDigite o nome do produto: ')
        igual = False
        for produto_modelo in controle:
            if produto_modelo['Produto'] == produto:
                igual = True
        while igual:
            console.print('[on yellow]Produto já cadastrado![on yellow/]')
            produto = inputtexto('Digite o nome do produto: ', erro = 'Erro! Tente Novamente! \nDigite o nome do produto: ')
            igual = False
            for produto_modelo in controle:
                if produto_modelo['Produto'] == produto:
                    igual = True
        cadastro['Produto'] = produto
        preco = inputfloat('Digite o Preço: R$ ', erro = 'Digite somente números! Tente novamente! \nDigite o Preço: R$ ')
        while preco <= 0:
            console.print('[on red]Valor inválido[on red/]')
            preco = inputfloat('Digite o Preço: R$ ', erro = 'Digite somente números! Tente novamente! \nDigite o Preço: R$ ')
        cadastro['Preço'] = preco
        quant = inputnum('Digite a quantidade de produtos: ', erro = 'Digite somente números! Tente novamente! \nDigite a quantidade de produtos: ')
        quant = int(quant)
        while quant <= 0:
            console.print('[on red]Valor inválido[on red/]')
            quant = inputnum('Digite a quantidade de produtos: ', erro = 'Digite somente números! Tente novamente! \nDigite a quantidade de produtos: ')
            quant = int(quant)
        cadastro['Quantidade'] = quant
        elemento[produto] = preco, quant
        controle.append(cadastro.copy())
        finalizar = pedir_texto('Quer cadastrar outro produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
        if finalizar == 'N':
            tabela()
            menu()
def editar():
    global a, buscar
    while a == 2:
        tabela()
        buscar = inputnum('Entre com um índice para mostrar o produto ou digite 1000 para parar: ', erro = 'Digite somente números! Tente novamente! \nEntre com um índice para mostrar o produto ou digite 1000 para parar: ')
        if buscar == 1000:
            menu()
        if buscar >= len(controle) or buscar < 0:
            console.print(f'[on red]Não temos produto com índice {buscar}[on red/]')
        else:
            console.print(f'[orange]O produto {buscar} é o {controle[buscar]["Produto"]}[orange/]')
            o = pedir_texto('Tem certeza que quer editar esse produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
            if o == 'N':
                console.print('[purple]Sem problemas![purple/]')
                editar()
            elif o == 'S':
                tabela_editar = Table(title='Opções de Edição')
                tabela_editar.add_column('  Nome do Produto   ', justify='center')
                tabela_editar.add_column(' Preço do Produto  ', justify='center')
                tabela_editar.add_column('Quantidade Disponível', justify='center')
                tabela_editar.add_row('[Digite 1]','[Digite 2]','[Digite 3]')
                console.print(tabela_editar)
                qualeditar = inputnum('Qual opção você quer editar? \nPara finalizar Digite 1000 \n -> ', erro = 'Digite somente números! Tente novamente! \nQual opção você quer editar? \nPara finalizar Digite 1000 \n -> ')
                while qualeditar > 0 and qualeditar <= 3:
                    if qualeditar == 1:
                        editar_nome()
                    elif qualeditar == 2:
                        editar_preco()
                    elif qualeditar == 3:
                        editar_quant()
                    while qualeditar != 1 and qualeditar != 2 and qualeditar != 3:
                        console.print('[on yellow]Função não encontrada!\nTente novamente![on yellow/]')
                        editar()
preco_compra = 0
def comprar():
    global a, preco_compra
    continuar = 'S'
    while a == 3 and continuar == 'S':
        tabela()
        compra = inputnum('Qual o índice do produto que deseja comprar? Se deseja cancelar Digite 1000 \n-> ', erro = 'Digite somente números! Tente novamente! \nQual o índice do produto que deseja comprar? Se deseja cancelar Digite 1000 \n-> ')
        if compra == 1000:
            menu()
        elif compra >= len(controle) or compra < 0:
            console.print(f'[on red]Não temos produto com índice {compra}[on red/]')
        else:
            console.print(f'[orange]O produto {compra} é o {controle[compra]["Produto"]}[orange/]')
            l = pedir_texto('Tem certeza que quer comprar esse produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
            if l == 'N':
                console.print('[purple]Sem problemas![/purple]')
                menu()
            elif l == 'S':
                qualquant = inputnum(f'Quantos {controle[compra]["Produto"]} você quer comprar? ', erro = f'Digite somente números! Tente novamente! \nQuantos {controle[compra]["Produto"]} você quer comprar? ')
                for i,produto in enumerate(controle):
                    if i == compra:
                        while qualquant > produto["Quantidade"] or qualquant <= 0:
                            console.print('[on red]Valor não suportado![on red/]')
                            comprar()
                        else:
                            preco_compra += produto["Preço"]*qualquant
                            console.print(f'[yellow]Sua compra está custando: R$ {preco_compra}[yellow/]')
                            produto["Quantidade"] -= qualquant
                            continuar = pedir_texto('Quer comprar outro produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
                            if continuar == 'N':
                                console.print(f'Sua compra ficou no valor de R$ [green]{preco_compra}[green/]')
                                pagamento = inputfloat('Digite o valor a ser entregue: \n-> ', erro = 'Digite somente números! Tente novamente! \nDigite o valor a ser entregue: ')
                                while pagamento < preco_compra:
                                    console.print(f'Valor menor que [red]R$ {preco_compra}[red/] \nDigite um valor válido!')
                                    pagamento = inputfloat('Digite o valor a ser entregue: \n-> ', erro = 'Digite somente números! Tente novamente! \nDigite o valor a ser entregue: ')
                                if pagamento > preco_compra:
                                    troco = pagamento - preco_compra
                                    console.print(f'Seu troco é de [green]R$ {troco}[green/] \nObrigado pela compra, volte sempre!')
                                    preco_compra = 0
                                    sleep(3)
                                    clear()
                                    menu()
                                else:
                                    console.print(f'[green]Obrigado pela compra, volte sempre![green/]')
                                    preco_compra = 0
                                    sleep(3)
                                    clear()
                                    menu()
                            else:
                                comprar()
                            tabela()
                            menu()

def tabela():
    tabela_prod = Table(title='Produtos')
    tabela_prod.add_column('#')
    tabela_prod.add_column('Produto')
    tabela_prod.add_column('Quantidade')
    tabela_prod.add_column('Preço')
    
    for i, prod in enumerate(controle):
        tabela_prod.add_row(str(i),prod['Produto'], str(prod['Quantidade']), f'[green]R$ {str(prod["Preço"])}[green/]')
    console.print(tabela_prod)

def editar_nome():
    global buscar
    edicao = controle[buscar]
    del controle[buscar]
    edit = inputtexto('Para qual nome? \n-> ', erro = 'Erro! Tente Novamente! \nPara qual nome? \n-> ')
    edicao['Produto'] = edit
    controle.append(edicao.copy())
    tabela()
    qeditar = pedir_texto('Quer editar outro produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
    if qeditar == 'S':
        editar()
    elif qeditar == 'N':
        menu()
def editar_preco():
    global buscar
    edicao = controle[buscar]
    del controle[buscar]
    edit = inputfloat('Para qual preço? \nR$ ', erro = 'Digite somente números! Tente novamente! \nPara qual preço? \nR$ ')
    edicao['Preço'] = edit
    controle.append(edicao.copy())
    tabela()
    qeditar = pedir_texto('Quer editar outro produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
    if qeditar == 'S':
        editar()
    elif qeditar == 'N':
        menu()
def editar_quant():
    global buscar
    edicao = controle[buscar]
    del controle[buscar]
    edit = inputnum('Qual a nova Quantidade? \n->', erro = 'Digite somente números! Tente novamente! \nQual a nova Quantidade? \n->')
    edicao['Quantidade'] = edit
    controle.append(edicao.copy())
    tabela()
    qeditar = pedir_texto('Quer editar outro produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
    if qeditar == 'S':
        editar()
    elif qeditar == 'N':
        menu()

def pedir_texto(texto, escolhas, erro):
    resposta = str(input(texto)).title()
    while resposta != escolhas[0] and resposta != escolhas[1]:
        print(erro)
        resposta = str(input(texto)).title()
    return resposta
def espaco(texto):
    espacos = 0
    for i in range(0, len(texto)):
        if texto[i:i+1] == ' ':
            espacos += 1
    if espacos == len(texto):
       return True
    else:
       return False

def inputtexto(texto, erro):
    resposta = input(texto).title()
    while True:
        try:
            resposta = int(resposta)
            resposta = input(erro).title()
        except:
            if espaco(resposta):
                resposta = input(erro).title()
            else:
                return resposta
def inputnum(texto, erro):
    resposta = input(texto)
    while True:
        try:
            resposta = int(resposta)
            return resposta
        except:
            resposta = input(erro)
def inputfloat(texto, erro):
    resposta = input(texto)
    while True:
        try:
            resposta = float(resposta)
            return resposta
        except:
            resposta = input(erro)
            
def clear():
    from os import system, name 
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
menu()

