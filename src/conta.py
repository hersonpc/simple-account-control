import pickle
import random
from utils import print_center


class Conta(object):
    
    def __init__(self, cliente_id, codigo = 0, saldo = 0):
        self._historico = []
        if(codigo is None or codigo <= 0):
            codigo = self.gerar_num_conta()
        self._numero = codigo
        self._cliente_id = cliente_id
        self._saldo = float(saldo)
        self.historico("DEP. ABERTURA", saldo, "REALIZADO")


    def gerar_num_conta(self):
        return random.randint(10000,99999)


    def getClienteID(self):
        return self._cliente_id


    def getNumero(self):
        return self._numero
    

    def getSaldoDisponivel(self):
        return self._saldo
    
    
    def getSaldo(self):
        return "$ {:12.2f}".format(self._saldo)
    
    
    def log(self, msg):
        print(" "*50 + " << " + msg)


    def historico(self, operacao, valor, status):
        evento = "| {:15s} | {:12.2f} | {:25s} | {:12.2f} |".format(
            operacao.upper(), 
            valor, 
            status.upper(), 
            self.getSaldoDisponivel())
        self._historico.append(evento)
        return self


    def extrato(self):
        print_center("="*77)
        print_center("| {:15s} | {:12s} | {:25s} | {:12s} |".format("OPERACAO", "VALOR ($)", "STATUS", "SALDO ($)"))
        print_center("|-{:15s}-+-{:12s}-+-{:25s}-+-{:12s}-|".format("-"*15, "-"*12, "-"*25, "-"*12))
        for evento in self._historico:
            print_center(evento)
        print_center("="*77)


    def deposito(self, valor):
        self._saldo += valor
        self.historico("DEPOSITO", valor, "REALIZADO")
        return self


    def saque(self, valor):
        if( (self.getSaldoDisponivel() - valor) < 0):
            self.historico("SAQUE", (valor *-1), "SALDO INSUFICIENTE")
            # return
        else:
            self._saldo -= valor
            self.historico("SAQUE", (valor *-1), "REALIZADO")

        # self.log("\tSaldo atual: " + self.getSaldo())

        return self