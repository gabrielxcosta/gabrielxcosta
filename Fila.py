class Fila:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.cidades = [None] * self.tamanho
        self.inicio = 0
        self.fim = -1
        self.numeroElementos = 0
        
    def enfileirar(self,cidade):
        if not Fila.filacheia(self):    
            if self.fim == self.tamanho -1:
                self.fim = -1
            self.fim += 1
            self.cidades[self.fim] = cidade
            self.numeroElementos += 1
        else:
            print("A fila está cheia")
        
    def desenfileirar(self):
        if not Fila.filavazia(self):     
            temp = self.cidades[self.inicio]
            self.inicio += 1
            if self.inicio == self.tamanho:
                self.inicio = 0
                self.numeroElementos -= 1
                return temp
        else:
            print("A fila está vazia")
            return None
        
    
    def getPrimeiro(self):
        return self.cidades[self.inicio]
    
    def filavazia(self):
        return self.numeroElementos == 0
    
    def filacheia(self):
        return self.numeroElementos == self.tamanho
    





