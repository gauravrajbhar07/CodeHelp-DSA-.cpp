#include <iostream>
#include <vector>
using namespace std;

// 10 10 15 20 25 

bool findKey(int arr[][4],int row ,int col,int key){
    for(int i = 0 ; i < row; i++){
     
        for(int j = 0 ; j < col ; j++){
            if(arr[i][j] == key){
                return true;
            }
        }
        
    }

    return false;

  
    
    
}

int main() {

    // int row = 5;
    // int col = 4;
    int key = 51;

    int arr[5][4] = {{1,2,3,4},{2,3,4,1},{5,6,1,3},{2,4,6,8},{1,9,9,6}};
 
    if(findKey(arr,5,4,key)){
        cout<<"element is present";
    }
    else{
        cout<<"Not present ";
    }


   
    
 

    return 0;
}
