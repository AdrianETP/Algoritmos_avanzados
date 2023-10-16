#include <algorithm>
#include <iostream>
#include <vector>

/* el algoritmo que eleji implementar que incluye fuerza bruta es selection sort
 * En este algoritmo se va a ordenar una lista desordenada encontrando el
 * elemento menor con busqueda secuencial y luego mandandolo al principio. Este
 * proceso se repite hasta que la lista este ordenada dando una complejidad de
 * O(n^2)
 */

// se recive una lista de cualquier tipo de elemento y se devuelve lo mismo
template <class T> std::vector<T> selection_sort(std::vector<T> &list) {
  for (int i = 0; i < list.size(); i++) {
    int smallest_number =
        std::numeric_limits<T>::max(); // asigna la variable a el valor mas
                                       // grande posible
    int smallest_index = -1;           // smallest index es -1
    for (int j = i; j < list.size(); j++) {
      if (list[j] <= smallest_number) { // si el valor que estamos comparando es
                                        // menor que el valor de smallest index,
                                        // se asigna ese valor a smallest index
        smallest_number = list[j];
        smallest_index = j;
      }
    }
    list.erase(
        list.begin() +
        smallest_index); // el que termine siendo smallest index se borra y se
                         // pone en el principio (el principio despues de los
                         // valores cambiados anteriormente)
    list.insert(list.begin() + i, smallest_number);
  }
  return list;
}

int main() {
  std::vector<int> list;
  list.push_back(1);
  list.push_back(10);
  list.push_back(2);
  list.push_back(5);
  list.push_back(9);
  list.push_back(6);
  std::vector<int> ordered_list = selection_sort(list);
  for (int i = 0; i < ordered_list.size(); i++) {
    std::cout << ordered_list[i] << ",";
  }
  return 0;
}
