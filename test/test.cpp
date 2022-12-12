#include <iostream>
using namespace std;
int main()
{
    int x = 0;
    cout << "enter a number" << endl;
    cin >> x;
    int y[x] = {};

    for (int i = 0; i < x; i++)
    {
        cin >> y[i];
    }

    return 0;
}