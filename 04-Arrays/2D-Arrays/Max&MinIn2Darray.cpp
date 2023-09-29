#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

int Min(int arr[][4],int row ,int col){

    int min = INT_MAX;

    for(int i = 0 ; i < row; i++){
     
        for(int j = 0 ; j < col ; j++){
            if(arr[i][j] < min){
                min = arr[i][j];
            }
        }
        
    }

    return min;   
}


int Max(int arr[][4],int row ,int col){

    int max = INT_MIN;

    for(int i = 0 ; i < row; i++){
     
        for(int j = 0 ; j < col ; j++){
            if(arr[i][j] > max){
                max = arr[i][j];
            }
        }
        
    }

    return max;   
}

int main() {



    int arr[5][4] = {{1,2,3,4},{2,3,4,1},{5,6,1,3},{2,4,6,8},{1,9,9,6}};
 
    cout<<Max(arr,5,4);
    cout<<" ";
    cout<<Min(arr,5,4);


    return 0;
}
