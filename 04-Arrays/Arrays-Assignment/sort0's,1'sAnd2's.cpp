#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

// i/p
// 0 1 2 0 1 2 

// o/p
// 0 0 1 1 2 2 


vector<int> DutchNationalFlagProblems(vector<int> arr) {

    int low = 0; 
    int mid = 0;
    int high = arr.size() - 1;
    int i = 0;

    while(mid <= high){
        if(arr[mid] == 0){
            swap(arr[mid],arr[low]);
            low++;
            mid++;
        }
        else if(arr[mid] == 1){

            mid++;
        }
        else{
            swap(arr[mid],arr[high]);
            high--;
        }
        
    }

    return arr;
    
}

int main() {

    vector<int> arr={0, 1, 2, 0, 1, 2};
    vector<int> ans = DutchNationalFlagProblems(arr);
    for(int i= 0 ; i < ans.size() ; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    for(int i= 0 ; i < ans.size() ; i++){
        cout<<ans[i]<<" ";
    }


    
    return 0;
}
