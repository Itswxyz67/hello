#include <iostream>
using namespace std;
class Exam { // base class declaration.
public:
void colorP(){
cout<<"Black";
}
};
class Atkt: public Exam // inheriting Exam class.
{
public:
void colorP(){
cout<<"Grey";
}
};
int main(void) {
Atkt kt;
kt.colorP();
}