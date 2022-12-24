#include <iostream>
using namespace std;
int main() {
    int x[] = {1, 2, 3, 4, 55, 6, 45, 56786};
    int n = sizeof(x) / sizeof(int);
    int l = 0;
    while (l<n)

    {
        cout << "x[" << l<< "]"
             << " is " << x[l] << endl;
        l++;
    }
    return 0;
}