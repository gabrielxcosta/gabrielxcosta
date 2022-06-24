# Representando o grafo exemplo:
def Vertices(grafo):
    vertices = []
    for vertice in grafo: # Iterando sobre os vértices do grafo
        vertices.append(vertice)
    print(f"Vértices: {vertices}")
    return vertices

def Vizinhos(grafo, vertice):
    vizinhos = []
    for u in grafo[vertice]:
        vizinhos.append(u)
    print(f"Vizinhos do vértice {vertice}: {vizinhos}")

grafo = { "A" : ["B"],
          "B" : ["C", "D"],
          "C" : ["B", "E"],
          "D" : ["A"],
          "E" : ["B"]
        }

Vertices(grafo)
Vizinhos(grafo, 'A')
Vizinhos(grafo, 'B')
Vizinhos(grafo, 'C')
Vizinhos(grafo, 'D')
Vizinhos(grafo, 'E')