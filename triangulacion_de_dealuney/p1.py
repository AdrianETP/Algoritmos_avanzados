
# seguramente necesitaras estas librerias
import math
import matplotlib.pyplot as plt
import objects

# ----------------------------


# Función para calcular a, b, y c de la ecuación general de una recta que pasa por dos puntos.
def calcular_abc(p1, p2):
    a = p2.y - p1.y  # Diferencia en las coordenadas y
    b = p1.x - p2.x  # Diferencia en las coordenadas x
    c = a * p1.x + b * p1.y  # .y Calculando c usando la fórmula general de la recta
    return a, b, c


# ----------------------------


# Función para calcular el punto de intersección de dos rectas.
def calcular_punto_interseccion(a1, b1, c1, a2, b2, c2):
    # Calculando el determinante para determinar si las rectas son paralelas
    determinante = a1 * b2 - a2 * b1
    if determinante == 0:
        return None  # Si las rectas son paralelas, no hay punto de intersección
    else:
        # Calculando las coordenadas x e y del punto de intersección
        x = (b2 * c1 - b1 * c2) / determinante
        y = (a1 * c2 - a2 * c1) / determinante
        return objects.Punto(x, y)


# ----------------------------


# ----------------------------


# Recibe los puntos, los elegidos y el punto de referencia inicial

# ----------------------------


def find_lowest_x(points):
    # encuentra al punto que tenga la menor y

    lowest_point = points[0]

    for point in points:
        if point.x < lowest_point.x:
            lowest_point = point
    return lowest_point


# ----------------------------


def find_lowest_y(points):
    lowest_point = points[0]
    for point in points:
        if point.y < lowest_point.y:
            lowest_point = point
    return lowest_point


# ----------------------------


def find_highest_x(points):
    highest_point = points[0]
    for point in points:
        if point.x > highest_point.x:
            highest_point = point
    return highest_point


# ----------------------------


def find_highest_y(points):
    highest_point = points[0]
    for point in points:
        if point.y > highest_point.y:
            highest_point = point
    return highest_point


# ----------------------------


def vertices_cuadrado(points):
    # encuentra los puntos que definen el cuadrado
    # en el eje x
    lowest_x = find_lowest_x(points)
    highest_x = find_highest_x(points)
    # en el eje y
    lowest_y = find_lowest_y(points)
    highest_y = find_highest_y(points)

    v1 = objects.Punto(lowest_x.x, lowest_y.y)
    v2 = objects.Punto(highest_x.x, lowest_y.y)
    v3 = objects.Punto(highest_x.x, highest_y.y)
    v4 = objects.Punto(lowest_x.x, highest_y.y)

    return [v1, v2, v3, v4]


# ----------------------------


def draw_hull(puntos, t):
    plt.scatter([p.x for p in puntos], [p.y for p in puntos])
    vertices = vertices_cuadrado(puntos)
    vertices.append(vertices[0])
    plt.plot([v.x for v in vertices], [v.y for v in vertices], linestyle="-")
    t.append(t[0])
    plt.plot([v.x for v in t], [v.y for v in t], linestyle="-")
    plt.show()  # y al final muestra el plot. tadaa.


# ----------------------------

# recibir puntos y retornar un lista de puntos
def BigT(points):
    # calcular vertices del rectangulo
    cuadrado = vertices_cuadrado(points)
# cacluclar m = Mitad de la distancia entre x1 y x2
    x1 = find_lowest_x(points)
    x2 = find_highest_x(points)
    y1 = find_lowest_y(points)
    y2 = find_highest_y(points)
    m = (math.sqrt((x2.x - x1.x)**2 + (y2.y - y1.y)**2)) / 2
# calcular v1 y v2
    v1 = objects.Punto(cuadrado[0].x - m, cuadrado[0].y - 1)
    v2 = objects.Punto(cuadrado[1].x + m, cuadrado[1].y - 1)
# calcular recta v1_a y recta v2_b
    v1_a = calcular_abc(v1, cuadrado[3])
    v2_b = calcular_abc(v2, cuadrado[2])
# calcular v3 con la interseccion de las dos rectas previas
    v3 = calcular_punto_interseccion(v1_a[0], v1_a[1], v1_a[2], v2_b[0], v2_b[1],
                                     v2_b[2])
# graficar
    t = [v1, v2, v3]
    triangle = objects.Triangulo(t)
    return triangle
