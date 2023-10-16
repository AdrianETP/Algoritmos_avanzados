
def build_suffix_array(text):
    # Agregar el carácter especial '$' al final de la cadena (necesario para el algoritmo).
    text += '$'

    # Crear una lista de sufijos, donde cada elemento es una tupla (sufijo, posición inicial).
    suffixes = [(text[i:], i) for i in range(len(text))]

    # Ordenar los sufijos lexicográficamente.
    suffixes.sort(key=lambda x: x[0])

    # Extraer las posiciones iniciales de los sufijos ordenados para obtener el Suffix Array.
    suffix_array = [suffix[1] for suffix in suffixes]

    return suffix_array


# Ejemplo de uso:
text = "banana"
suffix_array = build_suffix_array(text)
print("Texto:", text)
print("Suffix Array:", suffix_array)
