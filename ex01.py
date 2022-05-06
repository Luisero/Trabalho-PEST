cadastro = dict()
controle = list()
edicao = dict()
elemento = dict()
def menu():
    global a
    a = inputnum('[1] Cadastrar produto \n[2] Editar produto \n[3] Fazer compra \n -> ', erro = 'Digite somente números! Tente novamente! \n[1] Cadastrar produto \n[2] Editar produto \n[3] Fazer compra \n -> ')
    if a == 1:
        cadastrar()
    elif len(controle) != 0:
        if a == 2:
            editar()
        elif a == 3:
            comprar()
    else:
        if a == 2:
            print('Não há item cadastrado!')
            menu()
        elif a == 3:
            print('Não há item cadastrado!')
            menu()
    while a != 1 and a != 2 and a != 3:
        print('Função não encontrada! \nTente novamente!')
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
            print('Produto já cadastrado!')
            produto = inputtexto('Digite o nome do produto: ', erro = 'Erro! Tente Novamente! \nDigite o nome do produto: ')
            igual = False
            for produto_modelo in controle:
                if produto_modelo['Produto'] == produto:
                    igual = True
        cadastro['Produto'] = produto
        preco = inputfloat('Digite o Preço: R$ ', erro = 'Digite somente números! Tente novamente! \nDigite o Preço: R$ ')
        while preco <= 0:
            print('Valor inválido')
            preco = inputfloat('Digite o Preço: R$ ', erro = 'Digite somente números! Tente novamente! \nDigite o Preço: R$ ')
        cadastro['Preço'] = preco
        quant = inputnum('Digite a quantidade de produtos: ', erro = 'Digite somente números! Tente novamente! \nDigite a quantidade de produtos: ')
        quant = int(quant)
        while quant <= 0:
            print('Valor inválido')
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
        buscar = inputnum('Entre com um índice para mostrar o produto ou digite 1000 para parar: ', erro = 'Digite somente números! Tente novamente! \nEntre com um índice para mostrar o produto ou digite 1000 para parar: ')
        if buscar == 1000:
            menu()
        if buscar >= len(controle):
            print(f'Não temos produto com índice {buscar}')
        else:
            print(f'O produto {buscar} é o {controle[buscar]["Produto"]}')
            o = pedir_texto('Tem certeza que quer editar esse produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
            if o == 'N':
                print('Sem problemas!')
                editar()
            elif o == 'S':
                qualeditar = inputnum('Qual opção você quer editar? \n[1] Nome do Produto \n[2] Preço do Produto \n[3] Quantidade Disponível \nPara finalizar Digite 1000 \n -> ', erro = 'Digite somente números! Tente novamente! \nQual opção você quer editar? \n[1] Nome do Produto \n[2] Preço do Produto \n[3] Quantidade Disponível \nPara finalizar Digite 1000 \n -> ')
                while qualeditar > 0 and qualeditar <= 3:
                    if qualeditar == 1:
                        editar_nome()
                    elif qualeditar == 2:
                        editar_preco()
                    elif qualeditar == 3:
                        editar_quant()
                    while qualeditar != 1 and qualeditar != 2 and qualeditar != 3:
                        print('Função não encontrada! \nTente novamente!')
                        editar()
def comprar():
    global a, preco_compra, compra
    preco_compra = 0
    continuar = 'S'
    while a == 3 and continuar == 'S':
        tabela()
        compra = inputnum('Qual o índice do produto que deseja comprar? Se deseja cancelar Digite 1000 \n-> ', erro = 'Digite somente números! Tente novamente! \nQual o índice do produto que deseja comprar? Se deseja cancelar Digite 1000 \n-> ')
        if compra == 1000:
            menu()
        if compra >= len(controle):
            print(f'Não temos produto com índice {compra}')
        else:
            print(f'O produto {compra} é o {controle[compra]["Produto"]}')
            l = pedir_texto('Tem certeza que quer comprar esse produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
            if l == 'N':
                print('Sem problemas!')
                menu()
            elif l == 'S':
                quantidade()
def tabela():
    print('\n')
    print('-'*73)
    print('|     | Produto               | Preço                 | Quantidade            ')
    for a, b in enumerate(controle):
        print(f'| {a:>3}', end = ' ')
        for d in b.values():
            print(f'| {str(d):<21}', end = ' ')
        print('')
    print('\n')

def quantidade():
    global compra, preco_compra
    qualquant = inputnum(f'Quantos {controle[compra]["Produto"]} você quer comprar? ', erro = f'Digite somente números! Tente novamente! \nQuantos {controle[compra]["Produto"]} você quer comprar? ')
    for i,produto in enumerate(controle):
        if i == compra:
            if qualquant > produto["Quantidade"] or qualquant <= 0:
                print('Valor não suportado!')
                quantidade()
            else:
                preco_compra += produto["Preço"]*qualquant
                print(f'Sua compra está custando: R$ {preco_compra}')
                produto["Quantidade"] -= qualquant
                continuar = pedir_texto('Quer comprar outro produto? Digite [S] Sim ou [N] Não: ', escolhas=['S', 'N'], erro = 'Valor inválido, tente novamente!')
                if continuar == 'N':
                    print(f'Sua compra ficou no valor de R$ {preco_compra}')
                    pagamento = inputfloat('Digite o valor a ser entregue: \n-> ', erro = 'Digite somente números! Tente novamente! \nDigite o valor a ser entregue: ')
                    while pagamento < preco_compra:
                        print(f'Valor menor que R$ {preco_compra} \nDigite um valor válido!')
                        pagamento = inputfloat('Digite o valor a ser entregue: \n-> ', erro = 'Digite somente números! Tente novamente! \nDigite o valor a ser entregue: ')
                    if pagamento >= preco_compra:
                        troco = pagamento - preco_compra
                        print(f'Seu troco é de R$ {troco} \nObrigado pela compra, volte sempre!')
                        menu()
                tabela()
                menu()

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
menu()