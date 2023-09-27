#include <iostream>
#include <string>
using namespace std;

// 5
// ********1********
// *******2*2*******
// ******3*3*3******
// *****4*4*4*4*****
// ****5*5*5*5*5****

int main()
{
    int n;
    string input;

    cout << "Enter a number between 1 to 9: ";
    getline(cin, input);

    // Check if the input is empty or contains only spaces
    if (input.empty() || input.find_first_not_of(' ') == string::npos)
    {
        cout << "Invalid input. Please enter a number between 1 to 9." << endl;
    }
    else
    {
        // Convert the input to an integer
        n = stoi(input);

        // Check if the input is a valid number
        if (n > 9 || n == 0)
        {
            cout << "Invalid input. Please enter a number between 1 to 9." << endl;
        }
        else
        {
            for (int i = 0; i < n; i++)
            {
                int start_num_index = 8 - i;
                int num = i + 1;
                int count_num = num;

                for (int j = 0; j < 17; j++)
                {
                    if (j == start_num_index && count_num > 0)
                    {
                        cout << num;
                        start_num_index = start_num_index + 2;
                        count_num--;
                    }
                    else
                    {
                        cout << "*";
                    }
                }

                cout << endl;
            }
        }
    }

    return 0;
}
