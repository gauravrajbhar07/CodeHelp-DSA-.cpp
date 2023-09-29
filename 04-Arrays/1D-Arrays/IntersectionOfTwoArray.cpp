#include <iostream>
#include <vector>
using namespace std;

// i/p
// 6
// 1 2 3 4 6 8
// 4 
// 3 4 9 10

// o/p
// 3 4

vector<int> InterSection(vector<int> arr,vector<int> brr){

    vector<int> ans;

    for(int i = 0 ; i < arr.size() ;i++){
        int k = arr[i];
        for(int j = 0 ; j < brr.size(); j++){
            if(k == brr[j]){

                //marking the value
                brr[j] = -1;
                ans.push_back(k);

            }
        }
    }



    return ans;
}

int main() {

    int n1;
    cin>>n1;

    vector<int> arr(n1);

    for(int i = 0 ; i< n1 ; i++){
        cin>>arr[i];
    }

    int n2;
    cin>>n2;
    vector<int> brr(n2);
    for(int i = 0 ; i< n2 ; i++){
        cin>>brr[i];
    }

    vector<int> ans = InterSection(arr,brr);
    for(int i = 0 ; i< ans.size() ; i++){
        cout<<ans[i]<<" ";
    }
 

    return 0;
}
