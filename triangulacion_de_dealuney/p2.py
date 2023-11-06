import matplotlib.pyplot as plt
import numpy as np

# Función para encontrar el centro y el radio del círculo circunscrito


def hacerCirculo(p1, p2, p3):
    # Calcula las longitudes de los lados del triángulo
    a = np.linalg.norm(np.array(p2) - np.array(p3))
    b = np.linalg.norm(np.array(p1) - np.array(p3))
    c = np.linalg.norm(np.array(p1) - np.array(p2))

    # Calcula el semiperímetro del triángulo
    s = (a + b + c) / 2

    # Calcula el radio del círculo circunscrito
    radio = (a * b * c) / (4 * np.sqrt(s * (s - a) * (s - b) * (s - c)))

    # Calcula las coordenadas del centro del círculo
    A = p1[0] - p2[0]
    B = p1[1] - p2[1]
    C = p1[0] - p3[0]
    D = p1[1] - p3[1]
    E = (A * (p1[0] + p2[0]) + B * (p1[1] + p2[1])) / 2
    F = (C * (p1[0] + p3[0]) + D * (p1[1] + p3[1])) / 2
    det = A * D - B * C

    centro_x = (D * E - B * F) / det
    centro_y = (-C * E + A * F) / det

    return (centro_x, centro_y), radio
