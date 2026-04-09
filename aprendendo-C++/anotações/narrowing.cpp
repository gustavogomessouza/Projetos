#include <iostream>

using namespace std;

int main(){

    int numero = 1'000'000; // aqui o apóstrofe é apenas para legibilidade

    short numero2 = numero; // como short tem menos bites que int, então o valor de 'numero' é diminuido para caber em um short.
    // short numero2 {numero}; // previne o erro

    cout << numero2;


    return 0;
}