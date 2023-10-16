#include <iostream>
#include <vector>

// La complejidad de tiempo de Merge Sort es O(n log n), donde 'n' es el número
// de elementos en el arreglo. Esta función merge combina dos subarreglos
// ordenados en un solo arreglo ordenado.
void merge(std::vector<int> &arr, int left, int middle, int right) {
  // Calcula el tamaño de los subarreglos izquierdo y derecho.
  int size_izquierda = middle - left + 1;
  int size_derecha = right - middle;

  // Crea dos subvectores para almacenar los elementos de los subarreglos
  // izquierdo y derecho.
  std::vector<int> left_half(size_izquierda);
  std::vector<int> right_half(size_derecha);

  // Copia los elementos de los subarreglos izquierdo y derecho a los
  // subvectores correspondientes.
  for (int i = 0; i < size_izquierda; ++i)
    left_half[i] = arr[left + i];

  for (int i = 0; i < size_derecha; ++i)
    right_half[i] = arr[middle + 1 + i];

  // Combina los subarreglos izquierdo y derecho en el arreglo original en orden
  // ascendente.
  int left_index = 0;
  int right_index = 0;
  int merged_index = left;

  while (left_index < size_izquierda && right_index < size_derecha) {
    if (left_half[left_index] <= right_half[right_index]) {
      arr[merged_index] = left_half[left_index];
      left_index++;
    } else {
      arr[merged_index] = right_half[right_index];
      right_index++;
    }
    merged_index++;
  }

  // Copia cualquier elemento restante del subarreglo izquierdo al arreglo
  // original.
  while (left_index < size_izquierda) {
    arr[merged_index] = left_half[left_index];
    left_index++;
    merged_index++;
  }

  // Copia cualquier elemento restante del subarreglo derecho al arreglo
  // original.
  while (right_index < size_derecha) {
    arr[merged_index] = right_half[right_index];
    right_index++;
    merged_index++;
  }
}

// Esta función implementa el algoritmo Merge Sort para ordenar un arreglo.
void merge_sort(std::vector<int> &arr, int left, int right) {
  if (left < right) {
    // Encuentra el punto medio del arreglo
    int middle = left + (right - left) / 2;
    merge_sort(arr, left, middle);      // Ordena la mitad izquierda.
    merge_sort(arr, middle + 1, right); // Ordena la mitad derecha.
    merge(arr, left, middle, right);    // Combina las mitades ordenadas.
  } else {
    return; // Caso base: el arreglo ya está ordenado o contiene un solo
            // elemento.
  }
}

int main() {
  std::vector<int> arr; // Crea un vector de enteros para almacenar los datos.

  // Agrega algunos números desordenados al vector.
  arr.push_back(1);
  arr.push_back(3);
  arr.push_back(6);
  arr.push_back(5);
  arr.push_back(2);
  arr.push_back(12);
  arr.push_back(2);
  arr.push_back(16);
  arr.push_back(28);
  arr.push_back(4);
  arr.push_back(8);
  arr.push_back(7);

  // Llama a la función merge_sort para ordenar el vector.
  merge_sort(arr, 0, arr.size() - 1);

  // Imprime el vector ordenado.
  for (int i = 0; i < arr.size(); i++) {
    std::cout << arr[i] << ",";
  }

  return 0;
}
