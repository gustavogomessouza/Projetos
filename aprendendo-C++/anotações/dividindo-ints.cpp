#include <iostream>

int main(){


    int x = 5;
    // diferença entre os dois: um é executado antes de pegar o valor de x e outro depois
    x++; 
    ++x;

    // Ex:
    int x = 5; 
    int a = ++x; // nesse caso: a == 6 , x == 6.

    int x = 5;
    int a = x++; // nesse caso: a == 5 , x == 6.


    x += 5;

    std::cout << x;

    return 0;


}