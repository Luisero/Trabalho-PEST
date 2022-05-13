from time import sleep
from emailSender import enviarEmail
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from clear import clear
from bemvindo import boasVindas

console = Console()
mod_carro = dict()
'''
Modelo:string
Marca: string
Valor de fábrica: float
Para_PCD : string (sim/nao)
Preco: float
Quantidade: int
'''

carros = list()
clear()
boasVindas('Bem vindo!','blue')
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
                modo = inputEscolha('O que deseja fazer? [green][0][green/]Cadastrar [blue][1][blue/]Editar ',escolhas=['0','1'], erro='[on red]Valor inválido! Tente novamente[on red/]')
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

        paraPCD = inputEscolha('Esse carro é para PCD? [green][0]Sim[green/] [blue][1]Não[blue/]',escolhas=['0','1'], erro='Valor inválido! Tente novamente')
        if paraPCD == '0':
            paraPCD='Sim'
        else:
            paraPCD = 'Não'
        preco = 0
        marca = inputText('Qual a marca do carro? ').title()
        modelo = inputAllText('Qual o modelo do carro? ').title()
        #verificar se o modelo já está cadastrado
        igual = True
        while igual:
            if len(carros) != 0:
                for carro in carros:
                    if modelo == carro['Modelo'] and carro['Para_PCD'] == paraPCD:
                        igual = True
                        console.print('[on red]Carro já cadastrado![on red/]')
                        modelo = inputAllText('Qual o modelo do carro? ').title()
                        if paraPCD != carro['Para_PCD'] :
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
        continuar = inputEscolha('Deseja continuar cadastrando carros? [green][0]Sim[green/] [blue][1]Não[blue/]',escolhas=['0','1'], erro='[on red]Valor inválido! Tente novamente.[on red/]')
        if continuar == '0':
            continuar = 's'
            clear()
        else:
            clear()
            continuar = 'n'


def editar():
    carros_pcd = []
    carros_nopcd = []

    for carro in carros: #cria uma lista de carros pcd e de não pcd
        if carro['Para_PCD'] == 'Sim':
            carros_pcd.append(carro)
        else:
            carros_nopcd.append(carro)
    continuar = '0'
    while continuar == '0':
        if len(carros) == 0:
            console.print('[yellow]Nenhum carro para editar.[yellow/]')
            sleep(1)
            clear()
            break
        else:
            clear()
            printCarros(carros)
            
            paraPCD = inputEscolha('Esse carro é para PCD? [green][0]Sim[green/] [blue][1]Não[blue/]',escolhas=['0','1'], erro='Valor inválido! Tente novamente')

            if paraPCD == '0':
                paraPCD='Sim'
            else:
                paraPCD = 'Não'

            if paraPCD == 'Sim' and len(carros_pcd) == 0:
                console.print('[yellow]Nenhum carro para editar.[yellow/]')
                sleep(2)
                clear()
                break
            elif len(carros_nopcd) == 0:
                console.print('[yellow]Nenhum carro para editar.[yellow/]')
                sleep(2)
                clear()
                break
            modelo = inputAllText('Qual o modelo do carro para editar? ').title()
            
            achou = False
            if paraPCD == 'Sim':
                for carro in carros_pcd:
                    if carro['Modelo'] == modelo and carro['Para_PCD'] == paraPCD:
                        achou = True
            
                while not achou:
                    console.print('[on red]Carro não encontrado![on red/]')
                    modelo = inputAllText('Qual o modelo do carro para editar? ').title()
                    for carro in carros_pcd:
                        if carro['Modelo'] == modelo and carro['Para_PCD']:
                            achou = True  
            else:
                for carro in carros_nopcd:
                    if carro['Modelo'] == modelo and carro['Para_PCD'] == paraPCD:
                        achou = True
            
                while not achou:
                    console.print('[on red]Carro não encontrado![on red/]')
                    modelo = inputAllText('Qual o modelo do carro para editar? ').title()
                    for carro in carros_nopcd:
                        if carro['Modelo'] == modelo and carro['Para_PCD']:
                            achou = True  
                
            
            for i,modelo_carro in enumerate(carros):
                if modelo_carro['Modelo'] == modelo and modelo_carro['Para_PCD'] == paraPCD:
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
                    paraPCD = ''
        
        continuar = inputEscolha('Deseja continuar editando carros? [green][0]Sim[green/] [blue][1]Não[blue/]',escolhas=['0','1'], erro='[on red]Valor inválido[on red/]')
    clear()

def consultar(cliente_pcd):
    clear()
    carros_pcd = []
    carros_nopcd = []

    for carro in carros: #cria uma lista de carros pcd e de não pcd
        if carro['Para_PCD'] == 'Sim':
            carros_pcd.append(carro)
        else:
            carros_nopcd.append(carro)
    if cliente_pcd: #se o cliente for pcd
        if len(carros_pcd) == 0:
            console.print('[yellow]Nenhum carro pra comprar.[yellow/]')
        else:
            printCarros(carros_pcd)
            quercomprar = inputEscolha('Quer comprar um carro? [green][0]Sim[green/] [blue][1]Não[blue/]', escolhas=['0','1'], erro='[on red]Valor inválido! Tente novamente [on red/]')
            if quercomprar == '0':
                comprar(carros_pcd)

            else:
                console.print('[yellow]Tudo bem[yellow/]')

    else:#se o cliente não for pcd
        if len(carros_nopcd) == 0:
            console.print('[yellow]Nenhum carro pra comprar.[yellow/]')
        else:
            printCarros(carros_nopcd)
            quercomprar = inputEscolha('Quer comprar um carro? [green][0]Sim[green/] [blue][1]Não[blue/]', escolhas=['0','1'], erro='[on red]Valor inválido! Tente novamente [on red/]')
            if quercomprar == '0':
                comprar(carros_nopcd)
            else:
                console.print('[yellow]Tudo bem[yellow/]')

def comprar(lista_carros):

    modelo = inputAllText('Qual o modelo do carro quer comprar? ').title()
    achou = False

    while not achou:
        for i, carro in enumerate(lista_carros):
            if carro['Modelo'] == modelo:
                achou = True
                quantidade = inputInt('Quantos carros quer comprar? ')
                nova_quant = carro['Quantidade'] - quantidade
                while quantidade <= 0 or nova_quant<0:
                    console.print('[on red]Valor inválido! Tente novamente [on red/]')
                    quantidade = inputInt('Quantos carros quer comprar? ')
                    nova_quant = carro['Quantidade'] - quantidade
                carro['Quantidade'] = nova_quant

                preco = carro['Preco'] * quantidade
                datas = pegarData()
                tamanho_arquivo = len(__file__)
                path = __file__[0: tamanho_arquivo-7]
                num_pedido = 0
                with open(f'{path}pedido.txt', 'r') as f:
                    num_pedido = f.readline()
                    num_pedido = int(num_pedido) + 1
                    with open(f'{path}pedido.txt', 'w') as r:
                        r.write(str(num_pedido))
                #Nota fiscal
                nota_fiscal = Table(title='Nota fiscal')
                nota_fiscal.add_column('Marca')
                nota_fiscal.add_column('Modelo')
                nota_fiscal.add_column('Preço')
                nota_fiscal.add_column('Quantidade')
                nota_fiscal.add_column('Para PCD?')
                nota_fiscal.add_column('Número do pedido.')
                nota_fiscal.add_column('Data')
                nota_fiscal.add_row(carro['Marca'],carro['Modelo'], str(carro['Preco']), str(quantidade), carro['Para_PCD'], str(num_pedido), str(datas['Data']))
                ################################

                res_nota = inputEscolha('Deseja receber a nota fiscal por email? [green][0]Sim[green/] [blue][1]Não[blue/]', erro='[on red]Valor inválido! Digite novamente.[on red/]', escolhas=['0','1'])
                if res_nota == '0':
                    from infos import email, senha # email e senha do remetente
                    email_r = email
                    senha_r = senha
                    mensagem_html = f'''
                    <h1>Compra de carro efetuada!</h1>
                    <h2>Parabéns! Você acaba de adquirir um {carro['Marca']} {carro['Modelo']} </h2> 
                    <p><strong>Informações: </strong></p>
                    <ul style="list-style-type: none;">
                        <li>Marca: <strong>{carro['Marca']}</strong></li>
                        <li>Modelo: <strong>{carro['Modelo']}</strong></li>
                        <li>Preco: <strong>R${carro['Preco']}</strong></li>
                        <li>Quantidade: <strong>{quantidade}</strong></li>
                        <li>Para PCD? <strong>{carro['Para_PCD']}</strong></li>
                        <li>Compra feita no dia <time>{datas['Data']}</time> e na hora <time>{datas['Hora']}</time></li>
                        <li>Número do pedido: <strong>{num_pedido}</strong></li>

                    </ul>

                    <p>Concessionária Sol Quente: saia da sombra com a gente.</p>
                    <p><em><strong>&copy;Concessionária Sol Quente</strong></em></p>
                    '''
                    email_d= inputEmail('Digite seu e-mail para receber a nota fiscal')
                    def enviandoEmail():
                        for i in range(0,1):
                            console.log('Enviando e-mail')
                            enviarEmail(email_r,senha_r, mensagem_html,email_d,'Carro novo para você!')
                            console.log('Email enviado!')

                    with console.status('[green]Carregando[green/]') as e:
                        enviandoEmail()
                    
                    console.print(nota_fiscal)
                    
                else:
                    console.print(nota_fiscal)

                console.log('[on green]Compra confirmada![on green/]')


                break

        if not achou:
                console.print('[on red]Carro não encontrado![on red/]')
                modelo = inputAllText('Qual o modelo do carro comprar? ').title()







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
            if isSpace(res) :
                console.print('[on red]Valor inválido! Tente novamente.[on red/] ')
                res = Prompt.ask(texto)
            else:
                return res
def inputAllText(texto):
  
    res = Prompt.ask(texto).title()
    while True:
            if isSpace(res):
                console.print('[on red]Valor inválido! Tente novamente.[on red/] ')
                res = Prompt.ask(texto)
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

def inputEmail(texto):
    email = ''
    while True:
        email = inputText(texto).lower()

        email = email.split('@')

        while len(email) !=2:
            console.print('[on red]Valor inválido! Tente novamente.[on red/]')
            email = inputText(texto).lower()

            email = email.split('@')

        if len(email) == 2:
            for i in range(0,2):
                email[i] = email[i].split('.com')
            if len(email[1]) == 2 and not isSpace(email[0][0]) and not isSpace(email[1][0]):
                #certo
                return f'{email[0][0]}@{email[1][0]}.com'
            else:
                console.print('[on red]Valor inválido! Tente novamente.[on red/]')



def pegarData():
    import datetime
    date = datetime.datetime.now()

    datastr = date.strftime('%d/%m/%Y')
    horastr = date.strftime('%H:%S')

    datas = {
        "Data": datastr,
        "Hora": horastr
    }
    return datas


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
