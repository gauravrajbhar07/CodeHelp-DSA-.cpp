#include <iostream>
#include <string>
using namespace std;

// For setting the K th bit we will simply use bitwise all operation

// ip
// 10
// 2

// op
// 14
int setKthBit(int n,int k){

    int num = 1<<k;
    return n | num;
     

    
}


int main()
{
    int n;
    cin>>n;
    int k; 
    cin>>k;

    cout<<setKthBit(n,k);
  
    
    
    return 0;
}
