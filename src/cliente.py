class Cliente:

    def __init__(self, id, nome, telefone):
        self._id = id
        self._nome = nome[:50]
        self._telefone = telefone
        self._conta = {}

    
    def getID(self):
        return self._id


    def getNome(self):
        return self._nome.upper()


    def getConta(self):
        return self._conta


    def setConta(self, conta):
        self._conta = conta
        return self