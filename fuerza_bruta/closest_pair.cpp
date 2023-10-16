#include <cmath>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;

// La complejidad es O(n^2) porque se recorren todos los puntos y se calcula la
// distancia entre cada par de puntos.

struct Point { // creamos un struct point que tiene una coordenada x y y
  float x, y;
};

float getDistance(
    const Point &p1,
    const Point &p2) { // esta funcion obtiene la distancia entre 2 puntos con
                       // la formula de distancia ecludiana
  return sqrt(pow((p2.x - p1.x), 2) + pow((p2.y - p1.y), 2));
}

void closest_pair_brute_force(vector<Point> vec, Point &p1, Point &p2) {
  float smallestDistance = std::numeric_limits<float>::max();
  for (int i = 0; i < vec.size(); i++) { // este for loop recorre todos los
                                         // elementos y lo usa como referencia
    for (int j = i + 1; j < vec.size();
         j++) { // este for loop recorre todos los elementos y los compara con
                // el otro punto sacado en vec[i]
      float distance = getDistance(
          vec[i], vec[j]); // usamos getdistance para comparar la distancia
                           // entre el vector en i y el vector en j
      if (distance <
          smallestDistance) { // si el vector es mas chico que el vector mas
                              // chico actual, se asigna a la variable de
                              // sistancia y los puntos a p1 y p2
        p1 = vec[i];
        p2 = vec[j];
        smallestDistance = distance;
      }
    }
  }
}

int main() {
  vector<Point> points = {
      {-2.423, -8.469}, {5.721, 9.354},  {6.766, -3.823}, {4.129, 6.744},
      {5.371, -5.404},  {-8.101, 0.904}, {-7.121, 1.38},  {8.156, 6.039},
      {2.615, 2.077},   {-0.822, 9.342},
  };
  // puntos

  Point p1, p2;
  closest_pair_brute_force(points, p1, p2);

  cout << "Los puntos más cercanos son: (" << p1.x << ", " << p1.y << ") y ("
       << p2.x << ", " << p2.y << ")\n";
}
