#include <iostream>
#include <string>
using namespace std;

// 123
// 321

// 123456789 
// 987654321

int reverseInterger(int n){

    int rem;
    int ans= 0;
    while(n!= 0){
        rem = n % 10;
        ans = ans*10 + rem;
        n = n / 10;
        
    }
    return ans;
}


int main()
{
    int n;
    cin>>n;

    cout<<reverseInterger(n);
  
    
    

    return 0;
}
