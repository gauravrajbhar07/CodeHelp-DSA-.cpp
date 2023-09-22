#include <iostream>
#include <cmath>
using namespace std;

int BinaryToDecimal(int n){
    //multiplication Methods

    int decimalNumber = 0;
    int i = 0 ;


    while(n > 0){
        int bit = (n & 1);
        
        decimalNumber = bit *pow(2,i) + decimalNumber;

        n = n / 10 ;
        i = i + 1 ;

        
        
    }
    return decimalNumber;
}


int main(){

    int n;
    cin>>n;
    int binary = BinaryToDecimal(n);
    cout<<binary;


    return 0;
}