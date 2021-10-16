#include <iostream>
#include <string>
using namespace std;

class Animal
{
    public:
        virtual void run()
        {
            cout<<"Animal的run()方法"<<endl;
        }
    };
class Dog: public Animal
{
    public:
        void run()
        {
            cout<<"dog的run()方法"<<endl;
        }
    };
class Cat: public Animal
{
    public:
        void run()
        {
            cout<<"cat的run()方法"<<endl;
        }
    };
int main()
{
    Animal *animal;
    Dog dog;
    Cat cat;
    animal = &dog;
    animal->run();
    animal = &cat;
    animal->run();
    return 0;
    }
