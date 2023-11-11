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


def generar_permutaciones(n=len(G)):
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
for i, perm in enumerate(permutaciones):
    distances = []
    for j in range(len(G)):
        distances.append(perm[G[j][0]] - perm[G[j][1]])
    print(f'Permutación {i+1}: {perm}')
    print(max(distances))
