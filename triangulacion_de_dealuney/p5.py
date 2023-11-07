from itertools import count
import matplotlib.pyplot as plt
import numpy as np
import math
import objects


def graficar_puntos(puntos):
    for p in puntos:
        plt.plot(p.x, p.y, 'ro')


def graficar_triangulo(p1, p2, p3):
    plt.plot([p1.x, p2.x, p3.x, p1.x], [p1.y, p2.y, p3.y, p1.y], '-')


def circuncentro(p1, p2, p3):
    d = 2 * (p1.x * (p2.y - p3.y) + p2.x *
             (p3.y - p1.y) + p3.x * (p1.y - p2.y))
    ux = ((p1.x**2 + p1.y**2) * (p2.y - p3.y) + (p2.x**2 + p2.y**2)
          * (p3.y - p1.y) + (p3.x**2 + p3.y**2) * (p1.y - p2.y)) / d
    uy = ((p1.x**2 + p1.y**2) * (p3.x - p2.x) + (p2.x**2 + p2.y**2)
          * (p1.x - p3.x) + (p3.x**2 + p3.y**2) * (p2.x - p1.x)) / d
    return objects.Punto(ux, uy)


def mostrar_grafico():
    plt.show()
