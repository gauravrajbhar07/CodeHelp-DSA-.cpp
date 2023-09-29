#include <iostream>
#include <vector>
using namespace std;

//i/p
// 4 
// 2 4 6 8
// 3 
// 1 3 7

//o/p
// 2 4 6 8 1 3 7 

vector<int> Union(vector<int> arr,vector<int> brr){

    vector<int> ans;

    for(int i = 0 ; i < arr.size() ;i++){
        ans.push_back(arr[i]);
    }

    for(int i = 0 ; i < brr.size() ;i++){
        ans.push_back(brr[i]);
    }

    //pending 
    

   



    
    

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


    vector<int> ans = Union(arr,brr);
    for(int i = 0 ; i< ans.size() ; i++){
        cout<<ans[i]<<" ";
    }
 

    return 0;
}
