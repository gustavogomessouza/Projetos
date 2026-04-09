#include <iostream>

using namespace std;

int main(){

    double sales = 95000;
    double state_tax = 0.04;
    double county_tax = 0.02;


    cout << "Vendas totais: " << sales << "$" << endl
         << "Taxa do estado: " << state_tax*sales << "$" << endl
         << "Taxa do condado: " << county_tax*sales << "$" << endl
         << "Taxa total: " << (state_tax+county_tax)*sales << "$" << endl;




}