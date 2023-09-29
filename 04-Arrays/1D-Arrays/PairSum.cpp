#include <iostream>
#include <vector>
using namespace std;

//i/p
// 7       
// 1 3 5 7 2 4 6
// 9

//o/p
// 3 6
// 5 4
// 7 2

void PairSum(vector<int> arr,int sum){

    for(int i = 1 ; i <= arr.size(); i++)
    {
        for(int j = i + 1  ; j <= arr.size() ;j++ ){
            if(arr[i] + arr[j] == sum){
                cout<<arr[i] << " "<< arr[j]<<endl;
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
