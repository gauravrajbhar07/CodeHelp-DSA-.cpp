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
    int c = 1;
    




    for(int i = 0 ; i < n ; i++){

        for(int j = 0 ; j<=i;j++){
            cout<<c;
            c++;
            if(j < i){
                cout<<"*";
            }
        }
    
        cout<<endl;
    }

    // cout<<c<<endl;
    int start = c - n;
     for(int i = 0 ; i < n ; i++){
        int k = start;
        for(int j = 0 ; j<=(n - i - 1);j++){
            cout<<k;
            k++;
            if(j < (n - i -1)){
                cout<<"*";
            }
            

        }
        start = start - (n - i - 1);
        // cout<<"start :"<<start<<endl

    
        cout<<endl;
    }

    return 0;
}
