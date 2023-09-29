#include <iostream>
#include <vector>
#include <limits.h>
using namespace std;

void Transpose(int arr[][4], int row, int col) {
    int result[4][4]; // Create a temporary array to store the transposed matrix.

    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            result[j][i] = arr[i][j]; // Swap the indices for transposition.
        }
    }

    // Copy the transposed matrix back to the original array.
    for (int i = 0; i < row; i++) {
        for (int j = 0; j < col; j++) {
            arr[i][j] = result[i][j];
        }
    }
}

int main() {
    int arr[4][4] = {{1, 2, 3, 4}, {2, 3, 4, 1}, {5, 6, 1, 3}, {2, 4, 6, 8}};

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    cout << endl;
    cout << endl;
    cout << endl;

    Transpose(arr, 4, 4); // Call the transpose function on the original array.

    // Display the transposed array.
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}
