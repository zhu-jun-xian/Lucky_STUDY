#include <iostream>
#include <string>
using namespace std;

class Dog
{
    public :
        string name;
        void fun();
    };

int main()
{
    Dog dog;
    dog.fun();
    return 0;
    }
void Dog::fun()
{
    this->name = "王才";
    cout<<"小狗的名字是："<<this->name<<endl;
    }
