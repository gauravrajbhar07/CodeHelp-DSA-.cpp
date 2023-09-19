#include <iostream>
using namespace std;
//                 1
//             2   3   2
//         3   4   5   4   3
//     4   5   6   7   6   5   4
// 5   6   7   8   9   8   7   6   5   

int main(){

    int num;
    cin>>num;

    for(int i = 0 ; i <= num ; i++){
        for(int j = 1 ; j < num - i ; j++){
            cout<<" ";
        }

        for(int j = i ; j < 2 * i;j++){
            cout<<j<<" ";
        }

        int elem = 2* (i - 1);
        for(int j = 1 ; j <= i - 1 ;j++){
            cout<<elem--<<" ";
        }

       
        cout<<endl;
    }

    return 0;

}