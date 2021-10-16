#include <iostream>
#include <string>
using namespace std;
class Dog
{
public:
    string name;
    Dog(int i = 0)
    {
        total = i;
    }
    void addFood(int number)
    {
        total = total + number;
    }
    int getFood()
    {
        return total;
    }
private:
    int total;
};
int main()
{
    Dog dog;
    dog.name = "王才";
    dog.addFood(5);
    cout<<dog.getFood()<<endl;
    dog.addFood(55);
    cout<<dog.getFood()<<endl;
    return 0;

}
