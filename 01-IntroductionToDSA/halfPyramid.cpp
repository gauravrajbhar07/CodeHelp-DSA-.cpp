#include <iostream>
using namespace std;

int main(){


    //solid_Rectangle

    int row;

    cin>>row;

    for(int i = 1 ; i <=row ; i++){
        for(int j = 0 ; j < i;j++){
            cout<<"*";
        }
        cout<<endl;
    }
     


    return 0;

}