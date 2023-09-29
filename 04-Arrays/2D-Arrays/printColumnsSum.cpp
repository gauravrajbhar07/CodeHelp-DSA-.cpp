#include <iostream>
#include <vector>
using namespace std;

// 11 24 23 22 

void printColSum(int arr[][4],int row ,int col){
    for(int i = 0 ; i < col; i++){
        int sum = 0;
        for(int j = 0 ; j < row ; j++){
            sum = sum + arr[j][i];
        }
        cout<<sum<<" ";
    }

  
    
    
}

int main() {

    // int row = 5;
    // int col = 4;

    int arr[5][4] = {{1,2,3,4},{2,3,4,1},{5,6,1,3},{2,4,6,8},{1,9,9,6}};
 
    printColSum(arr,5,4);


   
    
 

    return 0;
}
