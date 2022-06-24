from Fila import Fila

class Largura:
    def __init__(self,inicio, objetivo):
        self.inicio = inicio
        self.inicio.visitado = True
        self.objetivo = objetivo
        self.fronteira =  Fila(20)
        self.fronteira.enfileirar(inicio)
        self.achou = False
        
    def buscar(self):
        primeiro = self.fronteira.getPrimeiro()
        print('Primeiro: {}'.format(primeiro.nome)) 
        if primeiro == self.objetivo:
            self.achou = True
            print('O objetivo {} foi encontrado!!!'.format(primeiro.nome))
        else:
            self.fronteira.desenfileirar()
            print('Desenfileirando o primeiro da fila...')
            for a in primeiro.adjacentes:
                print('Verificando se já visitado : {}'.format(a.cidade.nome))
                if a.cidade.visitado == False:
                    a.cidade.visitado = True
                    self.fronteira.enfileirar(a.cidade)
            if self.fronteira.numeroElementos > 0:
                Largura.buscar(self)
         
from Mapa import Mapa
mapa = Mapa()

from Mapa import Mapa
mapa = Mapa()

largura = Largura(mapa.O103, mapa.R123)
largura.buscar()
