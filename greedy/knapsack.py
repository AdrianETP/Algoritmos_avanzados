# la estrategia de este algoritmo es sacar los ratios (valor/peso) y ordenarlos en forma decedente por ratio
# de ahi es seleccionar los elementos con mayor ratio mientras que aun tengamos la capacidad para ponerlo

# este algoritmo es greedy por que no es la solucion mas optima pero si es una solucion que funciona en todos los casos

# un ejemplo en el cual este algoritmo no daria lo mas eficiente es cuando los
# elementos 2 y 3 darian un ratio mas grande que el elemento 1
# si los sumaras pero por el elemento 1 ya no puedes poner ninguno de esos elementos

# la complejidad es de O(n) siendo que no hay recursion ni for loops nesteados

def greedy_knapsack(values, weights, capacity):

    n = len(values)
    # se hace un array de tuplas con el ratio , valor , peso e indice
    ratios = [(values[i] / weights[i], values[i], weights[i], i)
              for i in range(n)]
    # se ordena el array de forma decendiente
    ratios.sort(reverse=True)
    # donde van a estar los valores totales
    total_value = 0
    knapsack = [0] * n

    # evaluacion de valores
    for _, val, weight, index in ratios:
        # si aun tenemos capacidad de poner el mas grande aun no seleccionado
        if capacity >= weight:
            knapsack[index] = 1
            total_value += val
            capacity -= weight

    return total_value, knapsack


# Ejemplo de uso
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
result, selected_items = greedy_knapsack(values, weights, capacity)
print("Valor máximo obtenido:", result)
print("Objetos seleccionados:", selected_items)
