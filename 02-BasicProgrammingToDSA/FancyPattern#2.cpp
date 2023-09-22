#include <iostream>
using namespace std;



// 5
// A
// A B A
// A B C B A
// A B C D C B A
// A B C D E D C B A



int main() {
    int num;
    cin >> num;

 

    for (int i = 0; i < num; i++) {
        char s;
        int j;
        for( j = 0 ; j < i+1 ;j++){
            int ans= j + 1;
            char ch = ans + 'A' -1;

            cout<<ch<<" ";
            // 

        }
        j = j -1;
        for(int j = i; j >= 1 ;j--){
            int ans = j;
            char ch = ans + 'A' -1;
            cout<<ch<<" ";
            
        }

        
        
        cout << endl;
    }
     
   

    return 0;
}
