#include <iostream>
using namespace std;



int main() {
    int num;
    cin >> num;

 

    for (int i = 0; i < num; i++) {
        char s;
        int j;
        for( j = 0 ; j < i+1 ;j++){
            int ans= j + 1;
            char ch = ans + 'A';

            cout<<ch<<" ";
            // 

        }
        j = j -1;
        for(; j >= 1 ;j--){
            cout<<" ";

        }

        
        
        cout << endl;
    }
     
   

    return 0;
}
