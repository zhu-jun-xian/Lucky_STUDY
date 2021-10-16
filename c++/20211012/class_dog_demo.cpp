#include <iostream>
#include <string>
using namespace std;
class  Dog
{
private:
    /* data */
    int age;
    string name;
public:
     Dog(/* args */);
    ~ Dog();
    void run(void)
    {
        age = 55;
        name = "wangcai";
        cout<<name<<":"<<age<<endl;
    }
};

 Dog:: Dog(/* args */)
{

}

 Dog::~ Dog()
{
}
int main()
{
    Dog dog;
    dog.run();
}