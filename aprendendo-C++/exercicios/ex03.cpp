#include <iostream>
#include <cmath>

using namespace std;

int main(){

    cout << "Insira o raio do seu círculo: ";
    double raio;
    cin >> raio;

    double perimetro = 2*raio*M_PI;

    double area = M_PI * raio * raio;


    cout << "O perímetro é: " << perimetro << endl
         << "A área é: " << area << endl;
    return 0;
}