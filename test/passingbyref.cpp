#include <iostream>
using namespace std;
void add(int &num)
{
    num++;
}

int main()
{
    int a = 1;
    cout << a << endl;

    add(a);

    cout << a << endl;

    return 0;
}
