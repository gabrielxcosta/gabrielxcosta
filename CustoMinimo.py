from VeetorOrdenado import VetorOrdenado

class CustoMinino:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.achou = False
        
    def buscar(self, atual):
        print('\nAtual: {}'.format(atual.nome))
        atual.visitado = True
        
        if atual == self.objetivo:
            self.achou = True
        else:
            self.fronteira = VetorOrdenado(len(atual.adjacentes))
            for a in atual.adjacentes:
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.inserir(a.cidade)
            self.fronteira.mostrar()
            if self.fronteira.getPrimeiro() != None:
                CustoMinino.buscar(self, self.fronteira.getPrimeiro())
                
from Mapa import Mapa
mapa = Mapa()

CUSTO = CustoMinino(mapa.R123)
CUSTO.buscar(mapa.O103)
                