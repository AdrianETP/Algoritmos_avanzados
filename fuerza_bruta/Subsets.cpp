#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// La complejidad del algoritmo es O(n^2) es exponencial en función del tamaño de entrada. 
// Función para revertir una lista de vectores 
vector<vector<int>> revertirLista(vector<vector<int>> a){
    vector<vector<int>> b;
    int size = a.size();
    for(int i = 0; i<size; i++){
        b.push_back(a.back());  // Agrega el último vector de 'a' al final de 'b'
        a.pop_back();  // Elimina el último vector de 'a'
    }
    return b;
}

// Función para imprimir los subconjuntos 
void imprimirSubSets(const vector<vector<int>>& permutaciones) {
    for (const auto& permutacion : permutaciones) {
        for (int num : permutacion) {
            cout << num << " ";  
        }
        cout << endl;
    }
}

// Función para agregar un cero al inicio de cada vector en 'n'
void agregaCero(vector<vector<int>>& n){
    for(int i = 0; i<n.size();i++){
       n[i].insert(n[i].begin(), 0);  // Inserta un cero al principio de cada vector
    }
}   

// Función para agregar un uno al inicio de cada vector en 'n'
void agregaUno(vector<vector<int>>& n){
    for(int i = 0; i<n.size();i++){
       n[i].insert(n[i].begin(), 1);  // Inserta un uno al principio de cada vector
    }
}   

/* Función para generar el conjunto potencia de N elementos usando representación binaria O(n) porque aumenta
conforme el tamaño de total del conjunto*/
vector<vector<int>> powerSetBin(int n){
    vector<vector<int>> Lista1;  
    vector<vector<int>> Lista2;  
    if(n == 1){
        Lista1.push_back({0});  // Agrega el subconjunto {0} a Lista1
        Lista1.push_back({1});  // Agrega el subconjunto {1} a Lista1
        return Lista1;  
    }
    else{
        Lista1 = powerSetBin(n-1);  // Genera los subconjuntos para n-1 elementos
        Lista2 = revertirLista(Lista1);  
        agregaCero(Lista1); 
        agregaUno(Lista2);  
        Lista1.insert(Lista1.end(), Lista2.begin(), Lista2.end());  
        return  Lista1;  
    }
}


int main() { 
    imprimirSubSets(powerSetBin(3));  // Imprime el conjunto potencia de 3 elementos

    return 0;
}
