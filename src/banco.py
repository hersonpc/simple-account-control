import pickle
import cPickle 
import zlib
from utils import limpar_tela, print_center
from cliente import Cliente
from conta import Conta
from conta_especial import ContaEspecial

class Banco(object):
    
    def __init__(self):
        self._dataset = { 
            "CLIENTES": [], 
            "CONTAS": []
        }
        self._conta_selecionada = []
        self._filename = 'database.gz'
        # self.store(True)
        self.load()


    def store(self, seed = False):
        if(seed):
            self._dataset["CLIENTES"].append(Cliente(32100, "Joaozinho Silva", "(62) 98001-0001"))
            self._dataset["CLIENTES"].append(Cliente(32101, "Maria Souza", "(62) 98022-2222"))
            self._dataset["CLIENTES"].append(Cliente(32102, "Getulio Vargas", "(11) 98044-4444"))
            self._dataset["CLIENTES"].append(Cliente(10900, "Paulo Guedes", "(11) 98088-3210"))
            self._dataset["CLIENTES"].append(Cliente(10800, "Silvio Santos", "(11) 98000-0000"))

            self._dataset["CONTAS"].append(Conta(1011, 1000, 32100))
            self._dataset["CONTAS"].append(Conta(1022, 0, 32101))
            self._dataset["CONTAS"].append(Conta(1026, 0, 32102))

            self._dataset["CONTAS"].append(ContaEspecial(7999,  10000, 10800).limite(100).limite(3500).limite(1000000))
            self._dataset["CONTAS"].append(ContaEspecial(8000, 500000, 10900).limite(1000000))

        with open(self._filename, 'wb') as fp:
            fp.write(zlib.compress(pickle.dumps(self._dataset, pickle.HIGHEST_PROTOCOL),9))
        
        return self


    def load(self):
        # print("LOAD-"*5)
        self._dataset["CONTAS"] = { 
            "CLIENTES": [], 
            "CONTAS": []
        }
        raw_data = -1
        try:
            with open(self._filename, "rb") as f:
                raw_data = f.read()
                if(len(raw_data) > 0):
                    payload = cPickle.loads(zlib.decompress(raw_data))
                    self._dataset = payload
                f.close()
        except Exception as e:
            raise


    def findClienteByID(self, id):
        for cliente in self._dataset["CLIENTES"]:
            if(cliente.getID() == id):
                return cliente
        return {}


    def findConta(self, num_conta):
        for conta in self._dataset["CONTAS"]:
            if(conta.getNumero() == num_conta):
                return conta
        return {}


    def listar_contas(self):
        print_center("="*64)
        print_center("| {:30s} | {:12s} | {:12s} |".format("NOME DO CLIENTE", "CONTA", "SALDO DISP."))
        print_center("| {:30s} | {:12s} | {:12s} |".format("-"*30, "-"*12, "-"*12))
        for conta in self._dataset["CONTAS"]:
            cliente = self.findClienteByID(conta.getClienteID())
            print_center("| {:30s} | {:12d} | {:12.2f} |".format(
                cliente.getNome(), 
                conta.getNumero(), 
                conta.getSaldoDisponivel()))
        print_center("="*64)
        raw_input("\nPressione [ENTER] para voltar ao menu.")


    def gerar_extrato(self, conta, cliente):
        self.cabecalho_tela(conta, cliente)
        print_center("Extrato de movimentacoes\n")

        conta.extrato()
        raw_input()
        return


    def registrar_movimentacao(self, conta, cliente):
        self.cabecalho_tela(conta, cliente)
        print_center("Registro de movimentacoes\n")

        tipo_operacao = raw_input("Deseja fazer um [D]eposito ou um [S]aque? ")[:1]
        if((tipo_operacao.upper() != "D") and (tipo_operacao.upper() != "S")):
            raw_input("\nTipo de operacao selecionado e invalido!")
            return
        valor_operacao = float(raw_input("Qual valor a ser movimentado? $ ")[:15])
        if(valor_operacao <= 0):
            raw_input("\nValor para a operacao e invalido!")
            return

        if((tipo_operacao.upper() == "D")):
            conta.deposito(valor_operacao)
        elif((tipo_operacao.upper() == "S")):
            conta.saque(valor_operacao)
        
        # persistir dados
        self.store()

        self.cabecalho_tela(conta, cliente)
        print_center("Registro de movimentacoes\n")
        raw_input("\n Operacao realizada com sucesso!")
        return


    def alterar_limite(self, conta, cliente):
        self.cabecalho_tela(conta, cliente)
        print_center("Alteracao de limites\n")
        if(type(conta) is not ContaEspecial):
            print_center("Esta conta nao possui esta opcao de alteracao de limites!")
            raw_input("\n\nPressione [ENTER] para voltar para o menu.")
            return

        valor_limite = float(raw_input("Qual valor do novo limite? $ ")[:15])
        if(valor_limite < 0):
            raw_input("\nValor para a operacao e invalido!")
            return

        conta.limite(valor_limite)

        # persistir dados
        self.store()

        self.cabecalho_tela(conta, cliente)
        print_center("Alteracao de limites\n")
        print_center("Operacao realizada com sucesso!")
        raw_input("\n\nPressione [ENTER] para voltar para o menu.")
        return


    def selecionarConta(self, num_conta):
        conta = None
        if(num_conta > 0):
            conta = self.findConta(num_conta)

        if(conta is None):
            raw_input("\nA conta informada e invalida ou nao foi localizada.")
            return

        self._conta_selecionada = num_conta
        return conta


    def cabecalho_tela(self, conta, cliente):
        limpar_tela()
        print_center("DETALHAMENTO DE CONTA")
        print("-"*80)
        print("CONTA SELECIONADA.: [ {:6d} ]".format(conta.getNumero())+" "*18+"SALDO ATUAL: $ [ {:12.2f} ]".format(conta.getSaldoDisponivel()))
        print("PROPRIETARIO......: [ {:55s} ]".format(cliente.getNome()))
        print("-"*80+"\n")


    def menu_conta(self):
        limpar_tela()

        conta = None
        if(self._conta_selecionada > 0):
            conta = self.findConta(self._conta_selecionada)

        if((conta is None) or (conta == {}) or (conta == [])):
            raw_input("\nA conta informada e invalida ou nao foi localizada.")
            return

        cliente_id = conta.getClienteID()
        cliente = self.findClienteByID(cliente_id)

        self.cabecalho_tela(conta, cliente)
        print("Selecione uma das opcoes listadas abaixo e informe o codigo:")
        print("="*80)
        opcoes = [
            { "id": 1, "desc": "Exibir extrato"},
            { "id": 2, "desc": "Registrar movimentaco"},
            { "id": 3, "desc": "Alterar limite"},
            { "id": 9, "desc": "Voltar para menu principal"},
        ]
        for op in opcoes:
            print("  [{:1d}] - {:20s}".format(op["id"], op["desc"].upper()))
        print("="*80)

        try:
            opcao = int(raw_input("Opcao: ")[:1])
        except:
            self.menu_conta()
            return

        if(opcao == 9):
            self._conta_selecionada = -1
            return
        elif(opcao == 1):
            self.gerar_extrato(conta, cliente)
        elif(opcao == 2):
            self.registrar_movimentacao(conta, cliente)
        elif(opcao == 3):
            self.alterar_limite(conta, cliente)

        self.menu_conta()
        return