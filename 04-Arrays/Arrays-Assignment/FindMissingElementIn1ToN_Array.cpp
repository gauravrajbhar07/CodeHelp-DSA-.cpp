#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

// i/p
// 1,3,4,2,3

// o/p
// The duplicate element is 3

//better approach
int findMissingOptimal2(vector < int > & arr) {
    int xor1 = 0, xor2 = 0;
    int N = arr.size();

    for (int i = 0; i < N - 1; i++) {
        xor2 = xor2 ^ arr[i]; // XOR of array elements
        xor1 = xor1 ^ (i + 1); //XOR up to [1...N-1]
    }
    xor1 = xor1 ^ N; //XOR up to [1...N]

    return (xor1 ^ xor2);
}

// o/p
// The Missing element is 3

//optimalApproach
//using sum all element Method
int findMissingOptimal1(vector < int > & arr){

  int n = arr.size();

    //Summation of first N numbers:
  int sum = (n * (n + 1)) / 2;

  int total_sum = 0;

  for(int i = 0 ; i < arr.size()- 1 ; i++){
    total_sum = total_sum + arr[i];
  }

  return sum ^ total_sum;
}


int main() {
  vector < int > arr;
  arr = {1, 2, 4, 5};
  cout << "The Missing element is " << findMissingOptimal2(arr) << endl;
}