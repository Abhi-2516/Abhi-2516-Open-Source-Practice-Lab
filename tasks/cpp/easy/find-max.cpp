/*
TASK:
Find the maximum element in an array.

Input:
n = 5
arr = [2, 9, 1, 7, 4]

Output:
9
*/

#include <iostream>
using namespace std;

int main()
{
    // TODO: Write your logic here
    int n;
    cin >> n;
    int arr[n];
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        arr[i] = temp;
    }
    int max_elem = INT_MIN;
    for (int i = 0; i < n; i++)
    {
        max_elem = max(max_elem, arr[i]);
    }
    cout << max_elem << endl;
    return 0;
}
