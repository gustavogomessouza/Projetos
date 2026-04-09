#include <iostream>

using namespace std;

int main(){

    int numero1 = 255; // salva m número na base decimal
    int numero2 = 0b11111111; // salva o mesmo número mas em base binária. "0b" é o prefixo de binário
    int numero3 = 0xFF; // salva o mesmo número mas em base hexadecimal. "0x" é o prefixo de hexadecimal

    cout << numero1 << endl << numero2 << endl << numero3;


    return 0;
}