
def z_algorithm(text, pattern):
    # Concatenar el patrón y el texto con un carácter especial entre ellos.
    concat_string = pattern + "$" + text
    n = len(concat_string)

    # Inicializar el Z-array con ceros.
    z = [0] * n

    # Inicializar los índices de los bordes izquierdo y derecho del substring coincidente.
    left, right = 0, 0

    for i in range(1, n):
        # Caso 1: El índice i está fuera del rango de [left, right], por lo que no podemos usar los valores previamente calculados.
        if i > right:
            left, right = i, i
            while right < n and concat_string[right - left] == concat_string[right]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            # Caso 2: El índice i está dentro del rango [left, right], por lo que podemos usar los valores previamente calculados.
            k = i - left
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                left = i
                while right < n and concat_string[right - left] == concat_string[right]:
                    right += 1
                z[i] = right - left
                right -= 1

    # Buscar las ocurrencias del patrón en el Z-array.
    occurrences = []
    for i in range(n):
        if z[i] == len(pattern):
            # Agregar la posición de inicio de la ocurrencia.
            occurrences.append(i - len(pattern) - 1)

    return occurrences


# Ejemplo de uso:
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
result = z_algorithm(text, pattern)
print("Ocurrencias del patrón en el texto:", result)
