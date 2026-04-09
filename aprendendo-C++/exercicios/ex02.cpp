
// converter celcius para fahrenheit

#include <iostream>

using namespace std;

int main(){

    cout << "Insira o valor em Celcius a ser convertido";
    
    double v_celcius;
    cin >> v_celcius;
 
    double v_fahrenheit = (v_celcius/5*9)+32;

    cout << v_fahrenheit;
    

    return 0;




}