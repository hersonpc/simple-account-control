###############################################################################
##  Instituicao.: UNIVERSIDADE ESTACIO DE SA
##  Curso.......: CIENCIA DE DADOS E BIG DATA ANALYTICS
##  Disciplina..: PRATICA E LABORATORIO II
###############################################################################
##  Aluno.......: HERSON PEREIRA CORDEIRO DE MELO (hersonpc@gmail.com)
##  Matricula...: 201908093609
##  Data........: 2020-04-27
##  GIT.........: https://github.com/hersonpc/simple-account-control
###############################################################################


from banco import Banco
from cliente import Cliente
from utils import limpar_tela, print_center, sair_app


def exibir_contas():
    limpar_tela()
    banco.listar_contas()
    try:
        num_conta = int(raw_input("\nDigite o num. da conta para acessa-la \nou pressione [ENTER] para voltar ao menu.\n\nOpcao: ")[:10])
    except:
        return
    banco.menu_conta(num_conta)
    return


def cadastrar_conta():
    limpar_tela()
    banco.nova_conta()
    return

def entrar_menu_conta():
    limpar_tela()
    print_center("MENU DE CONTA\n")
    conta = None
    try:
        num_conta = int(raw_input("Informe o numero da conta: "))
    except:
        num_conta = 0

    conta = banco.selecionarConta(num_conta)
    if(conta is not None):
        print(conta)
        banco.menu_conta()
    return


def menu():
    limpar_tela()
    print("Selecione uma das opcoes listadas abaixo e informe o codigo:")
    print("="*80)
    opcoes = [
		{ "id": 1, "desc": "Criar conta"},
		{ "id": 2, "desc": "Relatorio de contas cadastradas"},
		{ "id": 3, "desc": "Acessar uma conta"},
		{ "id": 9, "desc": "Sair do aplicativo"},
	]
    for op in opcoes:
        print("  [{:1d}] - {:20s}".format(op["id"], op["desc"].upper()))
    print("="*80)

    try:
        opcao = int(raw_input("\nOpcao: ")[:1])
    except:
        menu()
        return

    if(opcao == 9):
        sair_app()
    elif(opcao == 1):
        cadastrar_conta()
    elif(opcao == 2):
        exibir_contas()
    elif(opcao == 3):
        entrar_menu_conta()

    menu()
    return


## inicializacao ########################
limpar_tela()
banco = Banco()
menu()
