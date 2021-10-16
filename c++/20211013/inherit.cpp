#include <iostream>
#include <string>
using namespace std;

class Animal
{
    public:
        string color;
        int weight;
    };
class Dog: public Animal
{
    public:
        string name;
        int age;
        void run();
    };
int main()
{
    Dog dog;
    dog.name = "王才";
    dog.age = 2;
    dog.color = "white";
    dog.weight = 23;
    cout<<"name："<<dog.name<<endl;
    cout<<"age:"<<dog.age<<endl;
    cout<<"color:"<<dog.color<<endl;
    cout<<"weight:"<<dog.weight<<endl;
    }
