from conta import Conta


class ContaEspecial(Conta):
    
    def __init__(self, cliente_id, codigo = 0, saldo = 0):
        self._limite = 0
        super(ContaEspecial, self).__init__(cliente_id, codigo, saldo)
        # super().__init__(numero, saldo) # Python 3


    def getSaldoDisponivel(self):
        return self._saldo + self._limite
    
    
    def limite(self, valor):
        self._limite = valor
        self.historico("LIMITE", valor, "REALIZADO")
        return self