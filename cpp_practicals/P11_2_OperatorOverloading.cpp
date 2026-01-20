#include <iostream>
using namespace std;
class Math
{
int num;
public:
// setter to set value
void setValue(int val)
{
num = val;
}
// overloading + operator to add values in two objects
Math operator + (Math &obj) {
Math temp;
temp.num = num + obj.num;
return (temp);
}
// overloading - operator to subtract values in two objects
Math operator - (Math &obj){
Math temp;
temp.num = num - obj.num;
return (temp);
}
// overloading * operator to multiply values in two objects
Math operator * (Math &obj){
Math temp;
temp.num = num * obj.num;
return (temp);
}
// overloading / operator to divide values in two objects
Math operator / (Math &obj){
Math temp;
temp.num = num / obj.num;
return (temp);
}
// display result value getter
void getValue(){cout << num;
}
};
int main ()
{
// created objects obj1 and obj2 to perform mathematical operations and resObj to store results
Math obj1, obj2, resObj;
// accepting the values
obj1.setValue(20);
obj2.setValue(10);
cout << "Obj 1: ";
obj1.getValue();
cout << "\nObj 2: ";
obj2.getValue();
// assign result of obj1 and obj2 to resObj addition
resObj = obj1 + obj2;
cout << "\n\nObj1 + Obj2 : " ;
resObj.getValue();
// subtraction
resObj = obj1 - obj2;
cout << "\nObj1 - Obj2 : " ;
resObj.getValue();
// multiplication
resObj = obj1 * obj2;
cout << "\nObj1 * Obj2 : " ;
resObj.getValue();
// division
resObj = obj1 / obj2;
cout << "\nObj1 / Obj2 : " ;
resObj.getValue();
return 0;
}