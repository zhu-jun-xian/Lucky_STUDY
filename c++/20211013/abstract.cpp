#include <iostream>
using namespace std;
class Animal
{
public :
    virtual void run() = 0;

};
class Dog:public Animal
{
public:
    void run()
    {
        cout<<"dog的run方法"<<endl;
    }
};
class Cat:public Animal
{
public:
    void run()
    {
        cout<<"cat的run方法"<<endl;
    }
};
int main()
{
    Dog dog;
    Cat cat;
    dog.run();
    cat.run();
    return 0;
}