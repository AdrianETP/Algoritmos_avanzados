import math


def distancia(centro, punto):
    cx, cy = centro
    return math.sqrt((punto.x - cx)**2 + (punto.y - cy)**2)


def dentroTriangulo(puntos, triangulos):
    respuesta = []
    for triangulo in triangulos:
        for punto in puntos:
            if triangulo.radio >= distancia(triangulo.centro, punto):
                respuesta.append(triangulo)
                break
    return respuesta
