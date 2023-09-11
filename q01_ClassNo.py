class No:
    def __init__(self, valor):
        self.valor = No(valor)
        self.esquerda = None
        self.direita = None

