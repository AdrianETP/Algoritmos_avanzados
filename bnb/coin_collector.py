import heapq


# calculo upper bound
# se suman los valores de la columna actual para compararlo con el valor maximo actual a partir de una posicion especifica en x,y
# esta estimacion se utiliza en el algoritmo B&B para determinar si vale la pena explorar una rama particular de la busqueda
# si la quota superior de una solucion parcial es menor que el valor de la mejor solucion completa encontrada hasta ahora, esa rama del arbol se ignora

class State:
    def __init__(self, x, y, value, path):
        self.x = x
        self.y = y
        self.value = value
        self.path = path

    def __lt__(self, other):
        return self.value < other.value


def read_matrix_from_file(filename):
    with open(filename, 'r') as f:
        return [[int(x) for x in line.split()] for line in f.readlines()]


def upper_bound(matrix, x, y):
    return sum(matrix[x][y:]) + sum(row[y] for row in matrix[x:])


def branch_and_bound(matrix):
    n = len(matrix)
    m = len(matrix[0])

    pq = []
    heapq.heappush(pq, State(0, 0, matrix[0][0], [(0, 0, matrix[0][0])]))

    max_value = 0
    best_path = None

    while pq:
        current_state = heapq.heappop(pq)

        x, y, value, path = current_state.x, current_state.y, current_state.value, current_state.path

        if value + upper_bound(matrix, x, y) < max_value:
            continue

        if x == n - 1 and y == m - 1:
            if value > max_value:
                max_value = value
                best_path = path

        if x + 1 < n:
            new_value = value + matrix[x + 1][y]
            heapq.heappush(pq, State(x + 1, y, new_value,
                           path + [(x + 1, y, matrix[x + 1][y])]))

        if y + 1 < m:
            new_value = value + matrix[x][y + 1]
            heapq.heappush(pq, State(x, y + 1, new_value,
                           path + [(x, y + 1, matrix[x][y + 1])]))

    if best_path is None:
        return "No hay solución encontrada", 0

    directions = []
    for i in range(1, len(best_path)):
        if best_path[i][0] > best_path[i-1][0]:
            directions.append(f"abajo ({best_path[i][2]})")
        else:
            directions.append(f"derecha ({best_path[i][2]})")

    return ", ".join(directions), max_value


if __name__ == "__main__":
    matrix = read_matrix_from_file("matrix.txt")
    directions, total_value = branch_and_bound(matrix)
    print(f"Solución óptima: {directions}. Total = {total_value}")
