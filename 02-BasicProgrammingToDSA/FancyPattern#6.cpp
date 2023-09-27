#include <iostream>
#include <string>
using namespace std;


// 7
// *
// *1*
// *121*
// *12321*
// *1234321*
// *12321*
// *121*
// *1*
// *

int main()
{
    int n;
    cin>>n;
    int c = 1;

    cout<<"*"<<endl;
    
    for(int i = 0 ; i < n ; i++){
        
        int conditionVariable = i <= n/2 ? 2*i : 2*(n - i - 1);
        cout<<"*";
        for(int j = 0 ; j <=conditionVariable ; j++){
            
            if(j <= conditionVariable/2){
                cout<<j + 1;
            }else{
                cout<<conditionVariable - j + 1;
            }
        }
        cout<<"*";

        cout<<endl;
    }
    cout<<"*";

    return 0;
}
