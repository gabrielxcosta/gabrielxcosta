from Cidades import Cidade
from Adjacentes import Adjacente

class Mapa:
  B1 = Cidade("B1", 6)
  B2 = Cidade("B2", 5)  
  B3 = Cidade("B3", 5)    
  B4 = Cidade("B4", 4)
  C1 = Cidade("C1", 8)
  C2 = Cidade("C2", 7)
  C3 = Cidade("C3", 8)
  MAIL = Cidade("MAIL", 6)
  O103 = Cidade("O103", 0)  
  O109 = Cidade(" O109", 3)    
  O111 = Cidade("O111", 4)
  O119 = Cidade("O119", 2)
  O123 = Cidade("O123", 1)
  O125 = Cidade("O125", 2)
  R123 = Cidade("R123", 0)
  STORAGE = Cidade("STORAGE", 3)  
  TS = Cidade("TS", 5) 

  B1.addCidadeAdjacente(Adjacente(C2))
  B1.addCidadeAdjacente(Adjacente(B2))

  B2.addCidadeAdjacente(Adjacente(B4))

  B3.addCidadeAdjacente(Adjacente(B1))
  B3.addCidadeAdjacente(Adjacente(B4))
  
  B4.addCidadeAdjacente(Adjacente(O109))

  C1.addCidadeAdjacente(Adjacente(C3))
  
  C2.addCidadeAdjacente(Adjacente(C1))
  C2.addCidadeAdjacente(Adjacente(C3))
  
  O103.addCidadeAdjacente(Adjacente(TS))
  O103.addCidadeAdjacente(Adjacente(B3))
  O103.addCidadeAdjacente(Adjacente(O109))
  
  O109.addCidadeAdjacente(Adjacente(O111))
  O109.addCidadeAdjacente(Adjacente(O119))
  
  O119.addCidadeAdjacente(Adjacente(STORAGE))
  O119.addCidadeAdjacente(Adjacente(O123))
  
  O123.addCidadeAdjacente(Adjacente(R123))
  O123.addCidadeAdjacente(Adjacente(O125))
  
  TS.addCidadeAdjacente(Adjacente(MAIL))
