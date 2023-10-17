class Grafo:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]

    def agregar_arista(self, src, dest):
        self.adj[src].append(dest)
        self.adj[dest].append(src)

    def colorear_greedy(self):
        resultado = [-1] * self.V
        for u in range(self.V):
            # +1 para los índices de colores de 1 a V
            disponible = [True] * (self.V + 1)
            for v in self.adj[u]:
                if resultado[v] != -1:
                    disponible[resultado[v]] = False
            for c in range(1, self.V + 1):
                if disponible[c]:
                    resultado[u] = c
                    break
        print("Colores asignados usando el algoritmo Greedy básico:")
        for u in range(self.V):
            print(f"Nodo {u} --> Color {resultado[u]}")

    def colorear_welsh_powell(self):
        grados = [(i, len(self.adj[i])) for i in range(self.V)]
        grados.sort(key=lambda x: x[1], reverse=True)
        resultado = [-1] * self.V
        color = 1
        for i in range(self.V):
            u = grados[i][0]
            if resultado[u] == -1:
                resultado[u] = color
                prohibidos = [i for i in self.adj[u]]
                for v in range(u, len(grados)):
                    if resultado[v] == -1 and v not in prohibidos:
                        resultado[v] = color
                        prohibidos = prohibidos + self.adj[v]
                color += 1

        print("Colores asignados usando el algoritmo Welsh-Powell:")
        for u in range(self.V):
            print(f"Nodo {u} --> Color {resultado[u]}")

    def es_seguro(self, v, color, resultado):
        for u in self.adj[v]:
            if resultado[u] == color:
                return False
        return True

    def colorear_branch_and_bound_util(self, m, resultado, v):
        if v == self.V:
            return True

        for color in range(1, m + 1):
            if self.es_seguro(v, color, resultado):
                resultado[v] = color
                if self.colorear_branch_and_bound_util(m, resultado, v + 1):
                    return True
                resultado[v] = 0

    def colorear_branch_and_bound(self, m):
        resultado = [0] * self.V
        if not self.colorear_branch_and_bound_util(m, resultado, 0):
            print("No es posible colorear el grafo con los colores dados.")
            return False

        print("Colores asignados usando Branch and Bound:")
        for v in range(self.V):
            print(f"Nodo {v} --> Color {resultado[v]}")
        return True


g = Grafo(5)
g.agregar_arista(0, 1)
g.agregar_arista(0, 2)
g.agregar_arista(1, 3)
g.agregar_arista(2, 4)

g.colorear_greedy()
g.colorear_welsh_powell()
g.colorear_branch_and_bound(10)
