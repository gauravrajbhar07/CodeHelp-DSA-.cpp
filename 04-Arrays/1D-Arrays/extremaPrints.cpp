#include <iostream>
using namespace std;

int main() {
    
    //even number
    // 1 8 2 7 3 6 4 5 

    //odd number
    //1 8 2 7 3 6 5

    int arr[6] ={2,3,5,6,7,8};
    int start = 0;
    int end = 5;

    while(true){

        if(start > end)
        {
            break;
        }

        if(start == end){
            cout<<arr[start];
        }
        else{
        cout<<arr[start]<<" "<<arr[end]<<" ";

        }
        start++;
        end--;
    }
    

   

    return 0;
}
