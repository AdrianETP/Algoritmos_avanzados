import p1
import objects
import p2
import p3
import p4
import p5
import matplotlib.patches as patches
import matplotlib.pyplot as plt


def lee_archivo(archivo):
    f = open(archivo, "r")
    contenido = f.read()
    f.close()

    lines = contenido.split("\n")
    n = int(lines[0])
    aux = [
        list(map(float, lines[i].split("\t"))) for i in range(1,
                                                              len(lines) - 1)
    ]

    points = []
    for a in aux:
        points.append(objects.Punto(a[0], a[1]))

    return n, points


_, points = lee_archivo('./puntos.txt')
BigTriangle = p1.BigT(points)
vertices_BigTriangle = [BigTriangle.puntos[0],
                        BigTriangle.puntos[1], BigTriangle.puntos[2]]
T = [BigTriangle]

for p in points:
    for t in T:
        circle = p2.hacerCirculo(
            t.puntos[0].show(), t.puntos[1].show(), t.puntos[2].show())
        t.radio = circle[1]
        t.centro = circle[0]

    bad_triangles = p3.dentroTriangulo([p], T)

    unique_segments = p4.unique_segments(bad_triangles)

    for t in bad_triangles:
        T.remove(t)
    for l in unique_segments:
        # Crear un nuevo triángulo con el segmento 'l' y el punto 'p'
        new_triangle = objects.Triangulo([l.A, l.B, p])

        # Añadir el nuevo triángulo a la lista 'T'
        T.append(new_triangle)

    # Graficar la triangulación después de agregar el punto 'p'
    p5.graficar_puntos(points)
    for t in T:
        if not any(punto in vertices_BigTriangle for punto in t.puntos):
            p5.graficar_triangulo(t.puntos[0], t.puntos[1], t.puntos[2])
    p5.mostrar_grafico()

# Remover de T los triángulos que incluyan algún vértice de BigTriangle
vertices_BigTriangle = [BigTriangle.puntos[0],
                        BigTriangle.puntos[1], BigTriangle.puntos[2]]
T = [t for t in T if not any(
    punto in vertices_BigTriangle for punto in t.puntos)]

# Graficar la triangulación sin los círculos
p5.graficar_puntos(points)
for t in T:
    print("Triángulo:")
    for lado in t.lados:
        print(
            f"Segmento de ({lado.A.x}, {lado.A.y}) a ({lado.B.x}, {lado.B.y})")
    p5.graficar_triangulo(t.puntos[0], t.puntos[1], t.puntos[2])
p5.mostrar_grafico()

# Graficar la triangulación con los círculos
p5.graficar_puntos(points)
for t in T:
    p5.graficar_triangulo(t.puntos[0], t.puntos[1], t.puntos[2])
    # Dibujar el círculo para este triángulo
    circle = patches.Circle((t.centro[0], t.centro[1]), t.radio, fill=False)
    plt.gca().add_patch(circle)
p5.mostrar_grafico()
