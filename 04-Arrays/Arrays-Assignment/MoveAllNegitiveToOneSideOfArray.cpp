#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

// Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
// Output: -12 -13 -5 -7 -3 -6 11 6 5

// Move all negative numbers to beginning and positive to end with constant extra space


vector<int> MoveAllNegitiveToOneSideOfArray(vector<int> arr) {

    int left = 0 ; 
    int right = arr.size() - 1;

    while(left <= right){
        if(arr[left] < 0 && arr[right] <0){
            left++;
        }

        else if(arr[left] < 0 && arr[right] > 0){
            left++;
            right--;
        }
        else if(arr[left] > 0 && arr[right] < 0){
            swap(arr[left],arr[right]);
            right--;
        }
        else{
            left++;
            right--;
        }
    }

    return arr;


    
    
}

int main() {

    vector<int> arr={-12, 11, -13, -5, 6, -7, 5, -3, -6};
    vector<int> ans = MoveAllNegitiveToOneSideOfArray(arr);
    for(int i= 0 ; i < ans.size() ; i++){
        cout<<arr[i]<<" ";
    }
    cout<<endl;
    for(int i= 0 ; i < ans.size() ; i++){
        cout<<ans[i]<<" ";
    }


    
    return 0;
}
