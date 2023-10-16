def manacher(s):
    # Paso 1: Transformación de la cadena
    t = '#'.join('^{}$'.format(s))

    # Longitud de la cadena transformada
    n = len(t)

    # Arreglo para almacenar información sobre los palíndromos
    P = [0] * n

    # Posición del centro y extremo derecho del palíndromo más a la derecha
    C, R = 0, 0

    # Iteramos a través de la cadena transformada
    for i in range(n):
        # Si i está dentro del palíndromo más a la derecha encontrado hasta ahora
        if i <= R:
            # Usamos simetría para encontrar un valor inicial para P[i]
            mirror = C - (i - C)
            P[i] = min(R - i, P[mirror])

        # Expandimos el palíndromo desde la posición actual
        a, b = i + (1 + P[i]), i - (1 + P[i])
        while a < n and b >= 0 and t[a] == t[b]:
            current_palindrome = t[b:a+1]
            P[i] += 1
            a += 1
            b -= 1

        # Si el palíndromo actual se extiende más allá de R, actualizamos R y C
        if i + P[i] > R:
            C, R = i, i + P[i]

        print("i: ", i, ", R: ", R, "P[i]:", P[i])
    # Encontrar el palíndromo más largo y su posición en la cadena original
    max_len = max(P)
    center_index = P.index(max_len)
    # Posición en la cadena original
    start_index = (center_index - max_len) // 2

    # Extraemos el palíndromo más largo de la cadena original
    longest_palindrome = s[start_index:start_index + max_len]

    return longest_palindrome


# Ejemplo de uso
cadena = "babad"
resultado = manacher(cadena)
print("La subcadena palindrómica más larga es:", resultado)
