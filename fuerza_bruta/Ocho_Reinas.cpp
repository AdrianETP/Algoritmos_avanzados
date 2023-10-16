#include <cstring>
#include <iostream>
#include <vector>

// Problema de las 8 reinas
// complejidad O(n^n)
// Guillermo Garcia Acosta
// A01620676

#define N 8 // Tamaño del tablero

bool board[N][N]; // Tablero

bool isSafe(int row, int col) {
  // verificar si hay una reina en la misma fila
  for (int i = 0; i < col; i++) {
    if (board[row][i]) {
      return false;
    }
  }
  // verificar diagonal superior izquierda
  for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
    if (board[i][j]) {
      return false;
    }
  }
  // verificar diagonal inferior izquierda
  for (int i = row, j = col; i < N && j >= 0; i++, j--) {
    if (board[i][j]) {
      return false;
    }
  }
  return true;
}

// Función recursiva para resolver el problema de las 8 reinas
// Regresa true si las reinas se pueden colocar en el tablero
// de manera que no se ataquen entre ellas, de lo contrario regresa false
bool solve(int col) {
  if (col >= N)
    return true;

  for (int i = 0; i < N; i++) {
    if (isSafe(i, col)) {
      board[i][col] = true;
      if (solve(col + 1)) { // Recursivamente colocar el resto de las reinas
        return true;
      }
      board[i][col] = false; // Si no hay lugar para la reina en la fila actual,
                             // entonces regresa false
    }
  }

  return false; // si la reina no puede ser colocada en ninguna fila de esta
                // columna, regresa false
}

int main() {
  // Inicializar el tablero
  std::memset(board, false, sizeof(board));

  // Llamar a la función solve
  if (!solve(0))
    std::cout << "No hay solución" << std::endl;

  else {
    // Imprimir el tablero
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        if (board[i][j])
          std::cout << "Q ";
        else
          std::cout << ". ";
      }
      std::cout << std::endl;
    }
  }

  return 0;
}