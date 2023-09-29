#include <iostream>
#include <vector>
using namespace std;

//i/p
// 4
// 10 20 30 40 
// 80

//o/p
// 10 30 40


void PairSum(vector<int> arr,int sum){

    for(int i = 0 ; i <= arr.size(); i++)
    {
        for(int j = i + 1  ; j <= arr.size() ;j++ ){
            // cout<<"hello'";
            for(int k = j + 1;  k <= arr.size(); k++){

                if(arr[i] + arr[j] + arr[k] == sum){
                    cout<<arr[i] << " "<< arr[j]<<" "<< arr[k]<<endl;
                }
            }
        }
    }
    
}

int main() {

    int n1;
    cin>>n1;
    vector<int> arr(n1);
    
    for(int i = 0 ; i< n1 ; i++){
        cin>>arr[i];
    }

    int sum;
    cin>>sum;


   PairSum(arr,sum);
    
 

    return 0;
}
