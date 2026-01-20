#include <iostream>
using namespace std;
// Abstract class
class Shape
{
public:
virtual float calculateArea() = 0; // pure virtual function.
};
class Square : public Shape
{
float a;
public:
Square(float l)
{
a = l;
}
float calculateArea()
{
return a*a;
}
};
class Circle : public Shape
{
float r;
public:
Circle(float x)
{
r = x;
}
float calculateArea()
{
return 3.14*r*r ;
}
};
class Rectangle : public Shape
{
float l;
float b;
public:
Rectangle(float x, float y)
{
l=x;
b=y;
}
float calculateArea()
{
return l*b;
}
};
int main()
{
Shape *shape;
Square s(3.4);
Rectangle r(5,6);
Circle c(7.8);
shape =&s;
int a1 =shape->calculateArea();
shape = &r;
int a2 = shape->calculateArea();
shape = &c;
int a3 = shape->calculateArea();
cout << "Area of the square is " <<a1<< endl;
cout << "Area of the rectangle is " <<a2<< endl;
cout << "Area of the circle is " <<a3<<endl;
return 0;
}