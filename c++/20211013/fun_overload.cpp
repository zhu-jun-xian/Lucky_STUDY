#include <iostream>
#include <string>
using namespace std;
class Dog
{
    public:
    string name;
    void getWeight(int Weight)
    {
        cout<<name<<"的体重是："<<Weight<<endl;
    }
    void getWeight(double Weight)
    {
        cout<<name<<"的体重是："<<Weight<<endl;
    }
};
int main()
{
    Dog dog;
    dog.name = "王才";
    dog.getWeight(10);   
    dog.getWeight(10.55);
    return 0;
}