#include <iostream>

#include <cstdlib> // é a versão do C++ da biblioteca 'stdlib.h' do C. Dela vem o rand()

#include <ctime>


using namespace std;

int main() {

    

    srand(6); // ISSO SETA A VARIÁVEL DE RAND() PARA OUTRO NÚMERO MAS COMO É SEMPRE O MESMO TAMBÉM NÃO MUDA NADA
    
    // ler esse bloco por último
    long aleatorio = time(nullptr); // pega o número de segundos desde 1970. 
    srand(aleatorio);
    // que pode ser:    
    srand(time(nullptr));


    int numero = rand() % 1000; // SEMPRE DÁ O MESMO NÚMERO, NÃO É ALEATÓRIO DE VDD.
    // a parte %1000 do código faz com que o máximo desse número aleatório seja 1000. (é algebra modular básica né vamo lá)

    // FÓRMULA PARA LIMITAR O RAND():  int variavel = [rand() % (valor_maximo - valor_minimo + 1)] + valor_minimo

    // Como resolver?
    // Usar o tempo corrido em segundos desde 1970 como variável de rand(). Olha que inteligente.
    
    cout << numero;

    return 0;
}