#include <iostream>
#include <vector>
using namespace std;

//i/p
// 9
// 0 1 1 0 1 0 1 0 0

//o/p
// 3 6
// 5 4
// 7 2

vector<int> PairSum(vector<int> arr){

    int start = 0;
    int end = arr.size() - 1;
    int i = 0 ;


    while(start <= end){

        if(arr[i] == 0){
            swap(arr[i],arr[start]);
            start++;
            i++;
        }
        else{
            swap(arr[i],arr[end]);
            end--;
        }
    }
        
        
    
    return arr;

    
    
}

int main() {

    int n1;
    cin>>n1;
    vector<int> arr(n1);
    
    for(int i = 0 ; i< n1 ; i++){
        cin>>arr[i];
    }


    


   vector<int> ans = PairSum(arr);

   for(int i = 0 ; i< n1 ; i++){
        cout<<ans[i]<<" ";
   }
    
    
 

    return 0;
}
