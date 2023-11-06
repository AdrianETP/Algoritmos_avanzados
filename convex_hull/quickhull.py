import matplotlib.pyplot as plt
import numpy as np
import math


def quickhull(points):
    # Función recursiva para encontrar el casco convexo
    def find_hull(points, p1, p2):
        # Caso base: si no hay puntos, devuelve una lista vacía
        if not points:
            return []
        # Encuentra el punto más alejado del segmento (p1, p2)
        max_dist = -1
        farthest_point = None
        for point in points:
            d = distance(p1, p2, point)
            if d > max_dist:
                max_dist = d
                farthest_point = point
        # Divide los puntos en dos subconjuntos y llama recursivamente a find_hull
        convex_hull = []
        convex_hull.extend(find_hull([point for point in points if orientation(
            p1, farthest_point, point) == 1], p1, farthest_point))
        convex_hull.append(farthest_point)
        convex_hull.extend(find_hull([point for point in points if orientation(
            farthest_point, p2, point) == 1], farthest_point, p2))
        return convex_hull

    # Función para determinar la orientación de tres puntos
    def orientation(p, q, r):
        val = (float(q[1] - p[1]) * (r[0] - q[0])) - \
            (float(q[0] - p[0]) * (r[1] - q[1]))
        if val > 0:
            return 1  # Orientación en sentido horario
        elif val < 0:
            return -1  # Orientación en sentido antihorario
        else:
            return 0  # Los puntos son colineales

    # Función para calcular la distancia entre un punto y un segmento
    def distance(p1, p2, p3):
        return abs((p3[0] - p1[0]) * (p2[1] - p1[1]) - (p3[1] - p1[1]) * (p2[0] - p1[0]))

    # Caso base: si hay menos de 3 puntos, no hay necesidad de calcular la envolvente convexa
    if len(points) < 3:
        return points

    # Ordena los puntos por coordenada x
    points.sort(key=lambda x: x[0])

    # Encuentra la envolvente convexa en los dos lados del segmento formado por los puntos primero y último
    convex_hull = []
    convex_hull.extend(find_hull(points, points[0], points[-1]))
    convex_hull.extend(find_hull(points, points[-1], points[0]))

    # Elimina duplicados si los hay y devuelve la envolvente convexa
    return list(set(convex_hull))


# Ejemplo de uso
points = [(0, 0), (1, 3), (2, 2), (4, 4), (0, 2), (3, 1), (1, 1)]
convex_hull = quickhull(points)
print("Envolvente Convexa:", convex_hull)


def draw_hull(puntos, elegidos, start):
    n = len(puntos)               # contamos cuantos puntos son
    colors = np.random.rand(n)    # un arreglo de n colores

    # Un scatter plot grafica:
    # - una lista de puntos, si le pasamos 2 listas con coordenadas x, y
    # - o un solo punto, si le pasamos 2 valores x, y
    # Grafica todos los puntos semitrasparentes, y los elegidos en color solido
    plt.scatter([p[0] for p in elegidos], [p[1] for p in elegidos])
    plt.scatter([p[0] for p in puntos], [p[1] for p in puntos],
                c=colors, alpha=0.5)  # alpaha agrega trasparencia

    plt.scatter(start[0], start[1])  # graficamos el punto de referencia

    # plot grafica segmentos de recta
    # si le pasamos dos listas con coordenadas x, y
    # Para que el ultimo punto conecte con el primero, lo agregamos al final de la lsita
    elegidos.append(elegidos[0])
    # este tipo de linestyle es una linea continua
    plt.plot([p[0] for p in elegidos], [p[1]
             for p in elegidos],  linestyle="-")

    plt.show()


draw_hull(points)
