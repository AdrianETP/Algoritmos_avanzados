#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

// para este algoritmo de fuerza bruta voy a buscar una manera de recrear
// fake_coin de manera secuencial

// este algoritmo tiene complejidad de O(n) por que recorre toda la longitud de
// la lista
// este algoritmo recive una lista de monedas y devuelve el indice de donde esta
// la moneda falsa
//
// este algoritmo es peor que el tradicional de decrementa y venceras por que en
// este se tiene que recorrer toda la lista mientras que en el otro lo va
// dividiendo a la mitad y por lo tanto recorre mucho menos
int fake_coin(std::vector<float> coins) {
  int smallest_coin_index = -1;
  int smallest_coin = std::numeric_limits<int>::max();
  // recorre toda la lista y si encuentra una moneda mas pequena que la moneda
  // actual mas pequena lo remplaza en las variables
  for (int i = 0; i < coins.size(); i++) {
    if (coins[i] < smallest_coin) {
      smallest_coin = coins[i];
      smallest_coin_index = i;
    }
  }
  return smallest_coin_index;
}

int main() {
  std::vector<float> coins;
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(0.7);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  coins.push_back(1);
  std::cout << fake_coin(coins);
}
