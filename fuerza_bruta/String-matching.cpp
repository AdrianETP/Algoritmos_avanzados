#include <cmath>
#include <iostream>
#include <vector>
using namespace std;


// La complejidad del algoritmo es O(n * m), donde n es la longitud del string de texto y m es la longitud del string patrón.

// Función para encontrar todas las apariciones de un string patrón dentro de un string de texto
vector<int> stringMatching(const string &text, const string &pattern) {
  int n = text.size(); //Longitud de la cadena de texto
  int m = pattern.size(); // Longitud de la cadena patrón
  vector<int> positions; // Lista para almacenar las posiciones donde se encuentra la cadena patrón


  // Repite el proceso para cada posible punto de inicio en la cadena de texto
  // (de 0 a n - m)
  for (int i = 0; i <= n - m; ++i) {
    int j; // Variable para seguir la posición dentro del patrón
    for (j = 0; j < m; ++j) {
      if (text[i + j] != pattern[j]) {
        break; // Si alguna letra no coincide, deja de buscar en esta posición
      }
    }

    if (j == m) {
      positions.push_back(
          i); // Si se encontró una coincidencia completa, guarda la posición
    }
  }

  return positions; // Devuelve la lista de posiciones donde se encontró el
                    // patrón
}

int main() {
  string text =
      "Este es un ejemplo de string matching con un ejemplo más."; // Texto en
                                                                   // el cual
                                                                   // buscar
  vector<string> patterns = {"ejemplo", "string",
                             "más"}; // Lista de patrones para buscar

  // Repite el proceso para cada patrón en la lista
  for (const auto &pattern : patterns) {
    vector<int> positions =
        stringMatching(text, pattern); // Busca el patrón en el texto

    // Si se encontró el patrón, imprime las posiciones
    if (!positions.empty()) {
      cout << "Patrón \"" << pattern << "\" encontrado en las posiciones: ";
      for (int position : positions) {
        cout << position << " ";
      }
      cout << endl;
    } else { // Si no se encontró el patrón, imprime un mensaje
      cout << "Patrón \"" << pattern << "\" no encontrado." << endl;
    }
  }

  return 0; // Termina el programa devolviendo 0, que es una señal de que todo
            // salió bien

}
