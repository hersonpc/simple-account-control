from conta import Conta
# from interfaceBancaria import ContaBancaria

class ContaEspecial(Conta):
    
    def __init__(self, numero, saldo, cliente_id):
        self._limite = 0
        super(ContaEspecial, self).__init__(numero, saldo, cliente_id)
        # super().__init__(numero, saldo) # Python 3


    def getSaldoDisponivel(self):
        return self._saldo + self._limite
    
    
    def limite(self, valor):
        self._limite = valor
        self.historico("LIMITE", valor, "REALIZADO")
        return self