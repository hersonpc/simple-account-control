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
        self._conta_selecionada = 0
        self._filename = 'database.bin.gz'
        # self.store(True) # Criar dados de demostracao automaticamente...
        self.load()


    def store(self, seed = False):
        if(seed):
            # populando com dados de demostracao...
            clientes = [
                {   "TIPO": "COMUM", 
                    "SALDO_INI": 380.00, 
                    "CADASTRO": Cliente("Joao da Silva Filho", "(62) 98001-0001") 
                },
                {   "TIPO": "COMUM", 
                    "SALDO_INI": 50.00, 
                    "CADASTRO": Cliente("Maria das gracas meneguel", "(62) 98022-2222") 
                },
                {   "TIPO": "ESPECIAL", 
                    "SALDO_INI": 250000.00, 
                    "LIMITE": 1000000, 
                    "CADASTRO": Cliente("Silvio Santos", "(11) 98000-0000") 
                },
                {   "TIPO": "COMUM", 
                    "SALDO_INI": 10.00, 
                    "CADASTRO": Cliente("Getulio Vargas", "(11) 98044-4444") 
                },
                {   "TIPO": "ESPECIAL", 
                    "SALDO_INI": 500000, 
                    "LIMITE": 300000, 
                    "CADASTRO": Cliente("Paulo Guedes", "(11) 98000-0001") 
                }
            ]
            
            for cliente in clientes:
                if(cliente["TIPO"] == "COMUM"):
                    conta = Conta(cliente_id = cliente["CADASTRO"].getID(), saldo = cliente["SALDO_INI"])
                elif(cliente["TIPO"] == "ESPECIAL"):
                    conta = ContaEspecial(cliente_id = cliente["CADASTRO"].getID(), saldo = cliente["SALDO_INI"]).limite(cliente["LIMITE"])
                self._dataset["CLIENTES"].append(cliente["CADASTRO"])
                self._dataset["CONTAS"].append(conta)

        # salvar em arquivo binario compactado...
        with open(self._filename, 'wb') as fp:
            fp.write(zlib.compress(pickle.dumps(self._dataset, pickle.HIGHEST_PROTOCOL),9))
        
        return self


    def load(self):
        self._dataset = { 
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
            self.store()


    def setContaSelecionada(self, num_conta):
        self._conta_selecionada = num_conta
        return self

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


    def nova_conta(self):
        print_center("Cadastrar nova conta\n")
        print_center("="*80)

        nome_cliente = None
        telefone_cliente = None
        tipo_cliente = None
        limite_cliente = 0

        nome_cliente = raw_input("Nome do cliente: ")[:50].strip().upper()
        if(len(nome_cliente) <= 3):
            raw_input("\nO nome informado e invalido!")
            return
        telefone_cliente = raw_input("Num. telefone: ")[:15].strip()
        if(len(telefone_cliente) <= 8):
            raw_input("\nO telefone informado e invalido!")
            return

        tipo_cliente = raw_input("Qual a categoria deste cliente? [C]omun ou [E]special: ")[:1].strip().upper()
        if((tipo_cliente != "C") and (tipo_cliente != "E")):
            raw_input("\nO tipo informado e invalido!")
            return
        if(tipo_cliente == "E"):
            limite_cliente = float(raw_input("Qual limite bancario deste cliente? $ ")[:15].strip())
            if((limite_cliente <= 0) or (limite_cliente > 10000)):
                raw_input("\nO limite informado e invalido (o max. permitido e $ 10.000)!")
                return


        novo_cliente = Cliente(nome = nome_cliente, telefone = telefone_cliente)
        num_cadastro_cliente = novo_cliente.getID()
        if(tipo_cliente == "C"):
            nova_conta = Conta(cliente_id = num_cadastro_cliente)
        elif(tipo_cliente == "E"):
            nova_conta = ContaEspecial(cliente_id = num_cadastro_cliente)
            nova_conta.limite(limite_cliente)

        self._dataset["CLIENTES"].append(novo_cliente)
        self._dataset["CONTAS"].append(nova_conta)
        
        # persistir dados
        self.store()

        self.cabecalho_tela(nova_conta, novo_cliente)
        print_center("Cliente cadastrado com sucesso!\n\n")
        print_center("Codigo de cliente: {:8d}".format( nova_conta.getClienteID() ))
        print_center("Numero conta: {:8d}\n\n\n".format( nova_conta.getNumero() ))

        raw_input("\nPressione [ENTER] para voltar ao menu.")
        return


    def listar_contas(self):
        print_center("Relatorio das contas cadastradas")
        print_center("="*73)
        print_center("| {:6s} | {:30s} | {:12s} | {:12s} |".format("COD", "NOME DO CLIENTE", "NUM. CONTA", "SALDO DISP."))
        print_center("|-{:6s}-+-{:30s}-+-{:12s}-+-{:12s}-|".format("-"*6, "-"*30, "-"*12, "-"*12))
        for conta in self._dataset["CONTAS"]:
            cliente = self.findClienteByID(conta.getClienteID())
            print_center("| {:6d} | {:30s} | {:12d} | {:12.2f} |".format(
                    cliente.getID(), 
                    cliente.getNome(), 
                    conta.getNumero(), 
                    conta.getSaldoDisponivel()
                )
            )
        print_center("="*73)
        return


    def gerar_extrato(self, conta, cliente):
        self.cabecalho_tela(conta, cliente)
        print_center("Extrato de movimentacoes\n")

        conta.extrato()
        raw_input("\n\nPressione [ENTER] para voltar ao menu.")
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

        self.setContaSelecionada(num_conta)
        return conta


    def cabecalho_tela(self, conta, cliente):
        limpar_tela()
        print_center("DETALHAMENTO DE CONTA")
        print("-"*80)
        print("CONTA SELECIONADA.: [ {:6d} ]".format(conta.getNumero())+" "*18+"SALDO ATUAL: $ [ {:12.2f} ]".format(conta.getSaldoDisponivel()))
        print("PROPRIETARIO......: [ {:55s} ]".format(cliente.getNome()))
        print("-"*80+"\n")


    def menu_conta(self, num_conta = -1):
        limpar_tela()

        conta = None
        if(self._conta_selecionada > 0):
            conta = self.findConta(self._conta_selecionada)
        elif(num_conta > 0):
            conta = self.findConta(num_conta)

        print(self._conta_selecionada, num_conta)

        if((conta is None) or (conta == {}) or (conta == [])):
            raw_input("\nA conta informada e invalida ou nao foi localizada.")
            return

        self.setContaSelecionada(conta.getNumero()) # forca atualizar...

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