#include <iostream>
using namespace std;

// 5
// 
// 1
// 2*2
// 3*3*3
// 4*4*4*4
// 5*5*5*5*5
// 6*6*6*6*6*6
// 5*5*5*5*5
// 4*4*4*4
// 3*3*3
// 2*2
// 1

int main() {
    int num;
    cin >> num;

    for (int i = 0; i < num; i++) {
        for(int j = 0 ; j < i +1 ;j++){
            cout<< i+1;
            if( j != i){
                cout<<"*";
            }
           
        }
        
        cout << endl;
    }
     for (int i = num; i >= 0; i--) {
        for(int j = 0 ; j < i +1 ;j++){
            cout<< i+1;
            if( j != i){
                cout<<"*";
            }
           
        }
        
        cout << endl;
    }
    
   

    return 0;
}
