#include <iostream>
#include <cmath>
using namespace std;


int main(){

    int n;
    cin>>n;

    // int 
    int count = 1;
    for(int i = 1 ; i <= n ; i++){
        for(int j = n ; j >= i ; j--){

            if(  i == 1 ){
                cout<<count;
                count++;
            }

            else if(j == i){
                cout<<n;

            }
            else if(j == n ){
                cout<<i;

            }
            else{
                cout<<" ";
            }
        }
        cout<<endl;
    }
    return 0;
}