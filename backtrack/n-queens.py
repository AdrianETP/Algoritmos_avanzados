# para este algoritmo vamos a marcar una reglas para la reina

# 2 reinas no pueden estar en la misma columna (c)
# 2 reinas no pueden estar en la misma fila (r)
# 2 reinas no pueden estar en una diagonal positiva (c+r != constante)
# 2 reinas no pueden estar en una diagonal negativa (c-r != constante)

# la complejidad de este algoritmo es de O(n!), ya que en el peor de los casos, este va a tener que hacer
# TODAS las posibles combinaciones de reinas

# una forma en la cual se podria mejorar este algoritmo es haciendo una busqueda es hacer la 
# regla de minimo conflicto, en la cual se coloquen estrategicamente las reinas 
#en lugares que causen menos conflicto con otras reinas


def nQueens(n):
    # creamos listas (columna , diagonal positiva y diagonal negativa)
    # no creamos fila por que la recursion siempre va a pasar a la siguiente fila asi que no da sentido verificar si son diferentes
    col = set()
    positiveDiag = set()
    negativeDiag = set()
    # la tabla que estaremos modificando
    board = [["."]*n for i in range(n)]
    result = []

    def backtrack(r):

        # si r == n significa que ya encontro una combinacion exitosa asi que la pone en el array de result
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return

        # recorre todas las columnas en la tabla
        for c in range(n):
            # si alguno de estos casos es cierto, se salta este loop del for loop
            if r == c or c in col or (r+c) in positiveDiag or (r-c) in negativeDiag:
                continue
            # si no es ninguno de los casos anteriores, corre backtrack de nuevo pero en r+1 y con col, positiveDiag y negativeDiag con las nuevas variaciones agregadas
            positiveDiag.add(r+c)
            negativeDiag.add(r-c)
            col.add(c)
            board[r][c] = "Q"
            backtrack(r+1)
            # en esta parte se borra todo el progreso para probar otra posible combinacion (igual si si era correcta ya se guardo en result)
            positiveDiag.remove(r+c)
            negativeDiag.remove(r-c)
            col.remove(c)
            board[r][c] = "."

    # se corre backtrack en la primera fila
    backtrack(0)
    # se regresa result ya modificado por backtrack
    return result


# corre nQueens(4 como prueba)
print(nQueens(4))
