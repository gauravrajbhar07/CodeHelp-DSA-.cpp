#include <iostream>
#include <string>
using namespace std;

// 5
// *        *
// **      **
// ***    ***
// ****  ****
// **********
// **********
// ****  ****
// ***    ***
// **      **
// *        *


int main()
{
    int n;
    cin>>n;
    // int c = 1;
    
    for(int i = 0 ; i <= 2*n ; i++){ 

        int cond = i<n ? i : n + (n - i -1);

        int space = i<n ? 2*(n - cond - 1) : (i - cond -1 );

        for(int j = 0 ; j < 2*n ; j++){
            if(j <= cond ){
                cout<<"*";
            }
            else if(space > 0){
                cout<<" ";
                space--;
            }
            else{
                cout<<"*";
            }
        }
        cout<<endl;
    }

    return 0;
}
