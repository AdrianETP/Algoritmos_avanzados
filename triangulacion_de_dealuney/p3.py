import math


def distancia(centro, punto):
    return math.sqrt((punto.x - centro[0])**2 + (punto.y - centro[1])**2)


def dentroTriangulo(puntos, triangulos):
    respuesta = []
    for triangulo in triangulos:
        for punto in puntos:
            if triangulo.radio >= distancia(triangulo.centro, punto):
                respuesta.append(triangulo)
                break
    return respuesta
