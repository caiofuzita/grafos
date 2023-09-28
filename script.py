# Classe para representar um grafo
class Grafo:
    def __init__(self, vertices):
        self.V = vertices  # Número de vértices
        self.grafo = []  # Lista padrão para armazenar o grafo

    # Função para adicionar uma aresta ao grafo
    def add_aresta(self, u, v, w):
        self.grafo.append([u, v, w])

    # Função utilitária para encontrar o conjunto de um elemento i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Função que une dois conjuntos de x e y
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        # Anexa a árvore de menor classificação sob a raiz da árvore de alta classificação
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot

        # Se as classificações são iguais, faça um como raiz e aumente sua classificação em um
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # Função principal para construir o MST usando o algoritmo de Kruskal
    def kruskal_mst(self):
        resultado = []  # Armazena o MST resultante

        i = 0  # Índice usado para arestas classificadas
        e = 0  # Índice usado para resultado[]

        # Passo 1: Classifique todas as arestas em ordem não decrescente de seu peso.
        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        parent = []
        rank = []

        # Crie conjuntos individuais V com classificação 0
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.grafo[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                resultado.append([u, v])
                self.union(parent, rank, x, y)

        return resultado

# Criação dos vértices
g = Grafo(4)
# Criação das arestas com peso
g.add_aresta(0, 1, 10)
g.add_aresta(0, 2, 6)
g.add_aresta(0, 3, 5)
g.add_aresta(1, 3, 15)
g.add_aresta(2, 3, 4)

resultado = g.kruskal_mst()

print("Arestas no MST")
for u,v in resultado:
    print("%d -- %d" % (u,v))
