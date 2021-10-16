#include <iostream>
using namespace std;
namespace A
{
    int x = 3,y;
    void fun(void)
    {
        cin>>y;
        cout<<x<<"*"<<y<<"="<<x*y<<endl;
        }
    }
using namespace A;
int main(void)
{
    fun();
    A::x = 9;
    cout<<x<<endl;
    A::fun();
    return 0;
    }
