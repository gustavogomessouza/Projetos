#include <iostream>

using namespace std;

int main(){

    double price = 99.9;
    float interest_rate = 3.67F; // O "F" no final serve porque o compilador lê qualquer decimal como "Double", então ele tentaria botar um double num float e teria perde de informação

    long file_size = 90000L; // O "L" tem a mesma função do "F" anterior

    char letra = 'a';

    bool condicao = false;


    auto variavel = true; // auto-typa para bool
    auto variavel2 = 900000L; // auto-typa para long
    auto variavel3 = 900000; // auto-typa para int
    auto variavel4 = 'a'; // auto-typa para char
    auto variavel5 = "a"; // auto-typa para 'const char'
    auto variavel6 = 3.14F; // auto-typa para float
    auto variavel7 = 3.14; // auto-typa para double



    // inicializar com {}

    int valor; // set o valor para um número aleatório (que estava na memória antes eu acho).
    int valor2 {}; // set o valor para 0 quando inicializa.
    int valor3 {/*1.4*/}; // impede que algo que não possa ser convertido seja inicializado.

    return 0;
}

