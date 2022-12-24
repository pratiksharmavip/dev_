#include <iostream>
using namespace std;
enum player_status
{
    Ps_running,
    Ps_walking,
    Ps_crouching,
    Ps_prone
};
const float running = 100.f;
const float walking = 90.f;
const float crouching = 80.f;
const float prone = 70.f;
player_status num = rudnning;
void switch_on(int player1,num)
{
    player_status player1=num

    switch (player1)
    {
    case Ps_running:
        num = running;
        break;
    case Ps_walking:
        num = walking;
        break;
    case Ps_prone:
        num = prone;
        break;
    case Ps_crouching:
        num = crouching;
        break;

    default:
        break;
    }
    cout << "Movement speed: " << num << endl;
}
int main()
{
    return 0;
}