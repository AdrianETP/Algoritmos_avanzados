import p1
import objects
import p2
import p3
import p4
import p5


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
T = [BigTriangle]

for t in T:
    circle = p2.hacerCirculo(
        t.puntos[0].show(), t.puntos[1].show(), t.puntos[2].show())
    t.radio = circle[1]
    t.centro = circle[0]

for p in points:
    bad_triangles = p3.dentroTriangulo([p], T)

    unique_segments = p4.unique_segments(bad_triangles)

    for t in bad_triangles:
        T.remove(t)
    for l in unique_segments:
        # Crear un nuevo triángulo con el segmento 'l' y el punto 'p'
        new_triangle = objects.Triangulo([l.A, l.B, p])

        # Añadir el nuevo triángulo a la lista 'T'
        T.append(new_triangle)


p5.graficar_puntos(points)
for t in T:
    p5.graficar_triangulo(t.puntos[0], t.puntos[1], t.puntos[2])
p5.mostrar_grafico()
