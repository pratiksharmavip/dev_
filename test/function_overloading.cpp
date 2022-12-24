#include <iostream>
using namespace std;

void Print(int x){
    cout << x << endl;}
void Print(string x){
    cout << x << endl;}

int main()


{
    int x = 121;
    string ap = "apple";
    Print(x);
    Print(ap);
    

    return 0;
}