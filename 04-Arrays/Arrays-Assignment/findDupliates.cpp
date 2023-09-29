#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

// i/p
// 1,3,4,2,3

// o/p
// The duplicate element is 3

//better approach
int findDuplicateBetter(vector < int > & arr) {

  int n = arr.size();
  int size = n + 1;
  vector < int > freq(size,0);
  for(int i = 0 ; i < n ; i++){
    if(freq[arr[i]] == 0){
      freq[arr[i]]++;
    }
    else{
      return arr[i];
    }

  }

  
  return 0;
}


//optimalApproach
int findDuplicateOptimal(vector < int > & arr){

  int slow = arr[0];
  int fast = arr[0];

  do{
    slow = arr[slow];
    fast = arr[arr[fast]];

  }while(slow != fast);

  fast = arr[0];
  while(slow != fast){
    slow = arr[slow];
    fast = arr[fast];

  }

  return slow;

  



}


int main() {
  vector < int > arr;
  arr = {1,3,4,2,3};
  cout << "The duplicate element is " << findDuplicateOptimal(arr) << endl;
}