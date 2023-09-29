#include <iostream>
#include <vector>
using namespace std;

// i/p
// 11
// 1 2 4 2 1 3 6 5 5 6 4

// o/p
// 3

int findUnique(vector<int> arr){

    int ans = 0;

    for(int i = 0 ; i < arr.size() ; i++){
        ans = ans ^ arr[i];   
    }

    return ans;
}

int main() {

    int n;
    cin>>n;

    vector<int> arr(n);
    for(int i = 0 ; i< n ; i++){
        cin>>arr[i];
    }

    int ans = findUnique(arr);
    cout<<ans;
 

    return 0;
}
