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
from conta import Conta
from conta_especial import ContaEspecial
from utils import limpar_tela, print_center, sair_app


def exibir_contas():
    limpar_tela()
    print_center("Relatorio das contas cadastradas")
    banco.listar_contas()
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
		# { "id": 1, "desc": "Criar conta"},
		{ "id": 2, "desc": "Relatorio de contas cadastradas"},
		{ "id": 3, "desc": "Acessar uma conta"},
		{ "id": 9, "desc": "Sair do aplicativo"},
	]
    for op in opcoes:
        print("  [{:1d}] - {:20s}".format(op["id"], op["desc"].upper()))
    print("="*80)

    try:
        opcao = int(raw_input("Opcao: ")[:1])
    except:
        menu()
        return

    if(opcao == 9):
        sair_app()
	# elif(opcao == 1):
	#
    elif(opcao == 2):
        exibir_contas()
    elif(opcao == 3):
        entrar_menu_conta()

    menu()
    return

banco = Banco()
menu()

# cliente = Cliente("Joao Silva", "62 99001-1234")

# conta = cliente.setConta(Conta(3421, 0)).getConta()

# print("\tNome do cliente: " + cliente.getName())
# print("\tConta: " + str(conta.getNumero()))
# print("\tSaldo inicial: " + conta.getSaldo())

# conta.deposito(1000.0)
# conta.saque(2000)
# conta.saque(1000)
# conta.saque(60)
# conta.saque(60)

# conta.extrato()


# print("\n")
# cliente2 = Cliente("Maria Silva", "62 99001-9999")

# conta2 = cliente2.setConta(ContaEspecial(9812, 0, 0)).getConta()

# print("\tNome do cliente: " + cliente2.getName())
# print("\tConta: " + str(conta2.getNumero()))
# print("\tSaldo inicial: " + conta2.getSaldo())

# conta2.deposito(1000.0)
# conta2.limite(100.0)
# conta2.saque(2000)
# conta2.saque(1000)
# conta2.saque(60)
# conta2.saque(60)

# conta2.extrato()