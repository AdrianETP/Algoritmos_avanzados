#include <iostream>

// este algoritmo tiene una complejidad de 0(log n) ya que divide n
// repetidamente por 2 .Este algoritmo recive a y n y regresa el numero de a^n.
// Este algoritmo es mejor que hacerlo de fuerza bruta ya que la complejidad en
// cuanto a tiempo es menor que en fuerza bruta, siendo que se tendria que
// multiplicar a n veces usando un for loop en fuerza bruta mientras que aca se
// hace una sola operacion que se tarda  log(n) en sacar
int fast_pow(int a, int n) {
  if (n == 0) {
    return 1;
  }
  // si n es un numero par, llama fast pow con n/2 una vez y regresa su
  // multiplicacion por si mismo si n es impar, llama fast pow pero a (n-1)/2  y
  // lo multiplica por si mismo y por a para compensar el 1 que le restamos a n
  if (n % 2 == 0) {
    int half_pow = fast_pow(a, n / 2);
    return half_pow * half_pow;
  } else {
    int half_pow = fast_pow(a, (n - 1) / 2);
    return half_pow * half_pow * a;
  }
}

int main() {
  int result = fast_pow(2, 20);
  std::cout << result << std::endl;
  return 0;
}
