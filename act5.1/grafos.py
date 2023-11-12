import numpy as np
G = [
    (0, 1),
    (1, 2),
    (1, 3),
    (1, 7),
    (1, 8),
    (2, 4),
    (2, 6),
    (4, 5),
    (4, 7),
    (5, 7),
    (6, 7),
]


def generar_permutaciones(n=9):
    array = np.arange(n)  # Crear un array con n elementos
    permutaciones = []  # Lista para almacenar las permutaciones

    for _ in range(100):
        np.random.shuffle(array)  # Mezclar el array
        permutaciones.append(array.copy())  # Añadir la permutación a la lista

    return permutaciones


# Generar 100 permutaciones de un array de 10 elementos
permutaciones = generar_permutaciones()

# Imprimir las permutaciones
smallest_distance_perm = []
smallest_distance = float('inf')
for i, perm in enumerate(permutaciones):
    distances = []
    for j in G:
        a = j[0]
        b = j[1]
        distances.append(abs(perm[a] - perm[b]))
    print(f'Permutación {i+1}: {perm}')
    if max(distances) < smallest_distance:
        smallest_distance_perm = perm
        smallest_distance = max(distances)

print("the smallest distance permutation is: \n",
      smallest_distance_perm, "\n with a distance of: ", smallest_distance)
