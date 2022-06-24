import numpy as np

grafo = {"b1":{"b2": 6, "c2":3},
         "b2":{"b4": 3},
         "b3":{"b1": 4, "b4": 7},
         "b4":{"o109": 7},
         "c1":{"c3": 8},
         "c2":{"c1": 4},
         "c3":{},
         "mail":{},
         "o103":{"ts": 8, "b3": 4, "o109": 12},
         "o109":{"o111": 4, "o119": 16},
         "o111":{},
         "o119":{"storage": 7, "o123": 9},
         "o123":{"r123": 4, "o125": 4},
         "o125":{},
         "r123":{},
         "storage":{},
         "ts":{"mail": 6}
         }

S = 0
aux = None
s = np.Infinity

for Vizinhos in grafo.keys():
    print("Vizinhos:", grafo[Vizinhos].keys(), end = " ")
    for Peso in grafo[Vizinhos]:
        if(grafo[Vizinhos][Peso] < s):
            aux = grafo[Vizinhos][Peso]
        print("| Peso:", grafo[Vizinhos][Peso], end = " ")
    print("\nMenor caminho é por:", aux)
    print("\n")