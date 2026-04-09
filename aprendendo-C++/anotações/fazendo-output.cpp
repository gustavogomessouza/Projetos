#include <iostream>

int main(){

    int x = 10;
    int y = 20;

    std::cout << "x =";
    std::cout << x;

    // isso equivale a:

    std::cout << "x = " << x;


    // se eu quiser fazer uma quebra de linha:

    std::cout << std::endl;


    // juntando tudo

    std::cout << "x = " << x << std::endl 
              << "y = " << y << std::endl;
    // como indentação não faz diferença, da pra organizar mais legalzinho



    return 0;
}