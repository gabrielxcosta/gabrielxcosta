class Cidade:
  def __init__(self,nome, distancia):
    self.nome = nome
    self.visitado = False
    self.distancia = distancia
    self.adjacentes = []

  def addCidadeAdjacente(self,cidade):
    self.adjacentes.append(cidade)
    

    