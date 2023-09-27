#include <iostream>
#include <string>
using namespace std;

// 5
// ********1********
// *******2*2*******
// ******3*3*3******
// *****4*4*4*4*****
// ****5*5*5*5*5****

int main()
{
    int n;
    cin>>n;
    int k = 1;


    for(int i = 0 ; i <= n ; i++){

        for(int j = 0 ; j < i ; j++){
            if(j == i){
                cout<<k;
                k++;
            }
            
            cout<<k<<"*";
            k++;
        
            
        }
        cout<<endl;
    }
    int start  = k - n;
    // cout<<start;

    for(int i = 0 ; i <= n ; i++){
        int c = start;
        for(int j = 0 ; j <= n - i - 1 ;j++ ){

            cout<<c;
            c++;
        }
        start = start - (n - i - 1);

        cout<<endl;
    }

    return 0;
}
