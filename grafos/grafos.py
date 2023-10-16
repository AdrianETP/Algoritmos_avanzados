class Grafo:
    def __init__(self) -> None:
        self.graph = {}

    def is_empty(self):
        return self.graph == {}

    def exists(self, u):
        return u in self.graph

    def prim(self, start):
        visited = {node: False for node in self.graph}
        min_spanning_tree = []
        total_cost = 0

        priority_queue = [(0, start)]

        while priority_queue:
            weight, current_node = priority_queue.pop(0)

            if not visited[current_node]:
                visited[current_node] = True
                total_cost += weight
                min_spanning_tree.append((weight, current_node))
                for neighbor, edge_weight in self.graph[current_node]:
                    if not visited[neighbor]:
                        priority_queue.append((edge_weight, neighbor))
            priority_queue.sort()
        return min_spanning_tree, total_cost

    def find(self, parent, node):
        if parent[node] != node:
            parent[node] = self.find(parent, parent[node])
        return parent[node]

    def union(self, parent, rank, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

    def kruskal(self):
        edges = []
        for node in self.graph:
            for neighbor, weight in self.graph[node]:
                edges.append((node, neighbor, weight))
        edges.sort(key=lambda x: x[2])

        min_spanning_tree = []
        total_cost = 0
        parent = {node: node for node in self.graph}
        rank = {node: 0 for node in self.graph}

        for u, v, weight in edges:
            if self.find(parent, u) != self.find(parent, v):
                min_spanning_tree.append((u, v, weight))
                total_cost += weight
                self.union(parent, rank, u, v)

        return min_spanning_tree, total_cost

    def dijkstra(self, start):
        unvisited = list(self.graph)
        shortest_distance = {node: float("infinity") for node in self.graph}
        shortest_distance[start] = 0
        path = {node: "" for node in self.graph}
        path.pop(start)
        current_node = start
        current_distance = shortest_distance[start]
        while unvisited != []:
            shortest_neighbor = ""
            shortest_neighbor_distance = float("infinity")
            for vecinos in self.graph[current_node]:
                value, weight = vecinos
                potential_distance = current_distance + weight
                if potential_distance < shortest_distance[value]:
                    shortest_distance[value] = potential_distance
                    if current_node in path:
                        path[value] = path[current_node] + "+" +\
                            current_node + "(" + str(weight) + ")"
                    else:
                        path[value] = current_node + "(" + str(weight) + ")"
                if potential_distance < shortest_neighbor_distance and value in unvisited:
                    shortest_neighbor_distance = potential_distance
                    shortest_neighbor = value
            unvisited.remove(current_node)
            current_node = shortest_neighbor
            current_distance = shortest_neighbor_distance
        shortest_distance.pop(start)
        for d, v in shortest_distance.items():
            path[d] = path[d] + "= " + str(v)

        return path

    def warshall(self):
        nodos = list(self.graph.keys())
        n = len(nodos)
        conexiones = {nodo: set() for nodo in nodos}

        # Inicializamos las conexiones conocidas entre nodos vecinos
        for i in range(n):
            u = nodos[i]
            for v, _ in self.graph[u]:
                conexiones[u].add(v)

        # Algoritmo de Warshall
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if nodos[j] in conexiones[nodos[i]]:
                        continue
                    if nodos[k] in conexiones[nodos[i]] and nodos[j] in conexiones[nodos[k]]:
                        conexiones[nodos[i]].add(nodos[j])

        return conexiones

    def floyd(self):
        nodos = list(self.graph.keys())
        n = len(nodos)
        distancias = [[float('infinity') for _ in range(n)]
                      for _ in range(n)]
        caminos = [[-1 for _ in range(n)] for _ in range(n)]

        # Inicializamos las distancias conocidas entre nodos vecinos y los caminos intermedios
        for i in range(n):
            distancias[i][i] = 0
            u = nodos[i]
            for v, peso in self.graph[u]:
                j = nodos.index(v)
                distancias[i][j] = peso
                caminos[i][j] = i

        # Algoritmo de Floyd para encontrar las distancias más cortas y los nodos intermedios
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                        distancias[i][j] = distancias[i][k] + \
                            distancias[k][j]
                        caminos[i][j] = k

        return nodos, distancias

    def add_edge(self, u, v, w):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, w))

    def read_from_file(self, file):
        with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                u, v, w = line.strip().split()
                self.add_edge(u, v, int(w))

    def print(self):
        print(self.graph)


g = Grafo()

g.read_from_file("g.txt")
g.print()
print("algoritmo de prim")
print(g.prim('A'))
print("algoritmo de kruskal")
print(g.kruskal())
print("algoritmo de dikstra")
dijkstra = g.dijkstra('A')
for d, v in dijkstra.items():
    print(d, ":", v)

print("algoritmo de walshall")
warshall = g.warshall()
for w, v in warshall.items():
    print(w, " tiene camino a: ", v)
print("Algoritmo de Floyd:")
n, v = g.floyd()
for i in range(len(n)):
    v[i].remove(0)
    print("peso del camino mas corto en", n[i], ": ", min(v[i]))
