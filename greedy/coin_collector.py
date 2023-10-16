# el algoritmo que vamos a usar es muy simple
# lo que va a hacer es que va a comparar si en la celda de abajo hay una moneda
# de mayor valor que la de la derecha y mediante esa comparacion de valores
# va a decidir a donde ir

# este es un algoritmo greedy por que no es para nada el mas optimo, pero es un
# algoritmo que va a funcionar decentemente en la mayoria de los casos
# (que va a encontrar un valor decente aunque no sea el mejor)

# no es el mas eficiente por que puede haber casos en los cuales el camino con
# mayor valor total tenga menos monedas al principio y el robot no tomaria ese
# camino por eso


def greedy_coin_collector(grid):
    max_coin_value = grid[0][0]
    y, x = 0, 0
    while y < len(grid) - 1 or x < len(grid[0]) - 1:
        # Comparar celdas de abajo y derecha
        down_value = grid[y + 1][x] if y + 1 < len(grid) else 0
        right_value = grid[y][x + 1] if x + 1 < len(grid[0]) else 0

        # Tomar la dirección con el valor máximo
        if down_value >= right_value:
            max_coin_value += down_value

            y += 1
        else:
            max_coin_value += right_value
            x += 1

    return max_coin_value


grid = [
    [1, 0, 5],
    [1, 2, 0],
    [0, 2, 1],
    [5, 0, 1],
]

print("Valor máximo de monedas:", greedy_coin_collector(grid))
