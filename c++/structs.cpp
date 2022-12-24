#include <iostream>
using namespace std;
struct car
{
    int id;
    string name;
    string color;
    void details()
    {
        cout << "Car Id: " << id << endl;
        cout << "Name: " << name << endl;
        cout << "Color: " << color << endl;
    }
};

int main()
{
    car anna{121, "hello","blue"};
    anna.details();
    return 0;
}