#include <iostream>
#include <vector>

using namespace std;

/* La complejidad de este algoritmo es O(n!) y el peor caso es O(12!). Ya que
para n = 12, el número de permutaciones sería 12! = 479,001,600.*/

// Función para invertir el orden de los elementos en un rango de un vector
void invertirOrden(vector<int> &permutacion, int indiceIni, int indiceFin) {
  while (indiceIni < indiceFin) {
    int aux = permutacion[indiceIni];
    permutacion[indiceIni] = permutacion[indiceFin];
    permutacion[indiceFin] = aux;
    indiceIni++;
    indiceFin--;
  }
}

// Función para generar todas las permutaciones lexicográficas hasta n
vector<vector<int>> permutacionesLex(int n) {
  vector<vector<int>>
      permutaciones;          // Almacenará todas las permutaciones generadas
  vector<int> permutacion(n); // Almacena la permutación actual

  // Casos base para n igual a 0 y 1
  if (n == 0) {
    return permutaciones; // No hay permutaciones para n = 0
  } else if (n == 1) {
    permutacion.push_back(1);
    permutaciones.push_back(permutacion);
    return permutaciones; // Solo una permutación [1] para n = 1
  }

  // Generar la primera permutación (orden inicial)
  for (int i = 1; i <= n; i++) {
    permutacion[i - 1] = i;
  }
  permutaciones.push_back(permutacion);

  // Variables para encontrar índices maxI y maxJ
  int aux, i = 0;
  int maxI = -1; // Mayor índice de i
  int maxJ = -1; // Mayor índice de j

  while (true) {
    // Encontrar el mayor índice i tal que permutacion[i] < permutacion[i + 1]
    int i = n - 2;
    while (i >= 0 &&
           permutacion[i] >
               permutacion[i + 1]) { // Recorrer lista hasta i con mayor indice
      i--;
    }

    if (i < 0) {
      // Ya se generaron todas las permutaciones
      break;
    }

    // Encontrar el mayor índice j tal que permutacion[i] < permutacion[j]
    int j = n - 1;
    while (permutacion[j] <
           permutacion[i]) { // Recorrer lista hasta j con mayor indice
      j--;
    }

    // Intercambiar permutacion[i] y permutacion[j]
    swap(permutacion[i], permutacion[j]);

    // Invertir el orden de los elementos después de i
    invertirOrden(permutacion, i + 1, n - 1);

    // Agregar la permutación generada a la lista de permutaciones
    permutaciones.push_back(permutacion);
  }
  return permutaciones;
}

// Función para imprimir las permutaciones generadas
void imprimirPermutaciones(const vector<vector<int>> &permutaciones) {
  for (const auto &permutacion : permutaciones) {
    for (int num : permutacion) {
      cout << num << " ";
    }
    cout << endl;
  }
}

int main() {
  vector<vector<int>> permutaciones;
  permutaciones = permutacionesLex(4);
  imprimirPermutaciones(permutaciones);
  return 0;
}
