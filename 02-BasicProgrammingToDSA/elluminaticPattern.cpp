#include <iostream>
#include <cmath>
using namespace std;


int main(){
    int n;
    cin>>n;

    int num_count = n * (n + 1)/2;
    // cout<<num_count;
    for(int i = 0 ; i <= n ;i++){
        
        for(int j = 0 ; j < i ; j++){

            if(j%2 == 0){
                cout<<num_count<<" ";
                num_count--;
                
            }

            else{

                cout<<num_count<<" ";
                num_count++;
            }

            num_count = num_count ;

        }
        cout<<endl;
    }



    return 0;
}