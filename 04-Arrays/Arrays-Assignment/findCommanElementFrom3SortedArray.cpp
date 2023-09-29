#include <iostream>
#include <vector>
using namespace std;

// o/p
// Common Elements are 20 80 

vector<int > findCommanElementFrom3SortedArray(vector<int > arr,vector<int >brr,vector<int > crr){
    vector<int > ansArr;

    int i = 0 , j = 0,k = 0 ;
    int n1 = arr.size() - 1;
    int n2 = brr.size() - 1;
    int n3 = crr.size() - 1;

    while(i <= n1 && j <= n2 && k <= n3){

        if(arr[i] == brr[j] && brr[j] == crr[k]){
            ansArr.push_back(arr[i]);
            i++;
            j++;
            k++;
        }

        else if(arr[i] < brr[j]){
            i++;
        }

        else if(brr[j] < crr[k]){
            j++;
        }
        else{
            k++;
        }

    }
    return ansArr;

}

int main() {

    vector<int > arr = { 1, 5, 10, 20, 40, 80 };
    vector<int > brr = { 6, 7, 20, 80, 100 };
    vector<int > crr = { 3, 4, 15, 20, 30, 70, 80, 120 };

    vector<int >  ansArr = findCommanElementFrom3SortedArray(arr,brr,crr);
    cout << "Common Elements are ";
    for(auto i : ansArr){
        cout<<i<<" ";
    }
     

    return 0;
}
