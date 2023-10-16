def max_coins(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    # Creamos una matriz para almacenar las soluciones parciales
    dp = [[0] * cols for _ in range(rows)]

    # Llenamos la primera fila y la primera columna con las monedas acumuladas
    dp[0][0] = grid[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Llenamos el resto de la matriz usando la relación de recurrencia
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    # El valor en la esquina inferior derecha de la matriz dp contiene la respuesta
    return dp[rows-1][cols-1]


grid = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

print("max number of coins: ",max_coins(grid))

# la formula que se usa es
# F(i, j) = max(F(i-1, j), F(i, j-1)) + C[i][j]

# - F (i , j ) = la cantidad maxima de monedas en la celda (i,j)
# - F (i-1 , j ) = la cantidad maxima de monedas en la celda a la izquierda de la actual
# - F (i , j-1 ) = la cantidad maxima de monedas en la celda arriba de la actual
# - C[i , j ] = la cantidad actual de monedas en la celda actual

# como lo esta analizando es que checa en que celda anterior (izquierda o arriba)
# hay mas monedas y la cantidad maxima de monedas la pone en una nueva matriz en la posicion de la celda actual
# esa misma nueva matriz la usa en las siguientes iteraciones y la
# cantidad maxima se va a ir sumando hasta que en la ultima celda venga la cantidad maxima de monedas que se puede recolectar:

# y obviamente si i o j < 0 va a regresar 0
