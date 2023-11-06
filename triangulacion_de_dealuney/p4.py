import matplotlib.pyplot as plt
import objects


def equal_segments(seg_1, seg_2):
    point1_seg1 = (seg_1.A.x, seg_1.A.y)
    point2_seg1 = (seg_1.B.x, seg_1.B.y)
    point1_seg2 = (seg_2.A.x, seg_2.A.y)
    point2_seg2 = (seg_2.B.x, seg_2.B.y)

    # Revisar si los segmentos son iguales
    if point1_seg1 == point1_seg2 and point2_seg1 == point2_seg2:
        return True

    if point1_seg1 == point2_seg2 and point2_seg1 == point1_seg2:
        return True

    return False


def unique_segments(triangles):
    segments = []
    for triangle in triangles:
        segments += triangle.lados

    different_segments = [False for i in range(len(segments))]

    for i in range(len(segments) - 1):
        for j in range(i + 1, len(segments)):
            # Si los segments son iguales, removerlos
            if equal_segments(segments[i], segments[j]):
                different_segments[i] = True
                different_segments[j] = True

    # Obtener todos los segments en false
    different_segments = [
        segments[i] for i in range(len(different_segments))
        if different_segments[i] == False
    ]

    # Imprimir todos los segments diferentes

    return different_segments
