#include <iostream>
using namespace std;

int main(){

    int num;
    cin>>num;

    for(int i = 0 ; i < num ; i++){
        int count = 1;
        for(int j = num; j > i ; j--){
            cout<<count<<" ";
            count++;
        }
        cout<<endl;
    }

   


    return 0;

}