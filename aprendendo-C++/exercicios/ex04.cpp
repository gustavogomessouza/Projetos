#include <iostream>

#include <cstdlib>

using namespace std;

int main(){

    const short valor_maximo = 6;
    const short valor_minimo = 1;

    srand(time(nullptr));

    int valor_girado = rand()% (valor_maximo - valor_minimo + 1) + valor_minimo;
    int segundo_valor_girado = rand()% (valor_maximo - valor_minimo + 1) + valor_minimo;
    
    cout << valor_girado << "," << segundo_valor_girado;



    return 0;
}