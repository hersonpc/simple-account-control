import random


class Cliente:

    def __init__(self, nome, telefone, codigo = 0):
        if(codigo is None or codigo <= 0):
            codigo = self.gerar_num_cliente()
        self._id = codigo
        self._nome = nome[:50].strip().upper()
        self._telefone = telefone.strip()
        self._conta = {}

    
    def gerar_num_cliente(self):
        return random.randint(1000,99999)


    def getID(self):
        return self._id


    def getNome(self):
        return self._nome.upper()


    def getConta(self):
        return self._conta


    def setConta(self, conta):
        self._conta = conta
        return self